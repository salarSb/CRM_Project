from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.ListProduct.as_view(), name='products-list'),

    # DRF URLs
    path('api/v1/products/', views.ProductAPI.as_view(), name='products-api'),
    path('api/v1/organization-products/', views.OrganizationProductAPI.as_view(), name='organization-products-api'),
    path('api/v1/products/<int:pk>/', views.ProductDetailAPI.as_view(), name='product-detail-api'),
    path('api/v1/organization-products/<int:pk>/', views.OrganizationProductDetailAPI.as_view(),
         name='organization-product-detail-api'),
]
