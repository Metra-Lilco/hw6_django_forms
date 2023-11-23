from django import forms
from django.utils import timezone
import phonenumbers

from .models import Teacher, Group, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "patronymic", "last_name", "birth_date", "subject"]
        labels = {
            "first_name": "Ім'я",
            "patronymic": "По батькові",
            "last_name": "Прізвище",
            "birth_date": "Дата народження",
            "subject": "Предмет викладання",
        }
        help_texts = {
            "birth_date": "<small>(введіть дату у форматі DD.MM.YYYY)</small>"
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
        queryset=Student.objects.all(),
        label="Додати студентів до групи:",
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Group
        fields = ["name_of_the_group", "curator"]
        labels = {"name_of_the_group": "Назва групи", "curator": "Куратор"}

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
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label="Додати студента до таких груп:",
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "birth_date", "phone", "groups"]
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "birth_date": "Дата народження",
            "phone": "Номер телефону",
            "groups": "Групи",
        }
        help_texts = {
            "birth_date": "<small>(введіть дату у форматі DD.MM.YYYY)</small>"
        }
        widgets = {
            "phone": forms.TextInput(attrs={"placeholder": "+380 111 11 11"}),
        }

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

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as e:
            raise forms.ValidationError(e.args[0])
        if not phonenumbers.is_valid_number(parsed):
            raise forms.ValidationError(
                "Схоже що в номері телефону помилка, перевірте уважніше!"
            )

        return phonenumbers.format_number(
            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
