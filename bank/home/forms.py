from .models import Form
from django import forms

class regforms(forms.Form):
    class Meta:
        model = Form
        fields = ['name','dob','age','gender','phone','mail','address','district','branch','accout','card']