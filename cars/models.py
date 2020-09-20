from django.db import models
import datetime
from dealers.models import Dealer
from django.urls import reverse

# Create your models here. Example -> Condition: Used Year:2014 Make:Nissan Model:Versa Trim:SL Colour:Black
# BodyType: Sedan Drivetrain:Front-wheel drive (FWD) Transmission: Automatic Fuel Type: Gasoline Kilometers: 134,500
class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=100)
    CATEGORY = (
            ('New','New'),
            ('Used','Used')
        )
    category = models.CharField(max_length=50, choices=CATEGORY)
    image_main = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)
    image6 = models.ImageField(upload_to='images', blank=True)
    image7 = models.ImageField(upload_to='images', blank=True)
    image8 = models.ImageField(upload_to='images', blank=True)
    image9 = models.ImageField(upload_to='images', blank=True)
    image10 = models.ImageField(upload_to='images', blank=True)
    image11 = models.ImageField(upload_to='images', blank=True)
    image12 = models.ImageField(upload_to='images', blank=True)
    image13 = models.ImageField(upload_to='images', blank=True)
    image14 = models.ImageField(upload_to='images', blank=True)
    image15 = models.ImageField(upload_to='images', blank=True)

    kilometers = models.IntegerField(blank=True, null=True)
    TRANSMISSION = (
                ('Manual','Manual'),
                ('Automatic','Automatic')
    )
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    trim = models.CharField(max_length=50)
    fueltype = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    drivetrain = models.CharField(max_length=50)
    bodytype = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)

    YEAR_CHOICES = [(r,r) for r in range(1960, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    price = models.IntegerField()
    description = models.TextField()
    listheader1 = models.TextField()
    listcontents1= models.TextField()
    listheader2 = models.TextField()
    listcontents2= models.TextField()
    listheader3 = models.TextField()
    listcontents3= models.TextField()
    listheader4 = models.TextField()
    listcontents4= models.TextField()
    listheader5 = models.TextField()
    listcontents5 = models.TextField()
    listheader6 = models.TextField()
    listcontents6 = models.TextField()
    listheader7 = models.TextField()
    listcontents7 = models.TextField()
    listheader8 = models.TextField()
    listcontents8 = models.TextField()
    listheader9 = models.TextField()
    listcontents9 = models.TextField()

    date = models.DateField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs = {
                        'car_id':self.id
        })
