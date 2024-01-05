from django import forms
from .models import department,Faculty,Type,Subject,Student,Complaint,HOD,Director

class departmentform(forms.ModelForm):
    class Meta:
        model = department
        fields = ['dept_name']
class Typeform(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type_name']
class Subjectform(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name','dept_name']

class student_form(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ["s_name","enrollment_no","email","Div","Roll_no","password","department"]
        fields = ["Div","department"]

class edit_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["s_name","enrollment_no","email","Div","Roll_no","password","department"]
        widgets = {
            's_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class facultyform(forms.ModelForm):
    class Meta:
        model = Faculty
        # fields = ['faculty_name','email','subject','department_name','password']
        fields = ['subject','department_name']

class edit_faculty_form(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_name','email','subject','department_name','password']
        widgets = {
            'id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class complaint_form(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
class edit_complaint_form(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        widgets = {
            'id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class HOD_form(forms.ModelForm):
    class Meta:
        model =HOD
        fields = ['hod_Name','email','dept','password']


class HOD_edit(forms.ModelForm):
    class Meta:
        model =HOD
        fields = ['hod_Name','email','dept','password']
        widgets = {
            'id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class Director_form(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['director_name','email','password']
