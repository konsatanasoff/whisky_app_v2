from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('', views.UserListView.as_view(), name='user-list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path("details", views.UserDetailAPI.as_view(), name='user-detail'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
