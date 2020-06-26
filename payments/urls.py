from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('lipa/<int:pk>', views.lipa_na_mpesa_online, name='lipa'),
    path('pc/<int:pk>', views.payment_confirmation, name='pc'),
    path('receipt/<int:pk>', views.receipt, name='receipt'),


    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
]