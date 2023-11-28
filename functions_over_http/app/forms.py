from django import forms

class HeyYouForm(forms.Form):
    input_name = forms.CharField()

class HowOldForm(forms.Form):
    this_year = forms.IntegerField()
    birth_year = forms.IntegerField()

class OrderForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()