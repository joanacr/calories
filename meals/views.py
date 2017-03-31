from django.http import Http404

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from meals.permissions import IsOwnerOrReadOnly

from meals.models import Meal
from meals.serializers import MealSerializer

from django.contrib.auth.models import User
from meals.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MealList(generics.ListCreateAPIView):
    """
    List all meals, or create a new meal.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    queryset = Meal.objects.all()
    serializer_class = MealSerializer
