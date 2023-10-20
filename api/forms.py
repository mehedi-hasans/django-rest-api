from django import forms
from django.core import validators
class djangoForms(forms.Form):
    name= forms.CharField(label='User Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'style': 'width: 320px'}))
    dob = forms.DateField(label='Date of Birth:', widget=forms.TextInput(attrs={'type': 'date'}))
    email= forms.EmailField(label='User Email')
    boolean = forms.BooleanField(required=False)
    field = forms.CharField(max_length=15, min_length= 5)
    option = forms.ChoiceField(choices=(('', '--Select Option'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'),))
    choices =(('A+','A+'), ('B-','B-'), ('AB+','AB+'), ('O+','O+'))
    multipleOption = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    fieldValidators = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    numberValidators = forms.IntegerField(validators=[validators.MaxValueValidator(10), validators.MinValueValidator(5)])
    #Another Email Verify
    user_email = forms.EmailField()
    user_vemail = forms.EmailField()
    def clean(self):
        all_cleaned_data = super().clean()
        user_email = all_cleaned_data['user_email']
        user_vemail = all_cleaned_data['user_vemail']
        if user_email != user_vemail:
            raise forms.ValidationError('Field Do not match!')