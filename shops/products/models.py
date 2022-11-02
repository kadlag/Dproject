from django.db import models


class Product(models.Model):
    title = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title