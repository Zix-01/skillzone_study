from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):

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


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category')