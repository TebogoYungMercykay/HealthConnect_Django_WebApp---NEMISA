from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from twilio.rest import Client
import requests, logging, json, os

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
POSTS_TEMPLATE = 'blog/posts.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."


def post_feedback(request, user_id):
    
    if request.method == 'POST':
        
        try:
            param = user_id
            user_id = request.session.get('user_id')
            
            if user_id != param and user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/chats/post_feedback/{user_id}'

                post_data = {
                    "feedback": request.POST['feedback'],   
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

                        return api_response.get('data')
                
                logging.error(f"Error Occured When Requesting FeedBack Data: {e}: User Id: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting FeedBack Data: {e}: User Id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def user_feedback(request, user_id):
    
    if request.method == 'GET' or request.method == 'POST':
        
        if not request.POST['feedback']:
            messages.error(request, MESSAGE)
            return None
        
        try:
            param = user_id
            user_id = request.session.get('user_id')
            
            if user_id != param and user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/chats/user_feedback/{user_id}'

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
                
                logging.error(f"Error Occured When Requesting FeedBack Data: {e}: User Id: {user_id}")
                return JsonResponse({'status': 'error', 'message': MESSAGE})
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting FeedBack Data: {e}: User Id: {user_id}")
            return JsonResponse({'status': 'error', 'message': MESSAGE})

    else:
        messages.error(request, METHOD_ERROR)
        return JsonResponse({'status': 'error', 'message': MESSAGE})


def chat_messages(request, user_id, messages):
    try:
        param = user_id
        user_id = request.session.get('user_id')

        if user_id != param and user_id is not None:
            jwt_token = request.session.get('access_token')
            token_type = request.session.get('token_type')

            api_url = os.getenv("API_ENDPOINT") + f'/chats/chat_messages/{user_id}'

            headers = {
                "Content-Type": JSON_DATA,
                "Authorization": f"{token_type} {jwt_token}",
            }

            response = requests.post(api_url, headers=headers)

            if response.status_code == 200:
                api_response = response.json()
                if api_response.get('status') == "success":
                    return api_response.get('data')

            logging.error(f"Error Occurred When Requesting Chat Data: {response.text}, User Id: {user_id}")
            return None

        else:
            messages.error(request, USER_MESSAGE)
            return None

    except requests.RequestException as e:
        logging.error(f"Error Occurred When Requesting Chat Data: {e}, User Id: {user_id}")
        return None


def create_chat(request, consultation_id, message, sender_id = None):
    try:
        user_id = request.session.get('user_id')

        if user_id is not None:
            jwt_token = request.session.get('access_token')
            token_type = request.session.get('token_type')

            api_url = os.getenv("API_ENDPOINT") + f'/chats/create_chat/{consultation_id}?sender_id={sender_id}'

            post_data = {  "message": message, }
            post_data = json.dumps(post_data, indent=4, ensure_ascii=False)

            headers = {
                "Content-Type": JSON_DATA,
                "Authorization": f"{token_type} {jwt_token}",
            }

            response = requests.post(api_url, data=post_data, headers=headers)

            if response.status_code == 200:
                api_response = response.json()
                if api_response.get('status') == "success":
                    return api_response.get('data')

            logging.error(f"Error Occurred When Requesting Chat Data: {response.text}, User Id: {user_id}")
            return None

        else:
            messages.error(request, USER_MESSAGE)
            return None

    except requests.RequestException as e:
        logging.error(f"Error Occurred When Requesting Chat Data: {e}, User Id: {user_id}")
        return None

def whatsapp(request):

    if request.method == 'POST':

        account_sid = os.getenv('TWIILO_ACCOUNT_SID')
        auth_token = os.getenv('TWIILO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body = request.POST.get('body'),
            to = 'whatsapp:' + os.getenv('TWIILO_MOBILE_NO')
        )

        print(message.sid)

        return redirect('admin_ui')


def meeting(request):
    return render(request, 'consultation/videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

