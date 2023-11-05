from django.db import models

# Create your models here.
class Customers(models.Model):
    name=models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15, null=True, blank=True, db_index=True)
    email = models.EmailField(max_length=254, null=True, blank=True, db_index=True)
    address=models.TextField()

    def __str__(self):
        return self.name
  

class Brands(models.Model):
    brand=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.brand

class Product(models.Model):
    p_id = models.CharField(max_length=10, unique=True, db_index=True)  # Index on p_id for faster lookups
    name = models.CharField(max_length=100)
    brand=models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    p_image = models.ImageField(upload_to="ProductImages/", null=True, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Index on name for faster lookups
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    invoice_number=models.CharField(max_length=10)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['customer']),
            models.Index(fields=['date']),
        ]


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['sale']),
            models.Index(fields=['product']),
        ]


class Purchase(models.Model):
    purchase_invoice_number=models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill=models.FileField( upload_to="Purchase Bills", max_length=100,null=True,blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['supplier']),
            models.Index(fields=['date']),
        ]


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=0)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    amount=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    class Meta:
        indexes = [
            models.Index(fields=['purchase']),
            models.Index(fields=['product']),
        ]


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        indexes = [
            models.Index(fields=['product']), 
        ]


class Role(models.Model):
    name = models.CharField(max_length=100)
