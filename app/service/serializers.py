from rest_framework import serializers

from service.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.company_name", read_only=True)
    email = serializers.CharField(source="client.user.email", read_only=True)
    plan = PlanSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return instance.price

    class Meta:
        model = Subscription
        fields = ["client_name", "email", "service_id", "plan", "price"]
