from django.shortcuts import render, redirect

# Create your views here.
from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


def index(request):
    return render(request, "index.html")


def university(request):
    return redirect("index")


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("teachers_list")
    else:
        print("Invalid form!")
        print(form.errors)
    return render(request, "teacher_form.html", {"form": form})


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers_list.html", {"teachers": teachers})


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})
    form = GroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("groups_list")
    else:
        print("Invalid form!")
        print(form.errors)
    return render(request, "group_form.html", {"form": form})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, "groups_list.html", {"groups": groups})
