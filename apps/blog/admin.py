from django.contrib import admin

from apps.blog import models

# Register your models here.
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    
admin.site.register(models.Blog, BlogFilterAdmin)
