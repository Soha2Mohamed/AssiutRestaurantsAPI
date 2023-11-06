from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=15)
    mobile = models.CharField(max_length=11)
    address = models.TextField(max_length=30)


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
    restaurantID = models.ForeignKey(Restaurant, related_name='menu', on_delete=models.CASCADE)



