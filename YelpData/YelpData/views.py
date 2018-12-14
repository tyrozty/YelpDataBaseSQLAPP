from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import User
from .models import Business
from .models import Review
from .models import Photo


def index(request):
	return HttpResponse("Hello, world. You're at the YelpData index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'YelpData/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'YelpData/home.html'

class UserListView(generic.ListView):
	model = User
	context_object_name = 'users'
	template_name = 'YelpData/user.html'
	paginate_by = 50

	def get_queryset(self):
		return User.objects.order_by('user_name') 

class UserDetailView(generic.DetailView):
	model = User
	context_object_name = 'user'
	template_name = 'YelpData/user_detail.html' 


class BusinessListView(generic.ListView):
	model = Business
	context_object_name = 'businesses'
	template_name = 'YelpData/business.html'
	paginate_by = 50

	def get_queryset(self):
		return Business.objects.all().order_by('business_name')

class BusinessDetailView(generic.ListView):
	model = Business
	context_object_name = 'business'
	template_name = 'YelpData/business_detail.html'


class ReviewListView(generic.ListView):
	model = Review
	context_object_name = 'reviews'
	template_name = 'YelpData/review.html'
	paginate_by = 50

	def get_queryset(self):
		return Review.objects.order_by('review_identifier')

class ReviewDetailView(generic.ListView):
	model = Review
	context_object_name = 'review'
	template_name = 'YelpData/review_detail.html'


class PhotoListView(generic.ListView):
	model = Photo
	context_object_name = 'photos'
	template_name = 'YelpData/photo.html'
	paginate_by = 50

	def get_queryset(self):
		return Photo.objects.order_by('photo_identifier')

class PhotoDetailView(generic.ListView):
	model = Photo
	context_object_name = 'photo'
	template_name = 'YelpData/photo_detail.html'	