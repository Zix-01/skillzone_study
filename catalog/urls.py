from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import MainPageView, product_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('catalog/<int:pk>/', product_page, name='product_page'),
]
