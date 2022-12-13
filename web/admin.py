from django.contrib import admin
from .models import Banner
from .models import Gallery
from .models import Update
from .models import Clients
from .models import Icon
from .models import Order
from .models import OrderUpdate
from .models import Testimonial
from .models import CargoRequest

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ( 'title',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'id','image',)
    

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'summary',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ( 'id','image',)


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ( 'title',)



class OrderUpdateInline(admin.TabularInline):
    model = OrderUpdate


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'track_number',)
    inlines = [ OrderUpdateInline]


@admin.register(OrderUpdate)
class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ( 'order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ( 'name','designation',)


@admin.register(CargoRequest)
class CargoRequestAdmin(admin.ModelAdmin):
    list_display = ( 'services','length','width','from_country','to_country','weight','phone',)