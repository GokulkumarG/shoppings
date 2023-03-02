from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('admin',views.admin,name='admin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('form',views.form,name='form'),
    path('promo',views.promo,name='promo'),
    path('re_request',views.re_request,name='re_request'),
    path('login_form',views.login_form,name='login_form'),
    path('promo_filter',views.promo_filter,name='promo_filter'),
    path('delete_customer/<int:customer_id>',views.delete_customer,name="delete_customer"),
    path('offer_checking',views.offer_checking,name='offer_checking'),
]
