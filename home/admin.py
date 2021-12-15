from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Task)   #call method
admin.site.register(Book)