from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    confirm_published = forms.BooleanField(required=False, label='Подтвердить публикацию')

    class Meta:
        model = Product
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        
        if name and description and name == description:
            raise forms.ValidationError("Название не должно совпадать с описанием")