from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from requests.auth import HTTPBasicAuth
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from payments.models import ContractorProfile
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NumberForm
from django.views import View
from django.urls import reverse
import requests
import json

@login_required
def lipa_na_mpesa_online(request, pk):

    contractor = ContractorProfile.objects.get(pk=pk)

    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            form.save()
        
        number = request.POST.get('number')
        pesa = request.POST.get('amount')

        request.session['test'] = str(pesa)

        amount = float(pesa) + float(pesa) * 0.08

        request.session['nambari'] = str(amount)

        print(number, amount)

        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}

        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": number,  # replace with your phone number to get stk push
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": number,  # replace with your phone number to get stk push
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Allan",
            "TransactionDesc": "Testing stk push"
            }

        response = requests.post(api_url, json=request, headers=headers)

        return redirect('mpesa:pc', pk=pk)

    else:

        form = NumberForm()

    return render(request, 'mpesa/checkout.html', {'contractor':contractor})

@login_required
def payment_confirmation(request,pk):
    
    contractor = ContractorProfile.objects.get(pk=pk)

    return render(request, 'mpesa/payment.html', {'contractor':contractor}) 

@login_required
def receipt(request, pk):
    
    contractor = ContractorProfile.objects.get(pk=pk)

    amount = request.session['test']

    total = request.session['nambari']

    context={
        'contractor':contractor,
        'amount':amount,
        'total':total
    }

    print(amount)

    return render(request, 'mpesa/receipt.html', context) 

def getAccessToken(request):
	consumer_key = '9evtZaUeHplbCxTCyghipnFKWZutIUz2'
	consumer_secret = 'MrL3r2UEbF4tnplp'
	api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

	r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
	mpesa_access_token = json.loads(r.text)
	validated_mpesa_access_token = mpesa_access_token['access_token']

	return HttpResponse(validated_mpesa_access_token)

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://b4b8e649.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://b4b8e649.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)

    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)

    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],

    )
    payment.save()

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse(dict(context))