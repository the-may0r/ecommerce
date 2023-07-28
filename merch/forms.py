from django import forms

from .models import Merch

class NewMerchForm(forms.ModelForm):
    class Meta:
        model = Merch
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),

            }


class EditMerchForm(forms.ModelForm):
    class Meta:
        model = Merch
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),

            }