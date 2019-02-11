from mainapp.models import Product
from django.forms import ModelForm


class ProductsEditForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
