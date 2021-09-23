from django.forms import ModelForm
from django import forms

from mainapp.models import GalleryCafe


class GalleryCafeCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = GalleryCafe
        fields = ['name', 'image1', 'image2', 'image3', 'content']