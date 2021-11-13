from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Rock)
admin.site.register(models.Pop)
admin.site.register(models.Jazz)
admin.site.register(models.Traditional)