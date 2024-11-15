from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import MainPageView, ProductPageView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('catalog/<int:pk>/', cache_page(60)(ProductPageView.as_view()), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
