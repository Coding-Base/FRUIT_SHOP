from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
        code = models.CharField(max_length=10)
        description = models.CharField(max_length=255)
        discount = models.FloatField()


class Blog(models.Model):
      post = models.CharField(max_length=1000)
      title= models.CharField(max_length=100)
      date= models.CharField(max_length=40)
      blogger= models.CharField(max_length=40)

      
      


