from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.DrinkListView.as_view(), name='drink-list'),
    path('create/', views.DrinkCreateView.as_view(), name='create-drink'),
    path('drink/<int:pk>/', views.DrinkDetailView.as_view(), name='model-detail'),
]