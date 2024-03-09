from django.db import models
from apps.service.models import Service
from apps.professional.models import Professional
from apps.customer.models import Customer

class Sale(models.Model):
    services = models.ManyToManyField(Service)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="profess_sale")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cust_sale")
    payment_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    alternative_price = models.DecimalField(max_digits=10, decimal_places=2)

class ClientSale(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sale_clisal")
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="clisal_sale")

class ServiceSale(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="sale_servsal")
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="servsal_sale")