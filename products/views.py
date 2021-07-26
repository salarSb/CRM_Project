from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.models import Product, OrganizationProduct
from products.serializers import ProductSerializer, OrganizationProductSerializer


class ProductAPI(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ProductDetailAPI(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class OrganizationProductAPI(ListCreateAPIView):
    queryset = OrganizationProduct.objects.all()
    serializer_class = OrganizationProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class OrganizationProductDetailAPI(RetrieveUpdateAPIView):
    queryset = OrganizationProduct.objects.all()
    serializer_class = OrganizationProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
