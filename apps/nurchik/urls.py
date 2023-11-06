from django.urls import path
from apps.nurchik.views import index, contact, about,course
urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('course', course, name="course"),
]