from django.shortcuts import render, get_object_or_404

from catalog.models import Product
from django.views.generic import ListView

class MainPageView(ListView):
    model = Product


def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_page.html', context)
