from .models import *
from django.shortcuts import render, redirect

#Instruction : Use and pass only singular variable name throught the application.

def manager(request):
    return render(request, 'index.html')