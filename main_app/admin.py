from django.contrib import admin
from .models import Pokemon, Feeding, Held_Item

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Feeding)
admin.site.register(Held_Item)