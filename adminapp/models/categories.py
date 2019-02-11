from mainapp.models import ProductCategory
from django.forms import ModelForm


class CategoryEditForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class CategoryCreateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
