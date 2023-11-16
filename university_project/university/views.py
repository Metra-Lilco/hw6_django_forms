from django.shortcuts import render, redirect, get_object_or_404
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


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        teacher.delete()
        messages.success(
            request,
            f"Викладача {teacher.first_name} {teacher.patronymic} {teacher.last_name} успішно видалено.",
        )
        return redirect("teachers_list")

    return render(request, "teacher_delete.html", {"teacher": teacher})


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


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == "POST":
        group.delete()
        messages.success(request, f"Групу {group.name_of_the_group} успішно видалено.")
        return redirect("groups_list")

    return render(request, "group_delete.html", {"group": group})


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


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(
            request,
            f"Студента {student.first_name} {student.last_name} успішно видалено.",
        )
        return redirect("students_list")

    return render(request, "student_delete.html", {"student": student})


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


def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupForm(instance=group)
        return render(request, "group_edit.html", {"form": form})
    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        form.save()
        return redirect("groups_list")
    return render(request, "group_edit.html", {"form": form})
