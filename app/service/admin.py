from django.contrib import admin

from service.models import Subscription, Service, Plan


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price"]
    search_fields = ["name", "description"]
    empty_value_display = "-empty-"


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["plan_type", "discount_percent"]
    search_fields = ["plan_type"]
    empty_value_display = "-empty-"


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["client", "service", "plan"]
    search_fields = ["client", "service", "plan"]
    empty_value_display = "-empty-"
