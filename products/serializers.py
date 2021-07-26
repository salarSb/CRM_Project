from rest_framework import serializers

from products.models import Product, OrganizationProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['usable_for_organization_product'] = OrganizationProductSerializer(
            instance.usable_for_organization_product.all(), many=True).data
        return rep


class OrganizationProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProduct
        fields = '__all__'
