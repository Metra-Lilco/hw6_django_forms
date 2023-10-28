from django import forms
from django.utils import timezone
from .models import Teacher, Group


class TeacherForm(forms.Form):
    first_name = forms.CharField(label="Ім'я")
    patronymic = forms.CharField(label="По батькові")
    last_name = forms.CharField(label="Прізвище")
    birth_date = forms.DateField(
        label="Дата народження",
        help_text="<small>(введіть дату у форматі YYYY-MM-DD)</small>",
    )
    subject = forms.CharField(label="Предмет викладання")

    def clean_birth_date(self):
        birth_date = self.cleaned_data["birth_date"]
        if birth_date > timezone.now().date():
            raise forms.ValidationError("Дата народження не може бути у майбутньому.")
        age = timezone.now().date().year - birth_date.year
        if age < 18 or age > 80:
            raise forms.ValidationError(
                "Користувач повинен бути не молодше 18 та не старше 80 років."
            )

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(str(first_name)) >= 151:
            raise forms.ValidationError("Ім'я не може містити більше 150 символів.")

    def clean_patronymic(self):
        patronymic = self.cleaned_data["patronymic"]
        if len(str(patronymic)) >= 151:
            raise forms.ValidationError(
                "По батькові не може містити більше 150 символів."
            )

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(str(last_name)) >= 201:
            raise forms.ValidationError("Прізвище не може містити більше 200 символів.")

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if len(str(subject)) >= 151:
            raise forms.ValidationError(
                "'Предмет викладання' не може містити більше 150 символів."
            )


class GroupForm(forms.Form):
    name_of_the_group = forms.CharField(label="Назва групи")
    curator = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        label="Куратор",
        empty_label="Оберіть куратора з вчителів",
    )

    def clean_name_of_the_group(self):
        name_of_the_group = self.cleaned_data["name_of_the_group"]
        if len(str(name_of_the_group)) >= 201:
            raise forms.ValidationError(
                "Назва групи не може містити більше 200 символів."
            )

    class Meta:
        model = Group
        fields = ["name_of_the_group", "curator"]
