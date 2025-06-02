from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('products', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/category/<slug:slug>/', views.products_by_category),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)