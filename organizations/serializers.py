from rest_framework import serializers

from organizations.models import Organization
from products.serializers import OrganizationProductSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    submit_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Organization
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(OrganizationSerializer, self).to_representation(instance)
        rep['products'] = OrganizationProductSerializer(instance.products.all(), many=True).data
        return rep
