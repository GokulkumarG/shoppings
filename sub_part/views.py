from django.shortcuts import render
from .models import *

from django.contrib import messages

import string
import random

from django.conf import settings
from django.core.mail import send_mail

import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

#database register code
def re_request(request):
    if request.method == 'POST':
        # ex1=member(first_name=request.POST.get('first_name'),
        #            last_name=request.POST.get('last_name'),
        #            email_id=request.POST.get('email_id'),
        #            phone_number=request.POST.get('phone_number'),
        #            password=request.POST.get('password'))
        if member.objects.filter(email_id=request.POST.get('email_id'),phone_number=request.POST.get('phone_number')):
            print("*****already registered****")
            #error message show in frontend
            messages.error(request,'this emaild & phonenumber has already registered',extra_tags='already')
            return render(request,'register.html')
        elif member.objects.filter(email_id=request.POST.get('email_id')):
            print("*****already registered****")
            #error message show in frontend
            messages.error(request,'this emaild has already registered',extra_tags='already')
            return render(request,'register.html')
        elif member.objects.filter(phone_number=request.POST.get('phone_number')):
            print("*****already registered****")
            #error message show in frontend
            messages.error(request,'this phone_number has already registered',extra_tags='already')
            return render(request,'register.html')
        else:
            #random string****
            res = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase+string.digits, k=7))
 
            # print result
            print("The generated random string : " + str(res))
            promo_code1=str(res)
            #***********************************************8
            print("***data saved successfully****")
            ex1=member(first_name=request.POST.get('first_name'),
                   last_name=request.POST.get('last_name'),
                   email_id=request.POST.get('email_id'),
                   phone_number=request.POST.get('phone_number'),
                   password=request.POST.get('password'),
                   promo_code=promo_code1)
            ex1.save()
           
        #mail send code
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email_id=request.POST.get('email_id')
        
        subject = 'welcome gokulkumar page'
        message = f'Hi {first_name,last_name}, thank you for registering in gokulkumar page \n this is your promocode {promo_code1}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_id, ]
        send_mail( subject, message, email_from, recipient_list )
        print("**mail send successfullly***")

        return render(request,'promo.html',{'promo_code1':promo_code1})
    else:
        print("****data failed*****")
        return render(request,'register.html')

def admin(request):
    return render(request,'admin.html')

def dashboard(request):
    loggin_time=datetime.datetime.now()
    print(f"***login time:{loggin_time}****")
            #view count
    total_registers=member.objects.all().count()
           
    print(f"***total regsitartions {total_registers}****")
            #view all customer data
    customer_details=member.objects.all()
    view_purchasedata=purchased_customer.objects.all()
    purchase_count=purchased_customer.objects.all().count()
    return render(request,'dashboard.html',{'purchase_count':purchase_count,'view_purchasedata':view_purchasedata,
    'loggin_time':loggin_time,'total_registers':total_registers,'customer_details':customer_details})
   
    

def form(request):
    return render(request,'form.html')

def promo(request):
    return render(request,'promo.html')

def login_form(request):
    if request.method == 'POST':
        if admin_data.objects.filter(user_name=request.POST.get('user_name'),password=request.POST.get('password')):
            print("***login successfully")
            logger_data=admin_data.objects.get(user_name=request.POST.get('user_name'),password=request.POST.get('password'))
            loggin_time=datetime.datetime.now()
            total_registers=member.objects.all().count()
            customer_registers=member.objects.all()
            view_purchasedata=purchased_customer.objects.all()
            purchase_count=purchased_customer.objects.all().count()
            return render(request,'dashboard.html',{'view_purchasedata':view_purchasedata,'purchase_count':purchase_count,'logger_data':logger_data,'loggin_time':loggin_time,
                                                    'total_registers':total_registers,'customer_registers':customer_registers})
        else:
            print("**login failed")
            messages.error(request,'check your username or password',extra_tags='failed')
            return render(request,'admin.html')
        
