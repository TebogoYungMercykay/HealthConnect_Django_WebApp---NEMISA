from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
import requests
import logging
import os

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
POSTS_TEMPLATE = 'blog/posts.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."


def all_consultations(request, id):

    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None and user_id == id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/all_consultations/{user_id}'
                
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
                
                logging.error(f"Error Occured When Requesting Consultations: {e}, User Id: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Consultations: {e}, User Id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def make_consultation(request):

    if request.method == 'POST':
        
        if not (request.POST['doctor_id'] and request.POST['diseaseinfo_id'] and request.POST['consultation_date'] and request.POST['status']):
            
            messages.error(request, METHOD_ERROR)
            return None
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/consultations/make_consultation'

                post_data = {
                    "doctor_id": request.POST['doctor_id'],
                    "diseaseinfo_id": request.POST['diseaseinfo_id'],
                    "consultation_date": request.POST['consultation_date'],
                    "status": request.POST['status']
                }
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, data=post_data, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        title = request.session.get('token_type')[:2]
                        if title == 'dr':
                            return redirect('consultation_view_patient', api_response['data']['id'])
                        else:
                            return redirect('consultation_view_doctor', api_response['data']['id'])
                
                logging.error(f"Error Occured When Requesting Consultations: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Consultations: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))


def consultation_view_patient(request, consultation_id):

    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None and user_id == id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/consultation_view_patient/{consultation_id}'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        return render(request, 'consultation/consultation.html', {"consultation": api_response})
                
                logging.error(f"Error Occured When Consultation View: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Consultation View: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))
     

def consultation_view_doctor(request, consultation_id):

    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None and user_id == id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/consultation_view_doctor/{consultation_id}'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        render(request, 'consultation/consultation.html', {"consultation": api_response.get('data')})
                
                logging.error(f"Error Occured When Consultation View: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Consultation View: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))


def consultation_history_patient(request):

    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None and user_id == id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/consultations/consultation_history_patient'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        return render(request, 'patient/consultation_history/consultation_history.html', {"consultation": api_response.get('data')})
                
                logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))


def consultation_history_doctor(request):

    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None and user_id == id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/consultations/consultation_history_doctor'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        return render(request, 'doctor/consultation_history/consultation_history.html', {"consultation": api_response.get('data')})
                
                logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))


def close_consultation(request, consultation_id):
    
    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None and user_id == id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/close_consultation/{consultation_id}'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        return redirect(reverse('home'))
                
                logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))


def create_review(request, doctor_id):
    
    if request.method == 'POST':
        
        if not (request.POST['rating'] and request.POST['review'] and request.POST['doctor_id']):
            
            messages.error(request, METHOD_ERROR)
            return None
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/create_review/{doctor_id}'

                post_data = {
                    "rating": request.POST['rating'],
                    "review": request.POST['review'],
                    "doctor_id": request.POST['doctor_id']
                }
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, data=post_data, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        title = request.session.get('token_type')[:2]
                        if title == 'dr':
                            return redirect('consultation_view_patient', api_response['data']['id'])
                        else:
                            return redirect('consultation_view_doctor', api_response['data']['id'])
                
                logging.error(f"Error Occured When Creating Reviews: {e}, User Id: {user_id}")
                return redirect(reverse('home'))
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Creating Reviews: {e}, User Id: {user_id}")
            return redirect(reverse('home'))

    else:
        messages.error(request, METHOD_ERROR)
        return redirect(reverse('home'))


def get_reviews_id(request, doctor_id):
    
    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/get_reviews/{doctor_id}'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        return api_response['data']
                
                logging.error(f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")
                return JsonResponse({"average_rating": 0, "Ratings": []})
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")
            return JsonResponse({"average_rating": 0, "Ratings": []})

    else:
        messages.error(request, METHOD_ERROR)
        return JsonResponse({"average_rating": 0, "Ratings": []})


def get_reviews(request):
    
    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/consultations/get_reviews'
                
                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        return api_response['data']
                
                logging.error(f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")
                return JsonResponse({"average_rating": 0, "Ratings": []})
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")
            return JsonResponse({"average_rating": 0, "Ratings": []})

    else:
        messages.error(request, METHOD_ERROR)
        return JsonResponse({"average_rating": 0, "Ratings": []})

