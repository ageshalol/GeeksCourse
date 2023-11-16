from django.contrib import admin
from apps.nurchik import models
# Register your models here.
admin.site.register(models.Settings)
admin.site.register(models.Slide)
admin.site.register(models.About)
admin.site.register(models.Team)
admin.site.register(models.Teachers)
admin.site.register(models.Review)
admin.site.register(models.Gallery)


