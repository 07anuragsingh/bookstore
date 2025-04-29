from django.db import models

# Create your models here.


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=100)
    date_of_joining  = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=3000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

