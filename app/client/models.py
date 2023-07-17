from __future__ import annotations

from typing import Union

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager

try:
    from service.models import Subscription
except ImportError:
    pass


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Клиент')
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    subscriptions: Union[Subscription, Manager]

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
