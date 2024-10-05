from django.shortcuts import render

from catalog.models import Product


def main_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main_page.html', context)
