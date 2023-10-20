from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    musicianList = Musician.objects.order_by('first_name')
    diction = {'musician': musicianList}
    return render(request, 'index.html', context= diction)