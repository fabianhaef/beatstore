from django.db import models
from django.contrib.auth.models import User


class LicenceVariation(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_price(self):
        return "{:.2f}".format(self.price / 100)

    class Meta:
        verbose_name_plural = 'Licence Variations'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_soundkit = models.BooleanField(default=False)
    licence_variation = models.ManyToManyField(LicenceVariation)
    _id = models.AutoField(primary_key=True, editable=False)

    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    trackout_files = models.FileField(upload_to='trackouts/')

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    price = models.IntegerField(default=0)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=80, null=True, blank=True)
    taxPrice = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.created_at)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    zip_code = models.CharField(max_length=80, null=True, blank=True)
    zip_code = models.CharField(max_length=80, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.zip_code}, {self.country}"


