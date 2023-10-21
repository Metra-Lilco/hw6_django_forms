from django.shortcuts import render

# Create your views here.
from .models import Teacher
from .models import Group


def teacher_form(request):
    return render(request, "teacher_form.html")


def group_form(request):
    return render(request, "group_form.html")
