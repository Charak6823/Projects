from django import forms
from .models import RoomType

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name_kh', 'name']
        widgets = {
            'name_kh': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
