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
        return str(self.image)



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



class Order(models.Model):
    ORDER_CHOICES = (('ACCEPTED','ACCEPTED'),('ORDER PROCESSING','ORDER PROCESSING'),('SHIPMENT PENDING','SHIPMENT PENDING'),('ESTIMATED DELIVERY','ESTIMATED DELIVERY'))
    track_number = models.CharField(max_length=128)
    customer_name = models.CharField(max_length=128)
    email = models.EmailField('customer email',blank=True, null=True)
    phone = models.CharField(max_length=128)
    from_address = models.TextField()
    to_address = models.TextField()
    status = models.CharField(max_length=128,default=True,choices=ORDER_CHOICES)


    def get_order_update(self):
        if OrderUpdate.objects.filter(order=self).exists():
            return OrderUpdate.objects.filter(order=self)
        else:
            return None

            
    def str(self):
        return str(self.track_number)
   


class Icon(models.Model):
    title=models.CharField(max_length=128)
    icon=VersatileImageField('Image',upload_to='icon/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return str(self.title)
        


class OrderUpdate(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    location = models.CharField(max_length=128) 
    comments = models.CharField(max_length=128)
    timestamp = models.DateTimeField()
    order_icon = models.ForeignKey(Icon,on_delete = models.CASCADE,blank=True,null=True)

    def str(self):
        return str(self.order)