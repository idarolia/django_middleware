from django.http import HttpResponse
from django.shortcuts import render
from .models import Error

def index(request):
    all_errors = Error.objects.all()

    context = {
        'all_errors': all_errors
    }

    return render(request, 'error/index.html', context)
