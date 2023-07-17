from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'address', 'get_subscription']
    search_fields = ('company_name', 'address')
    empty_value_display = '-empty-'

    def get_subscription(self, obj):
        return obj.subscriptions.all()
