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



class Testimonial(models.Model):
    name=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)
    image=VersatileImageField('Image',upload_to='testimonials/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    decription=models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)



class CargoRequest(models.Model):
    SERVICE_CHOICES = (
        ("Air cargo", "Air cargo"),
        ("Sea cargo", "Sea cargo"),
        ("Port to port service", "Port to port service"),
        ("Moving service", "Moving service"),
        ("Express delivery", "Express delivery"),
    )
    FROM_COUNTRY_CHOICES = (
        ("United States","United States"),
        ("United Kingdom","United Kingdom"),
        ("Afghanistan","Afghanistan"),
        ("Albania","Albania"),
        ("Algeria","Algeria"),
        ("American Samoa","American Samoa"),
        ("Andorra","Andorra"),
        ("Angola","Angola"),
        ("Anguilla","Anguilla"),
        ("Antarctica","Antarctica"),
        ("Antigua and Barbuda","Antigua and Barbuda"),
        ("Argentina","Argentina"),
        ("Armenia","Armenia"),
        ("Aruba","Aruba"),
        ("Australia","Australia"),
        ("Austria","Austria"),
        ("Azerbaijan","Azerbaijan"),
        ("Bahamas","Bahamas"),
        ("Bahrain","Bahrain"),
        ("Bangladesh","Bangladesh"),
        ("Barbados","Barbados"),
        ("Belarus","Belarus"),
        ("Belgium","Belgium"),
        ("Belize","Belize"),
        ("Benin","Benin"),
        ("Bermuda","Bermuda"),
        ("Bhutan","Bhutan"),
        ("Bolivia","Bolivia"),
        )
    TO_COUNTRY_CHOICES = (
        ("Iceland","Iceland"),
        ("India","India"),
        ("Indonesia","Indonesia"),
        ("Iran, Islamic Republic of","Iran, Islamic Republic of"),
        ("Iraq","Iraq"),
        ("Ireland","Ireland"),
        ("Israel","Israel"),
        ("Italy","Italy"),
        ("Jamaica","Jamaica"),
        ("Japan","Japan"),
        ("Jordan","Jordan"),
        ("Kazakhstan","Kazakhstan"),
        ("Kenya","Kenya"),
        ("Kiribati","Kiribati"),
        ("Korea, Republic of","Korea, Republic of"),
        ("Kuwait","Kuwait"),
        ("Kyrgyzstan","Kyrgyzstan"),
        ("Latvia","Latvia"),
        ("Lebanon","Lebanon"),
        ("Lesotho","Lesotho"),
        ("Liberia","Liberia"),
    )
    WEIGHT_CHOICES = (
        ("100Kg","100Kg"),
        ("200Kg","200Kg"),
        ("300Kg","300Kg"),
        ("400Kg","400Kg"),
        ("500Kg","500Kg"),
        ("600Kg","600Kg"),
        ("700Kg","700Kg"),
    )
    services = models.CharField(max_length=100,choices=SERVICE_CHOICES)
    length = models.CharField(max_length=25)
    width = models.CharField(max_length=25)
    from_country = models.CharField(max_length=100,choices=FROM_COUNTRY_CHOICES)
    to_country = models.CharField(max_length=100,choices=TO_COUNTRY_CHOICES)
    weight = models.CharField(max_length=100,choices=WEIGHT_CHOICES)
    phone = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Cargo Request"

    def __str__(self):
        return str(self.services)


class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.name  