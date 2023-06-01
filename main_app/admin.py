from django.contrib import admin
# import your models here
from .models import Puppy, Feeding, Toy

# Register your models here
admin.site.register(Puppy)
admin.site.register(Feeding)
admin.site.register(Toy)