from django.db import models
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField



class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = image = VersatileImageField("Image", upload_to="Banner/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Banner"

    def __str__(self):
        return str(self.title)



class Gallery(models.Model):
    image=VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return str(self.title)



class Update(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=500)
    date=models.DateField()
    image=VersatileImageField('Image',upload_to='updates/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    content=HTMLField(blank=True, null=True)
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Updates"

    def __str__(self):
        return str(self.title)



class Clients(models.Model):
    image=VersatileImageField('Image',upload_to='clients/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return str(self.image)