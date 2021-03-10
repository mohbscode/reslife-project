from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # exclude = ['student']

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'work_order': forms.Select(attrs={'class': 'form-control'}),
            'dorm': forms.Select(attrs={'class': 'form-control'}),
            # 'room': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            # 'repair_date': forms.TextInput(attrs={'class': 'form-control'}),

        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dorm': forms.Select(attrs={'class': 'form-control'}),
            # 'room': forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone': forms.Select(attrs={'class': 'form-control'}),

        }
