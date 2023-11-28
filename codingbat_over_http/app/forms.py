from django import forms

class FrontForm(forms.Form):
    input_text = forms.CharField()
    num_r = forms.IntegerField()

class TeenForm(forms.Form):
    n1 = forms.IntegerField()
    n2 = forms.IntegerField()
    n3 = forms.IntegerField()

class XYZForm(forms.Form):
    str = forms.CharField()

class AvgForm(forms.Form):
    n1 = forms.IntegerField()
    n2 = forms.IntegerField()
    n3 = forms.IntegerField()
    n4 = forms.IntegerField()
    n5 = forms.IntegerField()