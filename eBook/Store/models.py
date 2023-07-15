from django.db import models

class Ebook(models.Model):
     title = models.CharField(max_length=50)
     price = models.FloatField()
     cvr_url = models.CharField(max_length=2048)

     def __str__(self):
        return self.title


book1 = Ebook()

class CartItems(models.Model):
     title = models.CharField(max_length=50, null=True)
     price = models.FloatField(null=True)

     def __str__(self):
        return self.title
     



# Create your models here.
