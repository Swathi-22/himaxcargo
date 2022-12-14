from django.shortcuts import render,get_object_or_404
from .models import Gallery
from .models import Banner
from .models import Update
from .models import Clients
from .models import Icon
from .models import Order
from .models import OrderUpdate
from .models import Testimonial
from .forms import CargoRequestForm
from .forms import ContactForm
from django.http import HttpResponse
import json


def index(request):
    banner = Banner.objects.all()
    clients = Clients.objects.all()
    testimonial = Testimonial.objects.all()
    forms = CargoRequestForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {"is_index":True,"banner":banner,"clients":clients,"testimonial":testimonial,"forms":forms}
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
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact": True,
            "forms": forms,

        }
        return render(request, 'web/contact.html', context)


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