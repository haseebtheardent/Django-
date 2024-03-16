from django.shortcuts import render
from store.models import Customer

def home(request):
    showdata=Customer.objects.all()
    dict={'table':showdata}
    return render(request, 'index.html',dict)

