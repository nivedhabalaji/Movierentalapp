from django import forms
from .models import Customers,Movies


class customerp(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('firstname', 'lastname','email','contact','address','city','state','zipcode','country')

class moviep(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('moviename', 'category','price')


