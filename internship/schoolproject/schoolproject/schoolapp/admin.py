from django.contrib import admin

# Register your models here.
from .models import destination
admin.site.register(destination)
from .models import team
admin.site.register(team)