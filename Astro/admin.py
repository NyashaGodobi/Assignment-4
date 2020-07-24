from django.contrib import admin
from .models import Prescription, Enquiry, Order

admin.site.register(Prescription)
admin.site.register(Enquiry)
admin.site.register(Order)
# Register your models here.
