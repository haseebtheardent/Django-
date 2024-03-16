from django.shortcuts import render
from store.models import Customer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def home(request):
    query_set = Customer.objects.all()
    data = None  # Default value
    error_message = None
    try:
        data = Customer.objects.get(pk=0)
    except ObjectDoesNotExist:
        error_message = "Customer with the specified primary key does not exist."

    dict = {'table': query_set, 'data': data, 'error': error_message}

    return render(request, 'index.html', dict)
