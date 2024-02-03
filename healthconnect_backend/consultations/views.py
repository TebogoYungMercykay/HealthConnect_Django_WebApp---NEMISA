from django.http import JsonResponse, HttpResponseRedirect
from ..chats_and_feedback.views import chat_messages
from django.shortcuts import render, redirect
import requests, logging, json, os, random
from django.contrib import messages
from django.urls import reverse
from ..utils import utils

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
CONSULTATION_TEMPLATE = 'consultation.html'
CONSULTATION_CHATS_TEMPLATE = 'consultation-chats.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."


# Helper Functions Starts Here

def get_doctors_data(request, user_id, jwt_token, token_type):
    try:
        api_url = os.getenv("API_ENDPOINT") + '/users/doctors'
        
        headers = {"Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}"}
        
        response = requests.post(api_url, headers=headers)
        response.raise_for_status()
        
        if response.status_code == 200:
            api_response = response.json()
            if api_response.get('status') == "success":
                doctors_data = api_response.get('data')
                for doctor in doctors_data:
                    doctor['activity'] = random.randint(3, 6)
                return doctors_data
            
    except requests.RequestException as e:
        logging.error(f"Error Occurred When Requesting Doctor Data: {e}, User Id: {user_id}")
    
    messages.error(request, MESSAGE)
    return None


def get_consultation_history(request, user_id, jwt_token, token_type, is_patient):
    try:
        api_url = os.getenv("API_ENDPOINT") + '/consultations/consultation_history_doctor'
        if is_patient:
            api_url = os.getenv("API_ENDPOINT") + '/consultations/consultation_history_patient'
        
        headers = {"Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}"}
        
        response = requests.post(api_url, headers=headers)
        response.raise_for_status()
        
        if response.status_code == 200:
            api_response = response.json()
            if api_response.get('status') == "success":
                consultation_history = api_response.get('data')['Consultations']
                for consultation in consultation_history:
                    consultation['consultation_date'] = utils.format_date(consultation['consultation_date'])
                    consultation['diseaseinfo']['confidence'] = round(consultation['diseaseinfo']['confidence'], 2)
                    consultation['list_symptoms'] = ', '.join(map(str, consultation['diseaseinfo']['symptoms']))
                
                return consultation_history
            
    except requests.RequestException as e:
        logging.error(f"Error Occurred When Requesting Consultations: {e}, User Id: {user_id}")
        
    messages.error(request, MESSAGE)
    return None

# Ends Here


