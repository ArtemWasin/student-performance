from django.contrib import admin
from django.urls import path, include
from performance.views import logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Для встроенных URL авторизации
    path('', include('performance.urls')),  # URL приложения performance
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Добавлен маршрут для выхода
]