from django.urls import path
from user.views import register_view
from django.contrib.auth import views

urlpatterns = [
    path('register/' , register_view , name='create'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='user_login')
]
