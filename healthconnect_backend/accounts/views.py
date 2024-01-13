from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .form import PatientCreateForm, DoctorCreateForm
import requests
import logging
import os

MESSAGE = "Some Error Occured, Please Try Again."
CONSULTATION_TEMPLATE = 'patient/consult_a_doctor/consult_a_doctor.html'
JSON_DATA = 'application/json'


def signup_patient(request):
    if request.method == 'POST':
        try:
            if request.POST['username'] and request.POST['email'] and request.POST['name'] and request.POST['dob'] and request.POST['gender'] and request.POST['address'] and request.POST['mobile'] and request.POST['password'] and request.POST['password1'] :
                
                if request.POST.get('password') == request.POST.get('password1'):
                    
                    temp_form = PatientCreateForm(request.POST)
                    
                    if temp_form.is_valid():
                        request_data = {
                            'email': temp_form.cleaned_data['email'],
                            'password': temp_form.cleaned_data['password'],
                            'name': temp_form.cleaned_data['name'],
                            'surname': temp_form.cleaned_data['surname'],
                            'dob': temp_form.cleaned_data['dob'],
                            'address': temp_form.cleaned_data['address'],
                            'mobile_no': temp_form.cleaned_data['mobile_no'],
                            'gender': temp_form.cleaned_data['gender'],
                        }
                        
                        api_url = os.getenv("API_ENDPOINT") + '/users/signup_patient'
                        
                        headers = {
                            'Content-Type': JSON_DATA,
                        }
                        
                        response = requests.post(api_url, data=request_data, headers=headers)
                        response.raise_for_status()
                        
                        if response.status_code == 200:
                            api_response = response.json()
                            if api_response.get('status') == "success":
                                messages.info(request, "Account created Successfully")
                                return redirect(reverse('login_patient'))
                            
                            else:
                                messages.info(request, api_response.get('data'))
                                return redirect(reverse('signup_patient'))
                    
                    messages.info(request, MESSAGE)
                    return redirect(reverse('signup_patient'))

                else:
                    messages.info(request,'Password not Matching, Please Try Again')
                    return redirect(reverse('signup_patient'))

            else :
                messages.info(request,'Please Make Sure All Required Fields are Filled Out Correctly')
                return redirect(reverse('signup_patient'))
            
        except requests.RequestException as e:
            logging.error(f"Error Occured During Sign Up Request: {e}: Patient")
            return redirect(reverse('signup_patient'))

    else:
        return render(request,'patient/signup_Form/signup.html')


def signup_doctor(request):
    if request.method == 'POST':
        try:
            if request.POST['username'] and request.POST['email'] and request.POST['name'] and request.POST['dob'] and request.POST['gender'] and request.POST['address'] and request.POST['mobile'] and request.POST['password'] and request.POST['password1']  and request.POST['registration_no'] and request.POST['year_of_registration'] and request.POST['qualification'] and request.POST['State_Medical_Council'] and request.POST['specialization']:
                
                if request.POST.get('password') == request.POST.get('password1'):
                    
                    temp_form = DoctorCreateForm(request.POST)
                    
                    if temp_form.is_valid():
                        request_data = {
                            'email': temp_form.cleaned_data['email'],
                            'password': temp_form.cleaned_data['password'],
                            'name': temp_form.cleaned_data['name'],
                            'surname': temp_form.cleaned_data['surname'],
                            'dob': temp_form.cleaned_data['dob'],
                            'address': temp_form.cleaned_data['address'],
                            'mobile_no': temp_form.cleaned_data['mobile_no'],
                            'gender': temp_form.cleaned_data['gender'],
                            'qualification': temp_form.cleaned_data['qualification'],
                            'registration_no': temp_form.cleaned_data['registration_no'],
                            'year_of_registration': temp_form.cleaned_data['year_of_registration'],
                            'state_medical_council': temp_form.cleaned_data['state_medical_council'],
                            'specialization': temp_form.cleaned_data['specialization'],
                        }
                        
                        api_url = os.getenv("API_ENDPOINT") + '/users/signup_doctor'
                        
                        headers = {
                            'Content-Type': JSON_DATA,
                        }
                        
                        response = requests.post(api_url, data=request_data, headers=headers)
                        response.raise_for_status()
                        
                        if response.status_code == 200:
                            api_response = response.json()
                            if api_response.get('status') == "success":
                                messages.info(request, "Account created Successfully")
                                return redirect(reverse('login_patient'))
                            
                            else:
                                messages.info(request, api_response.get('data'))
                                return redirect(reverse('signup_doctor'))
                    
                    messages.info(request, MESSAGE)
                    return redirect(reverse('signup_doctor'))

                else:
                    messages.info(request,'Password not Matching, Please Try Again')
                    return redirect(reverse('signup_doctor'))

            else :
                messages.info(request,'Please Make Sure All Required Fields are Filled Out Correctly')
                return redirect(reverse('signup_doctor'))
            
        except requests.RequestException as e:
            logging.error(f"Error Occured During Sign Up Request: {e}: Doctor")
            return redirect(reverse('signup_patient'))
        
    else:
        return render(request,'doctor/signup_Form/signup.html')


