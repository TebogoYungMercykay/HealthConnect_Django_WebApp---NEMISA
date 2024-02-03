from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
import requests, logging, json, os
from django.urls import reverse
# from twilio.rest import Client

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
POSTS_TEMPLATE = 'blog/posts.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."


def post_feedback(request, doctor_id, consultation_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if not request.POST['feedback']:
            messages.error(request, MESSAGE)
            
            redirect(reverse('home'))
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/chats/post_feedback/{doctor_id}'

                post_data = { "feedback": request.POST['feedback'], }
                post_data = json.dumps(post_data, indent=4, ensure_ascii=False)

                headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }
                
                response = requests.post(api_url, data=post_data, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        messages.success(request, "Feedback Posted Successfully")
                    
                        consultation_url = reverse('consultation_view', args=[consultation_id])
                        return HttpResponseRedirect(consultation_url)
                
                logging.error(f"Error Occured When Requesting FeedBack Data, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting FeedBack Data: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
    
    redirect(reverse('home'))


def user_feedback(request, user_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        if not request.POST['feedback']:
            messages.error(request, MESSAGE)
            return None
        
        try:
            param = user_id
            user_id = request.session.get('user_id')
            
            if user_id is not param and user_id is not None:
                
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
                
                logging.error(f"Error Occured When Requesting FeedBack Data, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting FeedBack Data: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return JsonResponse({'status': 'error', 'message': MESSAGE})


def chat_messages(request, consultation_id, sender_id = None):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = request.session.get('message_successful')
    
    try:
        user_id = request.session.get('user_id')

        if user_id is not None:
            jwt_token = request.session.get('access_token')
            token_type = request.session.get('token_type')

            api_url = os.getenv("API_ENDPOINT") + f'/chats/chat_messages/{consultation_id}'

            headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }
            response = requests.post(api_url, headers=headers)

            if response.status_code == 200:
                api_response = response.json()
                
                if api_response.get('status') == "success":
                    return api_response.get('data')
            
            logging.error(f"Error Occurred When Reading Chat Data, User Id: {user_id}")

        else:
            messages.error(request, USER_MESSAGE)

    except requests.RequestException as e:
        logging.error(f"Error Occurred When Reading Chat Data: {e}, User Id: {user_id}")
    
    return None


def create_chat(request, consultation_id, message, sender_id = None):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    try:
        user_id = request.session.get('user_id')

        if user_id is not None:
            jwt_token = request.session.get('access_token')
            token_type = request.session.get('token_type')

            api_url = os.getenv("API_ENDPOINT") + f'/chats/create_chat/{consultation_id}?sender_id={sender_id}'

            post_data = {  "message": message, }
            post_data = json.dumps(post_data, indent=4, ensure_ascii=False)

            headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }
            response = requests.post(api_url, data=post_data, headers=headers)

            if response.status_code == 200:
                api_response = response.json()
                if api_response.get('status') == "success":
                    return api_response.get('data')

            logging.error(f"Creating Chat Data, User Id: {user_id}")

        else:
            messages.error(request, USER_MESSAGE)

    except requests.RequestException as e:
        logging.error(f"Creating Chat Data: {e}, User Id: {user_id}")
    
    return None


def send_message(request, consultation_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if request.POST.get('message'):
            try:
                user_id = request.session.get('user_id')

                if user_id is not None:

                    message = request.POST.get('message')

                    chat_messages = create_chat(request, consultation_id, message, user_id)
                    if chat_messages is not None:
                        request.session['message_successful'] = True
                        messages.success(request, "Message Sent Successfully")

                    else:
                        logging.error(f"Creating Chat Data, User Id: {user_id}")

                else:
                    messages.error(request, USER_MESSAGE)

            except requests.RequestException as e:
                logging.error(f"Creating Chat Data: {e}, User Id: {user_id}")
            
        else:
            messages.error(request, MESSAGE)

    consultation_url = reverse('consultation_view', args=[consultation_id])
    return HttpResponseRedirect(consultation_url)

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

        return redirect('home')


def meeting(request):
    return render(request, 'consultation/videocall.html', {'name': request.user.first_name + " " + request.user.last_name})
