from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lat_long = models.CharField(max_length=255)
    full_details = models.JSONField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"
