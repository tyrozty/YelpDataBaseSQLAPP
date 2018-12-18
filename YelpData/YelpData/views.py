from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserForm
from .models import User
from .models import Business
from .models import Location
from .models import Review
from .models import Photo
from .models import Tip
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .filters import UserFilter
from django_filters.views import FilterView

def index(request):
	return HttpResponse("Hello, world. You're at the YelpData index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'YelpData/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'YelpData/home.html'


@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
	model = User
	context_object_name = 'users'
	template_name = 'YelpData/user.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return User.objects.order_by('user_name') 

@method_decorator(login_required, name='dispatch')
class UserDetailView(generic.DetailView):
	model = User
	context_object_name = 'user'
	template_name = 'YelpData/user_detail.html' 
	
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class BusinessListView(generic.ListView):
	model = Business
	context_object_name = 'businesses'
	template_name = 'YelpData/business.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Business.objects.all().order_by('business_name')

@method_decorator(login_required, name='dispatch')
class BusinessDetailView(generic.DetailView):
	model = Business
	context_object_name = 'business'
	template_name = 'YelpData/business_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class LocationListView(generic.ListView):
	model = Location
	context_object_name = 'locations'
	template_name = 'YelpData/location.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Location.objects.all().order_by('location_identifier')

@method_decorator(login_required, name='dispatch')
class LocationDetailView(generic.DetailView):
	model = Location
	context_object_name = 'location'
	template_name = 'YelpData/location_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ReviewListView(generic.ListView):
	model = Review
	context_object_name = 'reviews'
	template_name = 'YelpData/review.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Review.objects.order_by('review_identifier')

@method_decorator(login_required, name='dispatch')
class ReviewDetailView(generic.DetailView):
	model = Review
	context_object_name = 'review'
	template_name = 'YelpData/review_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class TipListView(generic.ListView):
	model = Tip
	context_object_name = 'tips'
	template_name = 'YelpData/tip.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Tip.objects.order_by('tip_id')

@method_decorator(login_required, name='dispatch')
class TipDetailView(generic.DetailView):
	model = Tip
	context_object_name = 'tip'
	template_name = 'YelpData/tip_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PhotoListView(generic.ListView):
	model = Photo
	context_object_name = 'photos'
	template_name = 'YelpData/photo.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Photo.objects.order_by('photo_identifier')

@method_decorator(login_required, name='dispatch')
class PhotoDetailView(generic.DetailView):
	model = Photo
	context_object_name = 'photo'
	template_name = 'YelpData/photo_detail.html'	

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UserCreateView(generic.View):
	model = User
	form_class = UserForm
	success_message = 'User created successfully'
	template_name = 'YelpData/user_new.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			if form.cleaned_data['businesses']:
				for business in form.cleaned_data['businesses']: 
					Review.objects.create(user=user, business=business)
				return redirect(user) 
		return render(request, 'YelpData/user_new.html', {'form': form})
	
	def get(self, request):
		form = UserForm()
		return render(request, 'YelpData/user_new.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(generic.UpdateView):
	model = User
	form_class = UserForm
	context_object_name = 'user'
	success_message = "User updated successfully"
	template_name = 'YelpData/user_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.save()
		old_ids = Review.objects\
			.values_list('business_id', flat=True)\
			.filter(user_id=user.user_id)

		new_businesses = form.cleaned_data['businesses']
		new_ids = []

		for business in new_businesses:
			new_id = business.business_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				Review.objects \
					.create(user=user, business=business)

		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				Review.objects \
					.filter(user_id=user.user_id, business_id=business_id) \
					.delete()

		return HttpResponseRedirect(user.get_absolute_url())


@method_decorator(login_required, name='dispatch')
class UserDeleteView(generic.DeleteView):
	model = User
	success_message = "User deleted successfully"
	success_url = reverse_lazy('user')
	context_object_name = 'user'
	template_name = 'YelpData/user_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		Review.objects \
			.filter(user_id=self.object.user_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())


class PaginatedFilterView(generic.View):
	def get_context_data(self, **kwargs):
		context = super(PaginatedFilterView, self).get_context_data(**kwargs)
		if self.request.GET:
			querystring = self.request.GET.copy()
			if self.request.GET.get('page'):
				del querystring['page']
			context['querystring'] = querystring.urlencode()
		return context

class UserFilterView(PaginatedFilterView, FilterView):
	model = User
	filterset_class = UserFilter
	context_object_name = 'user_list'
	template_name = 'YelpData/user_filter.html'
	paginate_by = 3