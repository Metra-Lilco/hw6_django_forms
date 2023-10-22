from django.shortcuts import render

# Create your views here.
from .forms import TeacherForm
from .models import Teacher
from .models import Group


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        t = Teacher.objects.create(
            first_name=request.POST["first_name"],
            patronymic=request.POST["patronymic"],
            last_name=request.POST["last_name"],
            birth_date=request.POST["birth_date"],
            subject=request.POST["subject"],
        )
        print("Запис збережено: ", t)
    else:
        print("Invalid form!")
        print(form.errors)
    return render(request, "teacher_form.html", {"form": form})


def group_form(request):
    if request.method == "GET":
        return render(request, "group_form.html")
    print("Дані форми отримано!", request.POST)
    g = Group.objects.create(
        name_of_the_group=request.POST["name_of_the_group"],
        curator=request.POST["curator"],
    )
    print("Запис збережено: ", g)
    return render(request, "group_form.html")
