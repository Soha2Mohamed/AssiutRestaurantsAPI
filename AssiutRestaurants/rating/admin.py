from django.contrib import admin

# Register your models here.
from .models import User, Restaurant

admin.site.register(Restaurant)
