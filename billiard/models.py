from django.db import models
import uuid
from phone_field import PhoneField

class Listing(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=50, default='Pool Tournament')
    director = models.CharField(max_length=100, default='name')
    phone_number = models.PhoneField(blank=True, help_text='Contact phone number', E164_only=False)
    email = models.EmailField(max_length=50)
    venue = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField(max_length=15)
    date = models.DateField()
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
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    date = models.DateField()
    article = models.TextField(max_length=2000)
    description =models.TextField(max_length=200)

    def __str__(self):
        return self.title
