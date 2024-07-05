from django.contrib import admin

from autos.models import Auto
from autos.models import Make

# Register your models here.

admin.site.register(Make)
admin.site.register(Auto)
