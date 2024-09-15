# main/views.py

# main/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