def get_doctors(request):

    if request.method == 'GET':
        try:
            user_id = request.session.get('user_id')
            jwt_token = request.session.get('access_token')
            token_type = request.session.get('token_type')

            api_url = os.getenv("API_ENDPOINT") + '/users/doctors'

            headers = {
                "Content-Type": JSON_DATA,
                "Authorization": f"{token_type} {jwt_token}",
            }

            response = requests.post(api_url, headers=headers)
            response.raise_for_status()

            doctors_obj = None
            
            if response.status_code == 200:
                api_response = response.json()
                if api_response.get('status') == "success":

                    doctors_obj = api_response.get('data')
                    return render(request, CONSULTATION_TEMPLATE, {"dobj": doctors_obj})
            
            logging.error(f"Error Occured When Requesting for Doctors Data: {e}: User_id: {user_id}")
            return render(request, CONSULTATION_TEMPLATE, {"dobj": None})
                    
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting for Doctors Data: {e}: User_id: {user_id}")
            return redirect(reverse('home'))

    else:
        return render(request, CONSULTATION_TEMPLATE, {"dobj": None})
        

def get_user(request, user_id):

    if request.method == 'GET' or request.method == 'POST':
        try:
            param_id = user_id
            user_id = request.session.get('user_id')
            
            if param_id == user_id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/users/{user_id}'

                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        return api_response.get('data')
                
                logging.error(f"Error Occured When Requesting for Doctors Data: {e}: User_id: {user_id}")
                return None
            
            else:
                raise PermissionDenied("Incorrect User Id used.")
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting User Data: {e}: User_id: {user_id}")
            return None

    else:
        return None


def savedata(request, user_id):
    
    if request.method == 'POST':
        try:
            param_id = user_id
            user_id = request.session.get('user_id')
            
            if param_id == user_id:

                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')
                
                api_url = os.getenv("API_ENDPOINT") + f'/users/savedata/{user_id}'
                
                headers = {
                    'Content-Type': JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }
                
                request_data = {
                    "name": request.POST['name'],
                    "surname": request.POST['surname'],
                    "address": request.POST['address'],
                    "mobile_no": request.POST['mobile_no']
                }
                
                response = requests.put(api_url, json=request_data, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    
                    if api_response.get('status') == "success":

                        if api_response.get('name')[:2].lower() == 'dr':
                            return reverse('doctor_profile', args=[user_id])
                        else:
                            return redirect(reverse('patient_profile', args=[user_id]))

                messages.info(request, MESSAGE)
                return redirect(reverse('patient_profile', args=[user_id]))            
            
            else:
                raise PermissionDenied("Incorrect User Id used.")

        except requests.RequestException as e:
            logging.error(f"Error Occured When Updating User Data: {e}: User_id: {user_id}")
            return None
        
    else:
        return redirect(reverse('doctor_profile', args=[user_id]))
    
