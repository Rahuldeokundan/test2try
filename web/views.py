from django.shortcuts import render
from django.http import HttpResponse
from .models import Top5Institute

# Create your views here.
def index(request):
    T5I= Top5Institute.objects.all()
    print(T5I)
    return render(request, 'index.html', {'Top5Institute':T5I})

