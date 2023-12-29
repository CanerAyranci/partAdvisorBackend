from django.contrib import admin
from .models import Tire, Vehicle, User

admin.site.register(User)
admin.site.register(Tire)
admin.site.register(Vehicle)