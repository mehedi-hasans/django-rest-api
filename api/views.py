from django.shortcuts import render
from .models import *
from . import forms
# Create your views here.
def index(request):
    musicianList = Musician.objects.order_by('first_name')
    diction = {'musician': musicianList}
    return render(request, 'index.html', context= diction)

def form(request):
    djangoForm = forms.djangoForms()
    diction = {'newForm': djangoForm, 'heading': 'Form from Django Library'}

    if request.method =='POST':
        djangoForm = forms.djangoForms(request.POST)
        diction.update({'newForm': djangoForm})
        diction.update({'Ematch': 'Match Perfectly'})
        if djangoForm.is_valid():
            name = djangoForm.cleaned_data['name']
            dob = djangoForm.cleaned_data['dob']
            email = djangoForm.cleaned_data['email']
            boolean = djangoForm.cleaned_data['boolean']
            field = djangoForm.cleaned_data['field']
            option = djangoForm.cleaned_data['option']
            multipleOption = djangoForm.cleaned_data['multipleOption']
            fieldValidators = djangoForm.cleaned_data['fieldValidators']
            numberValidators = djangoForm.cleaned_data['numberValidators']
           

            diction.update({'name': name})
            diction.update({'dob': dob})
            diction.update({'email': email})
            diction.update({'boolean': boolean})
            diction.update({'field': field})
            diction.update({'option': option})
            diction.update({'multipleOption': multipleOption})
            diction.update({'fieldValidators': fieldValidators})
            diction.update({'numberValidators': numberValidators})
            diction.update({'formSubmited': 'Yes'})



    return render(request, 'form.html', diction)