from django import forms

class djangoForms(forms.Form):
    name= forms.CharField(label='User Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'style': 'width: 320px'}))
    dob = forms.DateField(label='Date of Birth:', widget=forms.TextInput(attrs={'type': 'date'}))
    email= forms.EmailField(label='User Email')
    boolean = forms.BooleanField(required=False)
    field = forms.CharField(max_length=15, min_length= 5)
    option = forms.ChoiceField(choices=(('', '--Select Option'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'),))
    choices =(('A+','A+'), ('B-','B-'), ('AB+','AB+'), ('O+','O+'))
    multipleOption = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)