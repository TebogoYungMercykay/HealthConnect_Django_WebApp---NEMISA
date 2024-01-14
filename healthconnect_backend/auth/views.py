from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .form import LoginForm
from django.contrib import messages
import requests
import logging
import os

from django.http import JsonResponse

MESSAGE = "Some Error Occured, Please Try Again."
FORM_DATA = 'application/x-www-form-urlencoded'
JSON_DATA = 'application/json'


def login_patient(request):
    
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
                                            
                        request.session['user_id'] = api_response.get('id')
                        request.session['access_token'] = api_response['data']['access_token']
                        request.session['token_type'] = api_response['data']['token_type']
                        request.session['name'] = api_response.get('name')
                        request.session['is_authenticated'] = True
                        
                        # return JsonResponse({"status": "success"}) # Temporary for Testing
                        return redirect(reverse('patient_ui'))
                        
        
                    else:
                        messages.info(request, api_response.get('data'))
                        return redirect(reverse('login_patient'))
                        
            messages.info(request, MESSAGE)
            return redirect(reverse('login_patient'))

        except requests.RequestException as e:
            logging.error(f"Error Occured During Login Request: {e}: Patient")
            return redirect(reverse('home'))
        
    else:
        return render(request,'patient/signin_page/index.html')


def login_doctor(request):
    
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
                                            
                        request.session['user_id'] = api_response.get('id')
                        request.session['access_token'] = api_response['data']['access_token']
                        request.session['token_type'] = api_response['data']['token_type']
                        request.session['name'] = api_response.get('name')
                        request.session['is_authenticated'] = True
                        
                        # return JsonResponse({"status": "success"}) # Temporary for Testing
                        return redirect(reverse('doctor_ui'))
        
                    else:
                        messages.info(request, api_response.get('data'))
                        return redirect(reverse('login_doctor'))
                        
            messages.info(request, MESSAGE)
            return redirect(reverse('login_doctor'))

        except requests.RequestException as e:
            logging.error(f"Error Occured During Login Request: {e}: Doctor")
            return redirect(reverse('home'))

    else:
        return render(request,'doctor/signin_page/index.html')


def login_admin(request):

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
                                            
                        request.session['user_id'] = api_response.get('id')
                        request.session['access_token'] = api_response['data']['access_token']
                        request.session['token_type'] = api_response['data']['token_type']
                        request.session['name'] = api_response.get('name')
                        request.session['is_authenticated'] = True
                        
                        # return JsonResponse({"status": "success"}) # Temporary for Testing
                        return redirect(reverse('admin_ui'))
        
                    else:
                        messages.info(request, api_response.get('data'))
                        return redirect(reverse('login_admin'))
                        
            messages.info(request, MESSAGE)
            return redirect(reverse('login_admin'))
        
        except requests.RequestException as e:
            logging.error(f"Error Occured During Login Request: {e}: Admin")
            return redirect(reverse('home'))

    else:
        return render(request,'admin/signin/signin.html')


def logout(request):

    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            jwt_token = request.session.get('access_token')
            token_type = request.session.get('token_type')

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
                    request.session.pop('is_authenticated', None)
                    request.session.pop('name', None)
            
                    # return JsonResponse({"status": "success"}) # Temporary for Testing
                    return redirect(reverse('home'))
            
            request.session.clear()
            return redirect(reverse('home'))
            
        except requests.RequestException as e:
            logging.error(f"Error Occured During Logout Request: {e}: User Id: {user_id}")
            request.session.clear()
            return redirect(reverse('home'))

    else:
        return redirect(reverse('home'))
    
