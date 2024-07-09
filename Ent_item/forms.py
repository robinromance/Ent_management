from django import forms
from Ent_item.models import Student

# create your forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
