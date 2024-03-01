from django.db import models
from apps.product.models import Product
from apps.professional.models import Professional
from apps.customer.models import Customer

class Sale(models.Model):
    products = models.ManyToManyField(Product)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="profess_sale")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cust_sale")
    payment_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    alternative_price = models.DecimalField(max_digits=10, decimal_places=2)

class ClientSale(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sale_clisal")
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="clisal_sale")

class ProductSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sale_prodsal")
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="prodsal_sale")