from django import forms
from .models import Employee

class employeeform(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields  = "__all__"
        #fields = ['name','email','age','password','salary']
