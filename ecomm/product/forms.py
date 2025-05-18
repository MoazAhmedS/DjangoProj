from django import forms
from .models import product, category

class InsertProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'image',
            'sku',
            'categoryobj',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter stock quantity'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter SKU'}),
            'categoryobj': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateProductForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'})
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product description'})
    )
    price = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price', 'step': '0.01'})
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    categoryobj=forms.ChoiceField(choices=((c.id,c.name) for c in category.getAll()),
                               widget=forms.Select(attrs={'class': 'form-control'}),
)

