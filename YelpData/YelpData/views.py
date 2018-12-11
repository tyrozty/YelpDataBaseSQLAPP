from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import User


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
