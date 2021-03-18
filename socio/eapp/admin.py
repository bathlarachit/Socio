from django.contrib import admin
from eapp import models
# Register your models here.
admin.site.register(models.chat)
admin.site.register(models.friend)
admin.site.register(models.Profile)
admin.site.register(models.post)
