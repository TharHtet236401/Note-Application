from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.
def home(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'base/home.html', context)


