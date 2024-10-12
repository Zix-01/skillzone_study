from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import MainPageView, ProductPageView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('catalog/<int:pk>/', ProductPageView.as_view(), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
]
