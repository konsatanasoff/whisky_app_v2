from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
