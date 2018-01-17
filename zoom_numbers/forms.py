from django import forms
from .models import FoodShelf, YMCA, PoliceCalls, QuestionMonth

class YMCAForm(forms.ModelForm):

    class Meta:
        model = YMCA
        fields = ('month', 'year', 'number_visits')

class FoodShelfForm(forms.ModelForm):

    class Meta:
        model = FoodShelf
        fields = ('month', 'year', 'number_visits')

class PoliceCallsForm(forms.ModelForm):

    class Meta:
        model = PoliceCalls
        fields = ('month', 'year', 'num_noise_calls')

class QuestionMonthForm(forms.ModelForm):

    class Meta:
        model = QuestionMonth
        fields = ('month', 'year', 'question', 'category_one', 'category_one_count', 'category_two', 'category_two_count', 'category_three', 'category_three_count', 'category_four', 'category_four_count')