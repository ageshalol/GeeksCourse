from django.urls import path
from apps.blog.views import blog,blog_detail
urlpatterns = [
    path('blog', blog, name="blog"),
    path('blog_detail/<int:id>/', blog_detail, name="blog_detail"),
    
]