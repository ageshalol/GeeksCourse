from django.shortcuts import render
from .models import Settings,Slide,About,Team,Teachers,Review
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    about = About.objects.latest('id')
    teachers = Teachers.objects.all()
    review = Review.objects.all()
    if request.method =="POST":
        username = request.POST.get('username')
        work = request.POST.get('work')
        message = request.POST.get('message')
        reserv = Review.objects.create(username = username,work = work,message=message)
    return render(request, "base/index-3.html", locals())

def contact(request):
    settings = Settings.objects.latest('id')  # settings - аСЕМАНЫН УКАСИ   Settings - аСЕМА
    return render(request, "contact.html", locals())

def about(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    team = Team.objects.all()
    return render(request, "base/about.html", locals())


    
def course(request):
    settings = Settings.objects.latest('id')
    return render(request, "base/course.html", locals())