def consultation(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST' or request.method == 'GET':
        try:
            user_id = request.session.get('user_id')
            if user_id is not None:
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')
                is_patient = request.session.get('is_patient')
                
                consultation_history = get_consultation_history(request, user_id, jwt_token, token_type, is_patient)
                
                if consultation_history is not None:
                    return render(request, CONSULTATION_TEMPLATE, {"consultation_history": consultation_history})
                
            else:
                messages.error(request, USER_MESSAGE)
        
        except requests.RequestException as e:
            logging.error(f"Error Occurred When Requesting Consultations: {e}, User Id: {user_id}")
    
    else:
        messages.error(request, METHOD_ERROR)
    
    messages.error(request, 'Some error Occurred while requesting Consultations')
    return render(request, CONSULTATION_TEMPLATE, {"consultation_history": None})


def make_consultation(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        print(request.POST)
        if not (request.POST['doctor_id'] and request.POST['diseaseinfo_id'] and request.POST['consultation_date'] and request.POST['status']):
            
            messages.error(request, METHOD_ERROR)
            return redirect(reverse('consultation'))
        
        else:
            try:
                user_id = request.session.get('user_id')
                if user_id is not None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + '/consultations/make_consultation'

                    post_data = {
                        "doctor_id": request.POST['doctor_id'],
                        "diseaseinfo_id": request.POST['diseaseinfo_id'],
                        "consultation_date": request.POST['consultation_date'],
                        "status": request.POST['status']
                    }
                    post_data = json.dumps(post_data, indent=4, ensure_ascii=False)
                    
                    headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }

                    response = requests.post(api_url, data=post_data, headers=headers)
                    response.raise_for_status()
                    
                    if response.status_code == 200:
                        api_response = response.json()
                        if api_response.get('status') == "success":
                            consultation_info = api_response.get('data')
                            
                            consultation_url = reverse('consultation_view', args=[consultation_info['consultation_id']])
                            return HttpResponseRedirect(consultation_url)
                    
                    logging.error(f"Error Occured When Requesting Consultations, User Id: {user_id}")
                
                else:
                    messages.error(request, USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Requesting Consultations: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return redirect(reverse('consultation'))


def consultation_view(request, consultation_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = request.session.get('message_successful')

    if request.method == 'POST' or request.method == 'GET':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None and consultation_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')
            
                headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}",}
                
                api_url = os.getenv("API_ENDPOINT") + f'/consultations/consultation_view_patient/{consultation_id}'
                if request.session.get('is_patient') is False:
                    api_url = os.getenv("API_ENDPOINT") + f'/consultations/consultation_view_doctor/{consultation_id}'
                    
                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        consultation_info = api_response.get('data')

                        if consultation_info is not None:
                            
                            # Formatting Consultation Info
                            consultation_info['consultation_date'] = utils.format_date(consultation_info['consultation_date'])
                            consultation_info['diseaseinfo']['confidence'] = round(consultation_info['diseaseinfo']['confidence'], 2)
                            consultation_info['list_symptoms'] = ', '.join(map(str, consultation_info['diseaseinfo']['symptoms']))
                            consultation_info['doctor']['year_of_registration'] = utils.format_date(consultation_info['doctor']['year_of_registration'])
                            consultation_info['doctor']['rating'] = round(consultation_info['doctor']['rating'], 2)
                            consultation_info['patient']['dob'] = utils.format_date(consultation_info['patient']['dob'])
                            consultation_info['patient']['age'] = utils.calculate_age(consultation_info['patient']['dob'])
                            consultation_info['patient']['age'] = utils.calculate_age(consultation_info['patient']['dob'])
                            consultation_info['days_elapsed_since'] = utils.days_elapsed_since(consultation_info['consultation_date'])

                            # Formatting Chat Messages
                            consultation_chats = chat_messages(request, consultation_id)
                            consultation_chats['length'] = len(consultation_chats['chats'])
                            if consultation_chats is not None:
                                for chat in consultation_chats['chats']:
                                    chat['created_at'] = utils.format_date(chat['created_at'])
                            
                            return render(request, CONSULTATION_CHATS_TEMPLATE, { 'consultation_info': consultation_info, 'consultation_chats': consultation_chats })
                            
                        else:
                            messages.error(request, MESSAGE)

                logging.error(f"Error Occured in Consultation View, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured in Consultation View: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return redirect(reverse('consultation'))
     

def close_consultation(request, consultation_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None and consultation_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/consultations/close_consultation/{consultation_id}'
                
                headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        consultation_url = reverse('consultation_view', args=[consultation_id])
                        return HttpResponseRedirect(consultation_url)
                
                logging.error(f"Error Occured When Consultation History, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Consultation History: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return redirect(reverse('home'))


def create_review(request, doctor_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if not (request.POST['rating'] and request.POST['review'] and request.POST['doctor_id']):
            
            messages.error(request, METHOD_ERROR)
            return None
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
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
                
                logging.error(f"Error Occured When Creating Reviews, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Creating Reviews: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return redirect(reverse('home'))


def get_reviews_id(request, doctor_id):
    
    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
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
                
                logging.error(f"Error Occured When Requesting Reviews, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return JsonResponse({"average_rating": 0, "Ratings": []})


def get_reviews(request):
    
    if request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
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
                
                logging.error(f"Error Occured When Requesting Reviews, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return JsonResponse({"average_rating": 0, "Ratings": []})

