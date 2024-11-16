from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, ModeratorForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.services import get_categories


class MainPageView(LoginRequiredMixin, ListView):
    model = Product


class ProductPageView(LoginRequiredMixin, DetailView):
    model = Product

    def get_queryset(self):
        return get_categories()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied()

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:main_page')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:main_page')

    def get_success_url(self):
        return reverse('catalog:product_page', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        # Создание формы для версий продукта
        ProductFormset = inlineformset_factory(Product, Version, ProductForm, extra=1)

        # Обработка POST запроса
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)

        # Получение активной версии продукта
        active_version = Version.objects.filter(product=self.object, is_active=True).first()

        # Проверка на активную версию продукта
        if active_version:
            context_data['active_version'] = active_version
        else:
            context_data['active_version'] = None  # или сообщение о том, что активной версии нет

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            self.object.user = self.request.user   # привязка продукта к юзеру
            self.object.save()
            formset.instance = self.object  # Установление связи между продуктом и версиями
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.can_change_product_description') and user.has_perm('catalog.can_change_product_category'):
            return ModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:main_page')
