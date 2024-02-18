from django.template import Template, Context
from django.shortcuts import render, redirect
import requests, logging, os, random
from django.contrib import messages
from .form import ContactForm
from ..utils import utils

USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."
REMOVED = "[Removed]"
CONTACT_EMAIL = 'contact.html'    

def dashboard(request):
    
    stored_messages = messages.get_messages(request)
    for message in stored_messages:
        pass
    
    if request.method == 'GET':

        return render(request, 'admin-dashboard.html', {
                'cards': utils.cards(),
                'recent_activity': utils.recent_activity(),
                'top_selling_medication': utils.top_selling_medication(),
                'recent_consultations': utils.recent_consultations()
            }
        )

    else:
        return redirect('home')


def diseaseinfos(request):
    
    stored_messages = messages.get_messages(request)
    for message in stored_messages:
        pass
    
    table_data = None
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None and request.session.get('is_admin'):
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/admin'
                headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }
                
                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        table_data = api_response.get('data')

        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Diseases Data: {e}: User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    if not table_data:
        table_data = utils.admin_table()

    # Table
    for data in table_data:
        if data['symptoms']:
            data['list_symptoms'] = ', '.join(map(str, data['symptoms']))
        else:
            data['list_symptoms'] = "Unresolved"
            
        if data['consultation_date']:
            data['consultation_date'] = utils.format_date(data['consultation_date'])
        else:
            data['consultation_date'] = "Unresolved"
    
    # Cards
    card_data = utils.admin_card()
    total = len(table_data)
    closed = sum(1 for entry in table_data if entry["status"] == "closed")
    
    card_data[0]["value"] = total
    card_data[1]["value"] = closed
    card_data[2]["value"] = total - closed
    
    increase_1 = random.randint(1, closed)
    increase_2 = random.randint(1, total - closed)
    card_data[0]["status"]["count"] = increase_1 + increase_2
    card_data[1]["status"]["count"] = increase_1
    card_data[2]["status"]["count"] = increase_2
    
    return render(request, 'admin-diseaseinfos.html', { 'admin_table': table_data, 'admin_card': card_data })


def sendmail(request):
    stored_messages = messages.get_messages(request)
    for message in stored_messages:
        pass
    
    messages.info(request, "Contact Query Sent successfully.")
    return render(request, CONTACT_EMAIL, {'status': "success", 'data': "Contact Query Sent successfully."})
