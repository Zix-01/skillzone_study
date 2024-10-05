from django.shortcuts import render

from catalog.models import Product, Category


def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main_page.html', context)
