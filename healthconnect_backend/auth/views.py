from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .form import LoginForm
from django.contrib import messages
import requests, logging, json, os

from django.http import JsonResponse

MESSAGE = "Some Error Occured, Please Try Again."
FORM_DATA = 'application/x-www-form-urlencoded'
JSON_DATA = 'application/json'


def login_patient(request):
    
    messages.clear()
    if request.method == 'POST':
        
        try:
            temp_form = LoginForm(request.POST)

            if temp_form.is_valid():
                form_data = {
                    'username': temp_form.cleaned_data['username'],
                    'password': temp_form.cleaned_data['password'],
                }

                api_url = os.getenv("API_ENDPOINT") + '/auth/login?type=patient'
                
                headers = {
                    'Content-Type': FORM_DATA,
                }
                
                response = requests.post(api_url, data=form_data, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        request.session.clear()
                        request.session['user_id'] = api_response.get('id')
                        request.session['access_token'] = api_response['data']['access_token']
                        request.session['token_type'] = api_response['data']['token_type']
                        request.session['name'] = api_response.get('name')
                        request.session['is_authenticated'] = True
                        request.session['is_patient'] = True
                        request.session['is_doctor'] = False
                        request.session['is_admin'] = False
                        request.session['chatbot_id'] = os.getenv("CHATBOT_ID")
                        request.session['prediction_successful'] = False

                        return render(request, 'pages-login.html')
                        
                    else:
                        messages.info(request, api_response.get('data'))
                        return render(request, 'pages-login.html')
                        
            messages.info(request, MESSAGE)
            return render(request, 'pages-login.html')

        except requests.RequestException as e:
            temp_message = ""
            try:
                api_response = response.json()
                temp_message = api_response.get('data')
            except Exception as e:
                temp_message = "Error Occured During Login Request"
                
            messages.error(request, temp_message)
            return render(request, 'pages-login.html')
        
    else:
        return render(request,'index.html')


def login_doctor(request):
    
    messages.clear()
    if request.method == 'POST':
        
        try:
            temp_form = LoginForm(request.POST)
            
            if temp_form.is_valid():
                form_data = {
                    'username': temp_form.cleaned_data['username'],
                    'password': temp_form.cleaned_data['password'],
                }

                api_url = os.getenv("API_ENDPOINT") + '/auth/login?type=doctor'
                
                headers = {
                    'Content-Type': FORM_DATA,
                }
                
                response = requests.post(api_url, data=form_data, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        request.session.clear()
                        request.session['user_id'] = api_response.get('id')
                        request.session['access_token'] = api_response['data']['access_token']
                        request.session['token_type'] = api_response['data']['token_type']
                        request.session['name'] = api_response.get('name')
                        request.session['is_authenticated'] = True
                        request.session['is_patient'] = False
                        request.session['is_doctor'] = True
                        request.session['is_admin'] = False
                        request.session['chatbot_id'] = os.getenv("CHATBOT_ID")
                        request.session['prediction_successful'] = False
                        
                        return render(request, 'pages-login.html')
        
                    else:
                        messages.info(request, api_response.get('data'))
                        return render(request, 'pages-login.html')
                        
            messages.info(request, MESSAGE)
            return render(request, 'pages-login.html')

        except requests.RequestException as e:
            temp_message = ""
            try:
                api_response = response.json()
                temp_message = api_response.get('data')
            except Exception as e:
                temp_message = "Error Occured During Login Request"
                
            messages.error(request, temp_message)
            return render(request, 'pages-login.html')

    else:
        return render(request,'pages-login.html')


def login_admin(request):
    
    messages.clear()
    if request.method == 'POST':
        
        try:
            temp_form = LoginForm(request.POST)
            
            if temp_form.is_valid():
                request_data = {
                    'username': temp_form.cleaned_data['username'],
                    'password': temp_form.cleaned_data['password'],
                }

                api_url = os.getenv("API_ENDPOINT") + '/auth/login?type=admin'
                
                headers = {
                    'Content-Type': FORM_DATA,
                }
                
                response = requests.post(api_url, data=request_data, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        request.session.clear()
                        request.session['user_id'] = api_response.get('id')
                        request.session['access_token'] = api_response['data']['access_token']
                        request.session['token_type'] = api_response['data']['token_type']
                        request.session['name'] = api_response.get('name')
                        request.session['is_authenticated'] = True
                        request.session['is_patient'] = False
                        request.session['is_doctor'] = False
                        request.session['is_admin'] = True
                        request.session['chatbot_id'] = os.getenv("CHATBOT_ID")
                        request.session['prediction_successful'] = False
                        
                        return render(request, 'pages-login.html')
        
                    else:
                        messages.info(request, api_response.get('data'))
                        return render(request, 'pages-login.html')
                        
            messages.info(request, MESSAGE)
            return render(request, 'pages-login.html')
        
        except requests.RequestException as e:
            temp_message = ""
            try:
                api_response = response.json()
                temp_message = api_response.get('data')
            except Exception as e:
                temp_message = "Error Occured During Login Request"
                
            messages.error(request, temp_message)
            return render(request, 'pages-login.html')

    else:
        return render(request,'pages-login.html')


def logout(request):
    
    messages.clear()
    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id', None)
            jwt_token = request.session.get('access_token', None)
            token_type = request.session.get('token_type', None)

            headers = {
                "Content-Type": JSON_DATA,
                "Authorization": f"{token_type} {jwt_token}",
            }
            
            api_url = os.getenv("API_ENDPOINT") + f'/auth/logout/{user_id}'
            
            response = requests.post(api_url, headers=headers)
            response.raise_for_status()
            
            if response.status_code == 200:
                api_response = response.json()
                
                if api_response.get('status') == "success":
                    request.session.pop('user_id', None)
                    request.session.pop('access_token', None)
                    request.session.pop('token_type', None)
                    request.session.pop('name', None)
                    request.session.pop('is_authenticated', None)
                    request.session.pop('is_patient', None)
                    request.session.pop('is_doctor', None)
                    request.session.pop('is_admin', None)
                    request.session.pop('chatbot_id', None)
                    request.session.pop('prediction_successful', None)

                    return redirect(reverse('home'))
            
            request.session.clear()
            return redirect(reverse('home'))
            
        except requests.RequestException as e:
            temp_message = ""
            try:
                api_response = response.json()
                temp_message = api_response.get('data')
            except Exception as e:
                temp_message = f"Error Occured During Logout Request: User Id: {user_id}"
                
            messages.error(request, temp_message)
            request.session.clear()
            return redirect(reverse('home'))

    else:
        request.session.clear()
        return redirect(reverse('home'))
    
