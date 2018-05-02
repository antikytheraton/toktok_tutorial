from django.db import models


class Restaurant(models.Model):
    manager = models.CharField(max_length=50)
    manager_phone = models.CharField(max_length=12, unique=True)
    manager_email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=120)
    phone = models.CharField(max_length=12, unique=True)
    picture = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    picture = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    name = models.CharField(max_length=20)
    picture = models.URLField()

    def __str__(self):
        return self.name

class Details(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    size = models.CharField(max_length=20)
    cost = models.CharField(max_length=30)

    def __str__(self):
        return self.product
    