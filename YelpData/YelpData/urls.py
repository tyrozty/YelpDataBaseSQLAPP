from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]