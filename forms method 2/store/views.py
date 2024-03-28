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
            emaill = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone']
            member = form.cleaned_data['membership']
            db_table = ContactTable(
                first_name=fname, last_name=lname, email=emaill, phone=phone_no, membership=member)
            db_table.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank You, your data has been submitted")

    else:
        form = Contact()
    return render(request, 'index.html', context={'form': form})
