from contextlib import redirect_stderr
from email import message
from ipaddress import ip_address
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
import requests
import json  
# Create your views here.
CODE_EVALUATION_URL = u'https://api.hackerearth.com/v4/partner/code-evaluation/submissions/'
CLIENT_SECRET = '88836b92d51b182929912d4f63b015a4f5928d2a'
def index(request):
    if request.method == "POST":
            user_code = request.POST["comment"]
            callback = "http://127.0.0.1:8000/myapp/"
            data = {
                'source':user_code,
                'lang':"PYTHON3",
                'time_limit': 5,
                'memory_limit': 246323,
                'input':"",
                #'callback' : callback,
                'id': "client-001"
            }
            headers = {"client-secret":CLIENT_SECRET}
            resp1 = requests.post(CODE_EVALUATION_URL, json=data, headers=headers)
            di1 = json.loads(resp1.text)
            GET_STATUS_URL = di1['status_update_url']
            resp2= requests.get(GET_STATUS_URL, headers=headers)
            di2 = json.loads(resp2.text)
            response = requests.get(di2['result']['run_status']['output'])
            text = response.text
            return render(request, 'myapp/home.html',{
                'message':text
            } )

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_auth:login'))
    return render(request, 'myapp/home.html')
    
def profile_view(request):
    pass

def home_view(request):
    pass

def quiz_view(request):
    pass

def contest_view(request):
    pass

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_auth:login'))
