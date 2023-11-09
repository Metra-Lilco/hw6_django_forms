from django.urls import path

from .views import (
    teacher_form,
    group_form,
    teachers_list,
    groups_list,
    index,
    university,
    student_form,
    students_list,
)


urlpatterns = [
    path("teacher", teacher_form, name="teacher_form"),
    path("group", group_form, name="group_form"),
    path("student", student_form, name="student_form"),
    path("teachers", teachers_list, name="teachers_list"),
    path("groups", groups_list, name="groups_list"),
    path("students", students_list, name="students_list"),
    path("", index, name="index"),
    path("university", university, name="university"),
]
