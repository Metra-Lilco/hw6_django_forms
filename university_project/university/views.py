from django.shortcuts import render

# Create your views here.
from .models import Teacher
from .models import Group


def teacher_form(request):
    if request.method == "GET":
        return render(request, "teacher_form.html")
    print("Дані форми отримано!", request.POST)
    t = Teacher.objects.create(
        first_name=request.POST["first_name"],
        patronymic=request.POST["patronymic"],
        last_name=request.POST["last_name"],
        birth_date=request.POST["birth_date"],
        subject=request.POST["subject"],
    )
    print("Запис збережено: ", t)
    return render(request, "teacher_form.html")

def group_form(request):
    return render(request, "group_form.html")
