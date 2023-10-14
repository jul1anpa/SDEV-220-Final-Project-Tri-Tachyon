from django.contrib import admin
from .models import Item, Hold

# Register your models here.
admin.site.register(Item)
admin.site.register(Hold)