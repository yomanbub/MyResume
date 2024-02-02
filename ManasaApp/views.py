# ManasaApp/views.py

from django.shortcuts import render

def resume(request):
    return render(request, 'ManasaAppDinchak/manasa_template.html')