def promo_filter(request):
    if member.objects.filter(Q(promo_code=request.POST.get('common_data'))| Q(phone_number=request.POST.get('common_data'))| Q(email_id=request.POST.get('common_data'))):
        customer_registers= member.objects.filter(Q(promo_code=request.POST.get('common_data'))| Q(phone_number=request.POST.get('common_data'))| Q(email_id=request.POST.get('common_data')))
        loggin_time=datetime.datetime.now()
        total_registers=member.objects.all().count()
        view_purchasedata=purchased_customer.objects.all()
        purchase_count=purchased_customer.objects.all().count()
        return render(request,'dashboard.html',{'purchase_count':purchase_count,'view_purchasedata': view_purchasedata,'customer_registers':customer_registers,'total_registers':total_registers,'loggin_time':loggin_time,'total_registers':total_registers})
    else:
        messages.error(request,'No Such Data',extra_tags='failed')
        loggin_time=datetime.datetime.now()
        total_registers=member.objects.all().count()
        view_purchasedata=purchased_customer.objects.all()
        purchase_count=purchased_customer.objects.all().count()
        return render(request,'dashboard.html',{'view_purchasedata':view_purchasedata,'purchase_count':purchase_count,'total_registers':total_registers,'loggin_time':loggin_time,'total_registers':total_registers})
        
def delete_customer(request,customer_id):
    ex1=member.objects.get(id=customer_id)
    first_name=ex1.first_name
    last_name=ex1.last_name
    email_id=ex1.email_id
    phone_number=ex1.phone_number
    promo_code=ex1.promo_code
    password=ex1.password
    var=purchased_customer(first_name=first_name,last_name=last_name,password=password,email_id=email_id,phone_number=phone_number,promo_code=promo_code)
    var.save()
    print("****data saved in purchase table****")
    ex1.delete()
    messages.error(request,'customer purchased successfully',extra_tags='success')
    loggin_time=datetime.datetime.now()
    total_registers=member.objects.all().count()
    customer_registers=member.objects.all()
    view_purchasedata=purchased_customer.objects.all()
    purchase_count=purchased_customer.objects.all().count()
    return render(request,'dashboard.html',{'customer_registers':customer_registers,'purchase_count':purchase_count,'view_purchasedata':view_purchasedata,'loggin_time':loggin_time,'total_registers':total_registers})
    
    
def offer_checking(request):
    if purchased_customer.objects.filter(phone_number=request.POST.get('c_number')):    
        your_amount=request.POST.get('amount')
        offer_amount=int(your_amount)* 0.2
        print(f"your offer amount {offer_amount}")
        loggin_time=datetime.datetime.now()
        print(f"***login time:{loggin_time}****")
            #view count
        total_registers=member.objects.all().count()
           
        print(f"***total regsitartions {total_registers}****")
            #view all customer data
        customer_details=member.objects.all()
        view_purchasedata=purchased_customer.objects.all()
        purchase_count=purchased_customer.objects.all().count()
        return render(request,'dashboard.html',{'offer_amount':offer_amount,'purchase_count':purchase_count,'view_purchasedata':view_purchasedata,
        'loggin_time':loggin_time,'total_registers':total_registers,'customer_details':customer_details})
    else:
        your_amount=request.POST.get('amount')
        offer_amount=int(your_amount)* 0.5
        print(f"your offer amount {offer_amount}")
        loggin_time=datetime.datetime.now()
        print(f"***login time:{loggin_time}****")
            #view count
        total_registers=member.objects.all().count()
           
        print(f"***total regsitartions {total_registers}****")
            #view all customer data
        customer_details=member.objects.all()
        view_purchasedata=purchased_customer.objects.all()
        purchase_count=purchased_customer.objects.all().count()
        return render(request,'dashboard.html',{'offer_amount':offer_amount,'purchase_count':purchase_count,'view_purchasedata':view_purchasedata,
        'loggin_time':loggin_time,'total_registers':total_registers,'customer_details':customer_details})