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
"""@api_view(['POST'])
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

    return Response({'success': 'User created successfully'}, status=201)"""


class UserView(APIView):
      
    #create new user
    def post(self, request):
        userSerializer = UserSerializer(data = request.data)
        if userSerializer.is_valid():
           userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_200_OK)
    #get a specific user or all users
    def get(self, request, id):
        
        if id:
            user = User.objects.filter(id=id).first()
            userSerializer = UserSerializer(user)

        else:
            userQuerySet = User.objects.all()        
            userSerializer = UserSerializer(userQuerySet, many = True)
          
        return Response(userQuerySet.data, status=status.HTTP_200_OK)
    
    def put (self, request, id):
        user = User.objects.filter(id=id).first()
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        userSerializer = UserSerializer(user,data = request.data)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_200_OK)
    
    def patch (self, request, id):
        user = User.objects.filter(id=id).first()
        print(user)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #i think we used partial = True here to update specific fields, what it does is to not perform field validation check for the fields which is missing in the request data.
        userSerializer = UserSerializer(user, data = request.data, partial = True)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_200_OK)
        
    #delete a specific user
    def delete (self, request, id):
        user = User.objects.filter(id=id).first()
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        user.delete()
        return Response(f"user deleted successfully", status=status.HTTP_204_NO_CONTENT)

#create new admin account

#log in

#forgot password

#get user's profile

class RestaurantView(APIView):
      
    #create new restaurant
    #need to restrict permission soon
    def post(self, request):
        restSerializer = RestaurantSerializer(data = request.data)
        if restSerializer.is_valid():
           restSerializer.save()
        return Response(restSerializer.data, status=status.HTTP_200_OK)

    #get list of restaurants
    def get(self, request):
      restQuerySet = Restaurant.objects.all()
      serializer = RestaurantSerializer(restQuerySet, many =True)
      return Response(serializer.data)
    
    #update restaurant
    def put (self, request, id):
        rest = Restaurant.objects.filter(id=id).first()
        if rest is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        restSerializer = RestaurantSerializer(rest,data = request.data)
        restSerializer.is_valid(raise_exception=True)
        restSerializer.save()
        return Response(restSerializer.data, status=status.HTTP_200_OK)
    
    #update specific fields in a restaurant
    def patch (self, request, id):
        rest = Restaurant.objects.filter(id=id).first()
        if rest is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        restSerializer = RestaurantSerializer(rest, data = request.data, partial = True)
        restSerializer.is_valid(raise_exception=True)
        restSerializer.save()
        return Response(restSerializer.data, status=status.HTTP_200_OK)
        
    #delete a restaurant
    def delete (self, request, id):
        rest = Restaurant.objects.filter(id=id).first()
        if rest is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        rest.delete()
        return Response(f"restaurant deleted successfully", status=status.HTTP_204_NO_CONTENT)
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