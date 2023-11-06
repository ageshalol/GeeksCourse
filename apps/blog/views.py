from django.shortcuts import render
from apps.blog.models import Blog
from apps.nurchik.models import Settings
# Create your views here.
def blog(request):
    settings = Settings.objects.latest('id')
    blog = Blog.objects.all()
    return render(request, "base/blog.html", locals())

def blog_detail(request,id):
    settings = Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    return render(request, "details/blog-details.html", locals())