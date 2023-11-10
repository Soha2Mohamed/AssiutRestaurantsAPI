from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from .permissions import permissions
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):

    class Status(models.TextChoices):
        OPEN = 'open','Open'
        CLOSED = 'closed', 'Closed'

    class Rating(models.IntegerChoices):
        VERY_BAD = 1
        BAD = 2
        NEUTRAL = 3
        GOOD = 4
        VERY_GOOD =5
    
    restaurantId = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=15)
    mobile = models.CharField(max_length=11)
    address = models.TextField(max_length=30)
    status = models.CharField(max_length=6,choices=Status.choices, default=Status.OPEN)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.NEUTRAL)

class Menu(models.Model):
    class Category(models.TextChoices):
        BREAKFAST = 'br', 'BreakFast'
        APPETIZERS = 'ap', 'Appetizers'
        SALAD = 'sa', 'Salad'
        BURGER = 'bu', 'Burger'
        PIZZA = 'pi', 'Pizza'
        CHICKEN = 'ch', 'Chicken'
        PASTA = 'pa' , 'Pasta'
        DESSERT = 'de', 'Dessert'
    itemId = models.BigAutoField(primary_key=True)
    itemName = models.CharField(max_length=15)
    description = models.TextField(max_length=50)
    category  = models.CharField(max_length=2,choices=Category.choices, default=Category.PIZZA)
    restaurantID = models.OneToOneField(Restaurant, related_name='menu', on_delete=models.CASCADE)


#function to create a token automatically everytime a user is created
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created , **kwargs):
    if created:
        Token.objects.create(user = instance)
        


