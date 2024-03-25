from django.shortcuts import render
from store.models import Customer, Product
from django.db.models import Q, F

# def home(request):
#     showdata = Customer.objects.all()
#     dict = {'data': showdata}
#     return render(request, 'index.html', dict)


def home(request):
    product = Product.objects.all()
    # product = Product.objects.filter(Q(inventory__lt=10)&Q(price__lt=20))
    # product = Product.objects.filter(inventory=F('price'))
    # product = Product.objects.order_by('price')
    # product = Product.objects.order_by('-price')
    # product = Product.objects.order_by('price')
    # product = Product.objects.filter(collection_id=9).order_by('price')
    dict = {'table': product}
    return render(request, 'index.html', dict)
