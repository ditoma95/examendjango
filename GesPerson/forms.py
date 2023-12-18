from django import forms
from django.forms import ModelForm
from GesPerson.models import Teacher, Student


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'birth_date', 'tel', 'email', 'speciality']

        # labels = {"first_name" : "Votre nom "}
    def first_name(self):
        first_name = self.cleaned_data['first_name']

        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError("Le chiffre n'est pas permis")
        return first_name

    def last_name(self):
        last_name = self.cleaned_data['last_name']

        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError("Le chiffre n'est pas permis")
        return last_name
        

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date', 'tel', 'email', 'pathway']

    def first_name(self):
        first_name = self.cleaned_data['first_name']

        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError("Le chiffre n'est pas permis")
        return first_name

    def last_name(self):
        last_name = self.cleaned_data['last_name']

        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError("Le chiffre n'est pas permis")
        return last_name