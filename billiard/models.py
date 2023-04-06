from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Listing(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=50, default='Pool Tournament')
    director = models.CharField(max_length=100, default='name')
    phone_number = PhoneNumberField(blank=True,region="US")
    email = models.EmailField(max_length=50)
    venue = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, default = None)
    sign_up_time = models.CharField(max_length=10)
    start_time = models.CharField(max_length =10)
    description = models.TextField(max_length = 1000)

    def __str__(self):
        return self.venue

class FeaturedPlayer(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    birth_date = models.DateField()    
    country = models.CharField(max_length=30)
    fargo = models.IntegerField()
    current_year_earnings = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

class News(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    date = models.DateField()
    article_md = models.TextField(max_length=4096,blank=True, default = None)
    description = models.TextField(max_length=512)
    featured = models.IntegerField(blank=True, default = None)
    featured_image = models.CharField(max_length=255, blank=True, default = None)

    def __str__(self):
        return self.title

class Post(models.Model):
    uuid =   models.UUIDField(primary_key=True,unique=True,auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default=None)
    body = models.TextField(max_length=6000)

    def __str__(self):
        return self.title + '|' + self.author

        
    
    

