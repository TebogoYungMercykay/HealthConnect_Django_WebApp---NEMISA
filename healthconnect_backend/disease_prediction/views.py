from ..consultations.views import get_consultation_history, get_doctors_data
from django.shortcuts import render
from django.contrib import messages
import requests, logging, json, os

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
CONSULTATION_TEMPLATE = 'consultation.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."


def get_disease(request, user_id):
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            param_id = user_id
            user_id = request.session.get('user_id')
            
            if user_id is not None and param_id == user_id:
                
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
                
                logging.error(f"Error Occured When Requesting Diseases Data: User Id: {user_id}")
                return None
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def check_disease(request, user_id, disease_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            param_id = user_id
            user_id = request.session.get('user_id')
            
            if user_id is not None and param_id == user_id:
                
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
                
                logging.error(f"Error Occured When Requesting Diseases Data, User Id: {user_id}")
                return None
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def create_disease(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if request.POST['no_of_symptoms'] and request.POST['symptoms']:
            
            try:
                user_id = request.session.get('user_id')
                if user_id is not None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')
                    is_patient = request.session.get('is_patient')

                    api_url = os.getenv("API_ENDPOINT") + f'/disease_prediction/create_disease/{user_id}'

                    post_data = {
                        "no_of_symptoms": request.POST['no_of_symptoms'],
                        "symptoms": json.loads(request.POST['symptoms'])
                    }
                    post_data = json.dumps(post_data, indent=4, ensure_ascii=False)

                    headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }
                    
                    response = requests.post(api_url, data=post_data, headers=headers)
                    response.raise_for_status()
                    
                    if response.status_code == 200:
                        api_response = response.json()
                        if api_response.get('status') == "success":

                            messages.info(request, "Successfully Created a Disease Prediction")
                            disease_data = api_response.get('data')
                            consultation_history = get_consultation_history(request, user_id, jwt_token, token_type, is_patient)
                            doctors_data = get_doctors_data(request, user_id, jwt_token, token_type)
                            
                            request.session['prediction_successful'] = True
                            
                            return render(request, CONSULTATION_TEMPLATE, { 'consultation_history': consultation_history, 'doctors_info': doctors_data, 'predicted_disesse': disease_data })
                    
                    logging.error(f"Error Occured When Creating Disease Prediction, User ID: {user_id}")
                
                else:
                    messages.error(request, USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Disease Prediction: {e}, User ID: {user_id}")

        else:
            messages.error(request, MESSAGE)

    else:
        messages.error(request, METHOD_ERROR)
    
    return render(request, CONSULTATION_TEMPLATE, { 'consultation_history': None, 'doctors_info': None, 'predicted_disesse': None })

