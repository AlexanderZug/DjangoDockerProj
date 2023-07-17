from rest_framework import serializers

from service.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name', read_only=True)
    email = serializers.CharField(source='client.user.email', read_only=True)

    class Meta:
        model = Subscription
        fields = ['client_name', 'email', 'service_id', 'plan_id']