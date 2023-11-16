from django.shortcuts import render
from apps.blog.models import Blog,Course
from apps.nurchik import models
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    about = models.About.objects.latest('id')
    teachers = models.Teachers.objects.all()
    review = models.Review.objects.all()
    course = Course.objects.order_by('?')[:3]
    blog = Blog.objects.order_by('?')[:3]
    if request.method =="POST":
        username = request.POST.get('username')
        work = request.POST.get('work')
        message = request.POST.get('message')
        reserv = models.Review.objects.create(username = username,work = work,message=message)
    return render(request, "base/index-3.html", locals())

def contact(request):
    settings = models.Settings.objects.latest('id')  # settings - аСЕМАНЫН УКАСИ   Settings - аСЕМА
    return render(request, "base/contact.html", locals())

def about(request):
    settings = models.Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    team = models.Team.objects.all()
    blog = Blog.objects.order_by('?')[:3]
    return render(request, "base/about.html", locals())

def gallery(request):
    settings = models.Settings.objects.latest('id')
    gallery = models.Gallery.objects.all()
    # settings - аСЕМАНЫН УКАСИ   Settings - аСЕМА
    return render(request, "secondary/gallery.html", locals())

def course(request):
    course = Course.objects.all()
    settings = models.Settings.objects.latest('id')
    return render(request, "base/course.html", locals())