from django.contrib import admin
from .models import Dog, Feeding, Toy


# Register your models here.
admin.site.register([Dog, Feeding, Toy])
