from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import Teacher, Group, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "patronymic", "last_name", "birth_date", "subject"]
        labels = {
            "first_name": _("Ім'я"),
            "patronymic": _("По батькові"),
            "last_name": _("Прізвище"),
            "birth_date": _("Дата народження"),
            "subject": _("Предмет викладання"),
        }
        help_texts = {
            "birth_date": _("<small>(введіть дату у форматі DD.MM.YYYY)</small>")
        }

    def clean_birth_date(self):
        birth_date = self.cleaned_data["birth_date"]
        if birth_date > timezone.now().date():
            raise forms.ValidationError("Дата народження не може бути у майбутньому.")
        age = timezone.now().date().year - birth_date.year
        if age < 18 or age > 80:
            raise forms.ValidationError(
                "Користувач повинен бути не молодше 18 та не старше 80 років."
            )
        return birth_date

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(str(first_name)) >= 151:
            raise forms.ValidationError("Ім'я не може містити більше 150 символів.")
        return first_name

    def clean_patronymic(self):
        patronymic = self.cleaned_data["patronymic"]
        if len(str(patronymic)) >= 151:
            raise forms.ValidationError(
                "По батькові не може містити більше 150 символів."
            )
        return patronymic

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(str(last_name)) >= 201:
            raise forms.ValidationError("Прізвище не може містити більше 200 символів.")
        return last_name

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if len(str(subject)) >= 151:
            raise forms.ValidationError(
                "'Предмет викладання' не може містити більше 150 символів."
            )
        return subject


class GroupForm(forms.ModelForm):
    students_to_add = forms.ModelMultipleChoiceField(
        queryset=Student.objects.none(),
        label="Студенти, що на даний момент не розподілені по групам:",
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Group
        fields = ["name_of_the_group", "curator"]
        labels = {"name_of_the_group": _("Назва групи"), "curator": _("Куратор")}

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        students_without_group = Student.objects.filter(group__isnull=True)

        if students_without_group.exists():
            self.fields["students_to_add"].queryset = students_without_group
        else:
            self.fields["students_to_add"] = forms.CharField(
                label="",
                widget=forms.TextInput(
                    attrs={"class": "form-control", "style": "width: 270px;"}
                ),
                initial="Всі студенти вже розподілені по групах",
                required=False,
                disabled=True,
            )

    def clean_name_of_the_group(self):
        name_of_the_group = self.cleaned_data["name_of_the_group"]
        if len(str(name_of_the_group)) >= 201:
            raise forms.ValidationError(
                "Назва групи не може містити більше 200 символів."
            )
        return name_of_the_group

    def save(self, commit=True):
        group = super().save(commit=False)
        students_to_add = self.cleaned_data["students_to_add"]

        if commit:
            group.save()
            group.students.set(students_to_add)

        return group

    def clean(self):
        cleaned_data = super().clean()
        students_to_add = cleaned_data.get("students_to_add")
        print("Обрані студенти:", students_to_add)
        return cleaned_data


# ДЗ 7. reverse, urls


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "birth_date", "group"]
        labels = {
            "first_name": _("Ім'я"),
            "last_name": _("Прізвище"),
            "birth_date": _("Дата народження"),
            "group": _("Група"),
        }
        help_texts = {
            "birth_date": _("<small>(введіть дату у форматі DD.MM.YYYY)</small>")
        }
        group = forms.ModelChoiceField(
            queryset=Group.objects.all(),
            required=False,
            empty_label="Не призначено",
            widget=forms.Select,
        )

    def clean_birth_date(self):
        birth_date = self.cleaned_data["birth_date"]
        if birth_date > timezone.now().date():
            raise forms.ValidationError("Дата народження не може бути у майбутньому.")
        age = timezone.now().date().year - birth_date.year
        if age < 18 or age > 80:
            raise forms.ValidationError(
                "Студент повинен бути не молодше 18 та не старше 80 років."
            )
        return birth_date

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(str(first_name)) >= 151:
            raise forms.ValidationError("Ім'я не може містити більше 150 символів.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(str(last_name)) >= 201:
            raise forms.ValidationError("Прізвище не може містити більше 200 символів.")
        return last_name
