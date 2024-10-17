from django.urls import reverse_lazy, reverse

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MainPageView(ListView):
    model = Product

class ProductPageView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', 'category')
    success_url = reverse_lazy('catalog:main_page')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', 'category')
    success_url = reverse_lazy('catalog:main_page')

    def get_success_url(self):
        return reverse('catalog:product_page', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:main_page')
