from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from performance.models import Student

class Command(BaseCommand):
    help = 'Creates user groups and default users'

    def handle(self, *args, **kwargs):
        # Создание групп
        admin_group, _ = Group.objects.get_or_create(name='Administrators')
        teacher_group, _ = Group.objects.get_or_create(name='Teachers')
        student_group, _ = Group.objects.get_or_create(name='Students')

        # Назначение разрешений
        admin_permissions = Permission.objects.all()
        admin_group.permissions.set(admin_permissions)

        teacher_permissions = Permission.objects.filter(
            codename__in=['add_grade', 'change_grade', 'view_grade', 'view_student', 'view_subject']
        )
        teacher_group.permissions.set(teacher_permissions)

        student_permissions = Permission.objects.filter(codename__in=['view_grade', 'view_student'])
        student_group.permissions.set(student_permissions)

        # Создание пользователей
        admin, _ = User.objects.get_or_create(username='admin')
        admin.set_password('admin123')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        admin.groups.add(admin_group)

        teacher, _ = User.objects.get_or_create(username='teacher')
        teacher.set_password('teacher123')
        teacher.save()
        teacher.groups.add(teacher_group)

        student_user, _ = User.objects.get_or_create(username='student')
        student_user.set_password('student123')
        student_user.save()
        student_user.groups.add(student_group)

        # Связь пользователя student с моделью Student
        Student.objects.get_or_create(
            user=student_user,
            defaults={'first_name': 'John', 'last_name': 'Doe', 'group': 'A-101'}
        )

        self.stdout.write(self.style.SUCCESS('Successfully created groups and users'))