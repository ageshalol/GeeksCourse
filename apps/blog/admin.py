from django.contrib import admin

from apps.blog import models

# Register your models here.
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')

class CourseFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'teachers')
    search_fields = ('title', 'teachers')
 
admin.site.register(models.Blog, BlogFilterAdmin)
admin.site.register(models.Course, CourseFilterAdmin)

