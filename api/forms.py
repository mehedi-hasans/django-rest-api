from django import forms

class djangoForms(forms.Form):
    name= forms.CharField()
    email= forms.EmailField()