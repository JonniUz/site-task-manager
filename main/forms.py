from django.forms import TextInput, Textarea

from .models import Task
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input task'
            }),
        }