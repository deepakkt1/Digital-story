from django.shortcuts import render
from django.template import Context, Template
# Create your views here.

def home(request):
	return render(request, 'myapp/index.html')

def game(request):
	return render(request, 'myapp/memory.html')
