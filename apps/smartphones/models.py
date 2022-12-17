from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title


class Smartphone(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='smart_images')
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SmartImage(models.Model):
    image = models.ImageField(upload_to='smart_images/carousel')
    smart = models.ForeignKey(Smartphone, on_delete=models.CASCADE, related_name='smart_images')

