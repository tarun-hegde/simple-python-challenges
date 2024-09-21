from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Order(models.Model):
    """assume that this is the model that is given in the django app"""
    customer = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def top_customers_last_6_months(cls):
        """this method is used to retrieve top customers from the last 6 months"""
    
        six_months_ago = timezone.now() - timedelta(days=6*30)
        orders = cls.objects.filter(order_date__gte=six_months_ago)
        top_customers = orders.values('customer').annotate(total_spent=models.Sum('total_amount')).order_by('-total_spent')[:5]
        return top_customers

