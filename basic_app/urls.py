from django.urls import path
from basic_app import views

app_name='basic_app'


urlpatterns = [
    path('info/', views.info, name='info'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
