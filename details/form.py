from django import forms

from details.models import Student


class FormStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentName', 'studentRoll', 'studentAge']
