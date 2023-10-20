from django import forms

class djangoForms(forms.Form):
    name= forms.CharField(label='User Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'style': 'width: 320px'}))
    dob = forms.DateField(label='Date of Birth:', widget=forms.TextInput(attrs={'type': 'date'}))
    email= forms.EmailField(label='User Email')