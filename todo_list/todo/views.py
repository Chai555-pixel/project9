# In todo/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'todo/home.html')  # Rendering the home.html template
