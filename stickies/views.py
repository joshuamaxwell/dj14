from django.http import HttpResponse
from django.shortcuts import render
from models import Note

def index(request):
    return render(request, 'index.html', {'notes': Note.objects.all()})