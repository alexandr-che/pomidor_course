from rest_framework.viewsets import ReadOnlyModelViewSet

from django.db.models import F, Sum

from services.models import Subscription
from services.serializers import SubscriptionSeralizer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().select_related(
        'client', 'client__user', 'service', 'plan'
    ).only(
        'client__company_name', 'client__user__email',
        'service__name', 'plan_id'
        ).annotate(
            price=F('service__full_price') - F('service__full_price') * 
                    (F('plan__discount_percent') / 100.00)
            )
    serializer_class = SubscriptionSeralizer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {'result': response.data}
        response_data['totla_amount'] = queryset.aggregate(
            total=Sum('price')
        ).get('total')
        response.data = response_data
        return response
