from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import main_page, product_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', main_page, name='main_page'),
    path('catalog/<int:pk>/', product_page, name='product_page'),
]
