from django.contrib import admin
# import your models here
from .models import Puppy, Feeding

# Register your models here
admin.site.register(Puppy)
admin.site.register(Feeding)