from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Feedback , Subject , Profile, Grade
from .forms import StudentForm, FeedbackForm ,SubjectForm , ProfileForm, GradeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


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

def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    students = Student.objects.all()
    return render(request, 'student.html', {'form': form, 'students': students})


def delete_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
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

def subjects(request):
        
    if request.method =='POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm()
    subjects = Subject.objects.all()
    context = {'subjects': subjects,
            'form': form,}
    return render(request, 'subject.html' ,context)

def edit_subject(request, slug):
    subject = get_object_or_404(Subject, slug=slug)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm(instance=subject)

    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'form': form, 'subjects': subjects})


def delete_subject(request,slug):
    subject = Subject.objects.get(slug=slug)
    subject.delete()
    return redirect('subjects')


@login_required
def grades_page(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm()

    grades = Grade.objects.all()
    return render(request, 'grade.html', {'form': form, 'grades': grades})  

@login_required
def edit_grade(request, id):
    grade = get_object_or_404(Grade, id=id)

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm(instance=grade)

    grades = Grade.objects.all()
    return render(request, 'grade.html', {'form': form, 'grades': grades})

@login_required
def delete_grade(request, id):
    grade = get_object_or_404(Grade, id=id)
    grade.delete()
    return redirect('grades') 


@login_required
def profile_page(request):
    return render(request, 'profile.html')

def leaderboard_page(request):
    top_students = (
        Grade.objects
        .values('student')
        .annotate(total=Sum('score'))
        .order_by('-total')[:5]
    )

    leaderboard = []

    for item in top_students:
        student_grades = Grade.objects.filter(student=item['student'])
        student_name = student_grades.first().student.name
        subjects = [grade.subject.name for grade in student_grades]

        leaderboard.append({
            'student_name': student_name,
            'subjects': subjects,
            'total': item['total'],
        })

    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})
