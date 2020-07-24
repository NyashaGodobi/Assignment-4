from django.urls import path
from .views import home, products, order, contact, addQuery, addOrder, addPrescription, panel

urlpatterns = [
    path('admin/', panel, name='admin'),
    path('', home, name='home'),
    path('products', products, name='products'),
    path('order', order, name='order'),
    path('contact', contact, name='contact'),
    path('addQuery', addQuery, name='query'),
    path('addOrder', addOrder, name='addOrder'),
    path('addPrescription', addPrescription, name='prescription'),
]

