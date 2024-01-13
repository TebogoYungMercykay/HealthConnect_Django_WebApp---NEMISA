from django.shortcuts import redirect
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


def get_disease(request, user_id):
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            param_id = user_id
            user_id = request.session.get('user_id')
            
            if user_id != None and param_id == user_id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/disease_prediction/{user_id}'

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
                
                logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def check_disease(request, user_id, disease_id):
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            param_id = user_id
            user_id = request.session.get('user_id')
            
            if user_id != None and param_id == user_id:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/disease_prediction/check_disease/{user_id}/{disease_id}'

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
                
                logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def create_disease(request, user_id):
    
    if request.method == 'POST':
        
        if request.POST['no_of_symptoms'] and request.POST['symptoms']:
        
            try:
                user_id = request.session.get('user_id')
                
                if user_id != None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + f'/disease_prediction/create_disease/{user_id}'

                    post_data = {
                        "no_of_symptoms": request.POST['no_of_symptoms'],
                        "symptoms": request.POST['symptoms']
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

                            messages.info(request, "Successfully Created a Disease Prediction")
                            return api_response.get('data')
                    
                    logging.error(f"Error Occured When Creating Disease Prediction: {e}: User ID: {user_id}")
                    return None
                
                else:
                    raise PermissionDenied(USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Disease Prediction: {e}: User ID: {user_id}")
                return None

        else:
            messages.error(request, MESSAGE)
            return redirect(reverse(POSTS_TEMPLATE))

    else:
        messages.error(request, METHOD_ERROR)
        return None

