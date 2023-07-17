from rest_framework.viewsets import ReadOnlyModelViewSet

from service.models import Subscription
from service.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
