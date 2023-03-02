from django.db import models

# Create your models here.
class member(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=15)
    password=models.CharField(max_length=100)
    promo_code=models.CharField(max_length=10)
    
class admin_data(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
class purchased_customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=15)
    password=models.CharField(max_length=100)
    promo_code=models.CharField(max_length=10)
    purchased_time=models.DateTimeField(auto_now_add=True)