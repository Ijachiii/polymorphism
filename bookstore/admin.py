from django.contrib import admin
from .models import Book, Cart

# Register your models here.
admin.site.register(Book, Cart)