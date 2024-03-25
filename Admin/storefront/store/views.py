from django.shortcuts import render
from store.models import Customer, Product, Promotion, Order, Promotion
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Sum, Count, Avg, Max, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
# Create your views here.


def home(request):
    customer = Customer.object.all()
    dict = {'table': customer}
    return render(request, 'index.html', dict)
