from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.db.models import Avg
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

def is_admin(user):
    return user.groups.filter(name='Administrators').exists()

def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()

def is_student(user):
    return user.groups.filter(name='Students').exists()

@login_required
def home(request):
    return render(request, 'performance/home.html')

@login_required
def student_list(request):
    if is_student(request.user):
        try:
            student = Student.objects.get(user=request.user)
            grades = Grade.objects.filter(student=student)
            return render(request, 'performance/student_list.html', {'students': [student], 'grades': grades})
        except Student.DoesNotExist:
            return render(request, 'performance/student_list.html', {'students': []})
    students = Student.objects.all()
    return render(request, 'performance/student_list.html', {'students': students})

@login_required
@user_passes_test(is_admin)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'performance/student_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'performance/student_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'performance/student_confirm_delete.html', {'student': student})

@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'performance/subject_list.html', {'subjects': subjects})

@login_required
@user_passes_test(is_admin)
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'performance/subject_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'performance/subject_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'performance/subject_confirm_delete.html', {'subject': subject})

@login_required
def grade_list(request):
    if is_student(request.user):
        try:
            student = Student.objects.get(user=request.user)
            grades = Grade.objects.filter(student=student)
        except Student.DoesNotExist:
            grades = []
    else:
        grades = Grade.objects.all()
    return render(request, 'performance/grade_list.html', {'grades': grades})

@login_required
@user_passes_test(is_teacher)
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'performance/grade_form.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'performance/grade_form.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'performance/grade_confirm_delete.html', {'grade': grade})

@login_required
def reports(request):
    # Средние баллы по студентам
    student_averages = Student.objects.annotate(avg_score=Avg('grades__score'))
    # Средние баллы по предметам
    subject_averages = Subject.objects.annotate(avg_score=Avg('grades__score'))
    # Лучший студент
    best_student = student_averages.order_by('-avg_score').first()
    # Худший студент
    worst_student = student_averages.order_by('avg_score').first()
    return render(request, 'performance/reports.html', {
        'student_averages': student_averages,
        'subject_averages': subject_averages,
        'best_student': best_student,
        'worst_student': worst_student,
    })

# Кастомное представление для выхода
class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']  # Разрешаем GET и POST

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

logout = CustomLogoutView.as_view(next_page=reverse_lazy('home'))