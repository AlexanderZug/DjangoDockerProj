from django.db.models import Prefetch, F, Sum
from django.core.cache import cache
from rest_framework.viewsets import ReadOnlyModelViewSet

from client.models import Client
from service.models import Subscription
from service.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        "plan",
        Prefetch(
            "client",
            queryset=Client.objects.all()
            .select_related("user")
            .only("company_name", "user__email"),
        ),
    ).annotate(price=F("service__price") - F("service__price") * (F("plan__discount_percent") / 100.00))
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        price_cache = cache.get("price_cache")
        if price_cache:
            total_price = price_cache
        else:
            total_price = queryset.aggregate(total_price=Sum("price")).get("total_price")
            cache.set("price_cache", total_price, timeout=60)

        response_data = {"result": response.data, "total_price": total_price}
        response.data = response_data

        return response
