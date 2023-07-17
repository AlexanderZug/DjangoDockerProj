from __future__ import annotations

from typing import Union

from django.db import models
from django.db.models import Manager

from client.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    subscriptions: Union[Subscription, Manager]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Plan(models.Model):
    PLAN_TYPES = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    )

    plan_type = models.CharField(
        max_length=10,
        choices=PLAN_TYPES,
        default=PLAN_TYPES[0][0],
        verbose_name='Тип плана',
    )
    discount_percent = models.PositiveIntegerField(verbose_name='Процент скидки', default=0)
    subscriptions: Union[Subscription, Manager]

    def __str__(self):
        return self.plan_type

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'


class Subscription(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Клиент',
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Услуга',
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='План',
    )

    def __str__(self):
        return f'{self.client} - {self.service} - {self.plan}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
