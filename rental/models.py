from django.db import models


class Contact(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=13)


class Machine(models.Model):
    machine_id = models.SmallIntegerField(primary_key=True)
    machine_name = models.CharField(max_length=50)
    machine_info = models.TextField(max_length=5000)
    machine_image = models.ImageField(null=True)


class Price(models.Model):
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    price_info = models.CharField(max_length=100, null=True)
