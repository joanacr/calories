from rest_framework import serializers
from meals.models import Meal, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    meals = serializers.PrimaryKeyRelatedField(many=True, queryset=Meal.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'meals')


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        user = serializers.ReadOnlyField(source='user.username')
        fields = ('user', 'datetime', 'calories', 'description')