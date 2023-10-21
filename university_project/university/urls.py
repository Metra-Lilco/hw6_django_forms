from django.urls import path

from .views import teacher_form, group_form


urlpatterns = [
    path("teacher", teacher_form, name="teacher_form"),
    path("group", group_form, name="group_form"),
]
