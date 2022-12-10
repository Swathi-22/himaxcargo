from django.contrib import admin
from .models import Banner
from .models import Gallery
from .models import Update
from .models import Clients



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