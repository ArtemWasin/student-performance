from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью User
    first_name = models.CharField(max_length=100)  # Имя студента
    last_name = models.CharField(max_length=100)  # Фамилия студента
    group = models.CharField(max_length=50)  # Группа студента

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)  # Название предмета
    description = models.TextField(blank=True)  # Описание предмета (опционально)

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')  # Связь со студентом
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')  # Связь с предметом
    score = models.IntegerField()  # Оценка (например, от 0 до 100)
    date = models.DateField(auto_now_add=True)  # Дата выставления оценки

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.score}"