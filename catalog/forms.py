from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_name(self):
        return self.clean_field('name')

    def clean_description(self):
        return self.clean_field('description')

    def clean_field(self, field_name):
        cleaned_data = self.cleaned_data.get(field_name, '')

        for word in self.forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово в поле {field_name}')
        return cleaned_data
