from django.shortcuts import render
from .models import User, Restaurant,Menu
from .serializers import UserSerializer,RestaurantSerializer,MenuSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404

from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
# I will use function based views as I'm writing a lot of behavior

#---user functions---
#create new user account account
@api_view(['POST'])
def createNewUser(request):
    serializer = UserSerializer(data=request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
         return Response({'error': 'Please provide username, password, and email'}, status=400)
   
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
    
    except Exception as e:
       return Response({'error': str(e)}, status=500)

    return Response({'success': 'User created successfully'}, status=201)


#create new admin account

#log in

#forgot password

#get user's profile

#get list of restaurants

#restaurant's profile

#search by restaurantName

#search by the highest rate

#search by most famous restaurants(most searched ones)

#rate restaurant

#review restaurant

#get rates of a restaurant


#get Menu (I'm thinking to make it like a way of flexible display but i need to use categories...)

#rate item in Menu



#list of most nearby restuarants

#---need permission functions---
#only owners can crud their restaurants and its menus

#add restaurant info

#update restaurant info

#delete restaurant info