from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
from .forms import TeacherForm, GroupForm, StudentForm
from .models import Teacher, Group, Student


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
        if not Teacher.objects.exists():
            messages.success(
                request,
                "У групи обов'язково має бути куратор. Тому вас перенаправлено "
                "на сторінку створення викладача, який може виконувати обов'язки куратора групи.",
            )
            return redirect("teacher_form")
        else:
            form.save()
            return redirect("groups_list")
    else:
        print("Invalid form!")
        print(form.errors)
    return render(request, "group_form.html", {"form": form})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, "groups_list.html", {"groups": groups})


# ДЗ 7. reverse, urls


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_form.html", {"form": form})
    form = StudentForm(request.POST)
    if form.is_valid():
        if not Group.objects.exists():
            messages.warning(
                request,
                "Так як ви не обрали групу для студента, можливо ще не створено"
                " жодної групи. Тому вас перенаправлено на сторінку створення групи.",
            )
            return redirect(reverse("group_form"))
        else:
            form.save()
            return redirect("students_list")
    else:
        print("Invalid form!")
        print(form.errors)
    return render(request, "student_form.html", {"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_edit.html", {"form": form})
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("students_list")
    return render(request, "student_edit.html", {"form": form})


def students_list(request):
    students = Student.objects.all()
    return render(request, "students_list.html", {"students": students})


def teacher_edit(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form})
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect("teachers_list")
    return render(request, "teacher_edit.html", {"form": form})
