from django.db import models
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField
# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = image = VersatileImageField("Image", upload_to="Banner/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Banner"

    def __str__(self):
        return str(self.title)

class Service(models.Model):
    title = models.CharField(max_length=100)