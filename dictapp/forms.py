from django.forms import ModelForm, models
from django import forms

from .models import dictclass

class DictForm(ModelForm):
    class Meta:
        model = dictclass
        fields = ['id', 'palavra', 'palavratrad', 'frase', 'frasetrad', 'figura1', 'som1']
        widgets = {'id': forms.TextInput(attrs={'size': 5}),
                   'palavra': forms.TextInput(attrs={'size': 70}),
                   'palavratrad': forms.TextInput(attrs={'size': 70}),
                   'frase': forms.TextInput(attrs={'size': 70}),
                   'frasetrad': forms.TextInput(attrs={'size': 70}),
                   'figura1': forms.TextInput(attrs={'size': 70}),
                   'som1': forms.TextInput(attrs={'size': 70}),



                   }



        """       
        palavra = forms.CharField(max_length=300)
        palavratrad = forms.CharField(max_length=300)
        frase = forms.CharField(max_length=100)
        frasetrad = forms.CharField(max_length=100)
        """
"""
class DictForm2(forms.Form):
    class Meta:
        model = dictclass
        palavra = forms.CharField(max_length=100)
        palavratrad = forms.CharField(max_length=100)
        frase = forms.CharField(max_length=100)
        frasetrad = forms.CharField(max_length=100)
        
	<!--link rel="stylesheet" href="G:\Django\Projetos\mdic_venv\webapp\static\webapp\css\style.css">-->
	<link rel="stylesheet" href="{% static 'dictapp/css/style.css' %}">
        
        
"""
