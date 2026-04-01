from django import forms
from .models import Student, Feedback ,Subject , Profile , Grade


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'image']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'message']
        
class SubjectForm(forms.ModelForm):
        class Meta:
            model = Subject
            fields = ['name', 'code', 'description']  
        

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']            