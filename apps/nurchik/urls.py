from django.urls import path
from apps.nurchik import views
urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('course', views.course, name="course"),
    path('gallery', views.gallery, name="gallery"),
]