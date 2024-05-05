from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSeralizer(serializers.ModelSerializer):
    plan = PlanSerializer()

    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    service = serializers.CharField(source='service.name')
    # если поле имеет имя price, то метод должен иметь имя вида get_<имя поля>
    price = serializers.SerializerMethodField()

    def get_price(self, instanse):
        return instanse.price

    class Meta:
        model = Subscription
        fields = (
            'id', 'client_name', 'email', 'service', 'plan', 'price'
        )
