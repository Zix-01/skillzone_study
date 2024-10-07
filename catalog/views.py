from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def main_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'cards_list.html', context)

def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_page.html', context)
