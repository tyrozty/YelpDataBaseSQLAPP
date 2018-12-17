from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('businesses/', views.BusinessListView.as_view(), name='businesses'),
    path('businesses/<int:pk>/', views.BusinessDetailView.as_view(), name='business_detail'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('tips/', views.TipListView.as_view(), name='tips'),
    path('tips/<int:pk>/', views.TipDetailView.as_view(), name='tip_detail'),
    path('photos/', views.PhotoListView.as_view(), name='photos'),
    path('photos/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('reviews/new/', views.UserCreateView.as_view(), name='user_new'),
    path('reviews/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('reviews/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete')
]