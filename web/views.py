from django.shortcuts import render
from .models import Gallery



def index(request):
    context = {"is_index":True}
    return render(request,'web/index.html',context)


def about(request):
    context = {"is_about":True}
    return render(request,'web/about.html',context)


def services(request):
    context = {"is_service":True}
    return render(request,'web/service.html',context)


def gallery(request):
    gallery=Gallery.objects.all()
    context = {"is_gallery":True,"gallery":gallery}
    return render(request,'web/gallery.html',context)


def updates(request):
    context = {"is_updates":True}
    return render(request, 'web/blog.html',context)


def updates_details(request):
    context = {}
    return render(request, 'web/blog-details.html',context)


def contact(request):
    context = {"is_contact":True}
    return render(request, 'web/contact.html',context)