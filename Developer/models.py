from django.db import models

# Create your models here.
class Customers(models.Model):
    name=models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15, null=True, blank=True, db_index=True)
    email = models.EmailField(max_length=254, null=True, blank=True, db_index=True)
    address=models.TextField()

    def __str__(self):
        return self.name
 
