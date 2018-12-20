from YelpData.models import User, Review
from api.serializers import UserSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = User.objects.order_by('user_name') # must need related?
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		self.perform_destroy(self, user)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()

