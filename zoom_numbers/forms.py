from django import forms
from .models import FoodShelf, YMCA

class YMCAForm(forms.ModelForm):

    class Meta:
        model = YMCA
        fields = ('month', 'year', 'number_visits')


