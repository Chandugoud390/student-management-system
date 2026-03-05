from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'current_academic_level',
            'enrollement_status',
            'photo',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Enter last name'
            }),
            'birth_date': forms.DateInput(attrs={
                'class' : 'form-control',
                'type': 'date'
            }),
            'gender': forms.RadioSelect(
                choices=Student.GENDER_CHOICES,
                attrs={'class': 'ustom-radio-buttons'}
            ),
            'current_academic_level': forms.Select(
                choices=Student.ACADEMIC_LEVEL_CHOICES,
                attrs={'class': 'form-select'}
            ),
            'enrollement_status': forms.Select(
                choices=Student.ENROLLEMENT_STATUS_CHOICES,
                attrs={'class': 'form-select'}
            ),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }