from .models import Order
from django.http import JsonResponse


# Create your views here.
def top_customers_view(request):
    """ Method used in Django view"""
    top_customers = Order.top_customers_last_6_months()
    return JsonResponse(list(top_customers), safe=False)