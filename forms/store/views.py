from django.shortcuts import render
from store.models import Customer, Product, Promotion, Order, Promotion
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Sum, Count, Avg, Max, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from .forms import Contact
from .models import ContactTable
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_no']
            table = ContactTable(
                first_name=fname, last_name=lname, email=email, phone=phone)
            table.save()
            messages.add_message(request,messages.SUCCESS,"Your Data has been submitted Successfully!")
    else:
        form = Contact()
    return render(request, 'index.html', context={'form': form})
