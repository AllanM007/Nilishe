from django.contrib import admin
from .models import MpesaCallBacks, MpesaCalls, MpesaPayment

admin.site.register(MpesaCallBacks)
admin.site.register(MpesaCalls)
admin.site.register(MpesaPayment)
