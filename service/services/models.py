from django.db import models
from django.core.validators import MaxValueValidator

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f'Service: {self.name}'


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('dicount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return f'Plan type: {self.plan_type}, Discount: {self.discount_percent}'


class Subscription(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT,
        related_name='subscriptions'
    )
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT,
        related_name='subscriptions'
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT,
        related_name='subscriptions'
    )
    
    def __str__(self):
        return f'Client: {self.client.company_name}, Service: {self.service.name}, Plan: {self.plan.plan_type}'
