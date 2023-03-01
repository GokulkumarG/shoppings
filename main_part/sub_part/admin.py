from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(member)
admin.site.register(admin_data)
admin.site.register(purchased_customer)

