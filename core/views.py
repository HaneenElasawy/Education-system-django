from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Feedback
from .forms import StudentForm, FeedbackForm


def home(request):
    return render(request, 'home.html')


def students_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'student.html', {'form': form, 'students': students})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students')


def contact_page(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by('-date_added')
    return render(request, 'contact.html', {'form': form, 'feedbacks': feedbacks})