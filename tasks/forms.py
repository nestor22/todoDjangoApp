from django import fomrs
from django.forms import ModelForm 
from .models import *


class TaskForm(forms.ModelForm):
    class Metta:
        model = Task
        fieds = '__all__'


