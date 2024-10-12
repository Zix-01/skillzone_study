from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView


class MainPageView(ListView):
    model = Product

class ProductPageView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', 'category')
    success_url = reverse_lazy('catalog:main_page')
