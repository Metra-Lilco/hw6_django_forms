from django.shortcuts import render

# Create your views here.
from .models import Teacher


def teacher_form(request):
    return render(request, "teacher_form.html")