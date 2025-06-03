from django import forms
from .models import Student, Subject, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'first_name', 'last_name', 'group']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }