from django.shortcuts import render,get_object_or_404
from .models import Gallery
from .models import Banner
from .models import Update
from .models import Clients
from .models import Icon
from .models import Order
from .models import OrderUpdate



def index(request):
    banner = Banner.objects.all()
    clients = Clients.objects.all()
    context = {"is_index":True,"banner":banner,"clients":clients}
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
    updates=Update.objects.all()
    context = {"is_updates":True,"updates":updates}
    return render(request, 'web/blog.html',context)


def updates_details(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.exclude(pk=update.pk)[:3]
    context = {'update':update,'updates':updates}
    return render(request, 'web/blog-details.html',context)


def contact(request):
    context = {"is_contact":True}
    return render(request, 'web/contact.html',context)


def tracking(request):
    if request.method=='GET':
        code =request.GET.get('code',None)
        if Order.objects.filter(track_number=code).exists():
            order=Order.objects.filter(track_number__icontains=code).first()
        else:
            order = None
    context = {
        'order':order
    }
    return render(request,'web/tracking.html',context)



def live_tracking(request,slug):
    order=get_object_or_404(Order,track_number=slug)
    context ={
        'order':order
    }
    return render(request,'web/tracking.html',context)