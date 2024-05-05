from rest_framework.viewsets import ReadOnlyModelViewSet

from django.db.models import Prefetch

from services.models import Subscription, Plan
from services.serializers import SubscriptionSeralizer

from clients.models import Client


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().select_related(
        'client', 'client__user', 'service', 'plan'
    ).only('client__company_name', 'client__user__email',
            'service__name', 'plan_id'
        )
    serializer_class = SubscriptionSeralizer
