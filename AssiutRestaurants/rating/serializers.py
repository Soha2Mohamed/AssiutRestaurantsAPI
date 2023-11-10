from rest_framework import serializers
from rating.models import  Restaurant, Menu
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields=['name','mobile','address','status','rating']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields='__all__'