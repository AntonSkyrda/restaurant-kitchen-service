from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen_service.models import DishType, Dish, Cook


admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Cook, UserAdmin)
