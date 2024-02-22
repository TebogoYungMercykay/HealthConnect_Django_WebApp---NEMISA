from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from ..utils import utils
from ..chats_and_feedback.views import create_chat, chat_messages
import requests
import logging
import json
import os
import random
from django.shortcuts import render
from django.http import JsonResponse
import random
import time
import hashlib
from agora_token_builder import RtcTokenBuilder
from ..auth.form import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
CONSULTATION_TEMPLATE = 'consultations/consultation.html'
CONSULTATION_CHATS_TEMPLATE = 'consultation-chats.html'
CONSULTATION_DOCTORS_TEMPLATE = 'consultations/consultationDoctors.html'
CONSULTATION_MANAGE_TEMPLATE = 'consultations/consultationManage.html'
CONSULTATION_VIDEO_TEMPLATE = 'consultations/consultationVideo.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."


# Helper Functions Starts Here

def get_doctors_data(request, user_id, jwt_token, token_type):
    try:
        api_url = os.getenv("API_ENDPOINT") + '/users/doctors'

        headers = {"Content-Type": JSON_DATA,
                   "Authorization": f"{token_type} {jwt_token}"}

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
        logging.error(
            f"Error Occurred When Requesting Doctor Data: {e}, User Id: {user_id}")

    messages.error(request, MESSAGE)
    return None


def get_consultation_history(request, user_id, jwt_token, token_type, is_patient):
    try:
        api_url = os.getenv("API_ENDPOINT") + \
            '/consultations/consultation_history_doctor'
        if is_patient:
            api_url = os.getenv("API_ENDPOINT") + \
                '/consultations/consultation_history_patient'

        headers = {"Content-Type": JSON_DATA,
                   "Authorization": f"{token_type} {jwt_token}"}

        response = requests.post(api_url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            api_response = response.json()
            if api_response.get('status') == "success":
                consultation_history = api_response.get('data')[
                    'Consultations']
                for consultation in consultation_history:

                    # consultation['consultation_date'] = utils.parse_string_date(consultation['consultation_date'])
                    consultation['diseaseinfo']['confidence'] = round(
                        consultation['diseaseinfo']['confidence'], 2)
                    consultation['list_symptoms'] = ', '.join(
                        map(str, consultation['diseaseinfo']['symptoms']))

                return consultation_history

    except requests.RequestException as e:
        logging.error(
            f"Error Occurred When Requesting Consultations: {e}, User Id: {user_id}")

    messages.error(request, MESSAGE)
    return None


def generate_channel_name(name1, name2, date):
    # Concatenate the email addresses and date
    data = f"{name1}{name2}{date}"
    hash_object = hashlib.sha256()
    # Update hash object with data
    hash_object.update(data.encode())
    # Get the hexadecimal representation of the hash
    hashed_data = hash_object.hexdigest()
    # Truncate to 64 bytes if necessary
    if len(hashed_data) > 64:
        hashed_data = hashed_data[:64]

    return hashed_data
def generate_numeric_uid(user_id):
    # Convert user_id to bytes for hashing
    user_id_bytes = str(user_id).encode('utf-8')
    
    # Use hashlib to generate a hash digest
    hash_digest = hashlib.sha256(user_id_bytes).hexdigest()
    
    # Convert the hash digest to an integer within the range of (0 to 2^32 - 1)
    numeric_uid = int(hash_digest, 16) % (2**32)
    
    return numeric_uid
# (Need a get doctors that renders a page too )


def get_doctors(request):

    if request.method == 'POST' or request.method == 'GET':
        try:
            user_id = request.session.get('user_id')
            if user_id is not None:
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')
                api_url = os.getenv("API_ENDPOINT") + '/users/doctors'

                # request info
                post_data = {
                    'consultation_dr': request.POST.get('consultation_dr', None),
                    'diseaseinfo_id': request.POST.get('diseaseinfo_id', None),
                    'diseaseinfo_name': request.POST.get('diseaseinfo_name', None)
                }
                headers = {"Content-Type": JSON_DATA,
                           "Authorization": f"{token_type} {jwt_token}"}
                response = requests.post(api_url, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        doctors_data = api_response.get('data')
                        for doctor in doctors_data:
                            doctor['activity'] = random.randint(3, 6)
                        
                        return render(request, CONSULTATION_DOCTORS_TEMPLATE, {"doctors_data": doctors_data, "prediction_data": post_data})

                logging.error(
                    f"Error Occurred When Requesting Doctor Data: {e}, User Id: {user_id}")
                return None
            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occurred When Requesting Doctor Data: {e}, User Id: {user_id}")

        messages.error(request, MESSAGE)
        return None


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

                consultation_history = get_consultation_history(
                    request, user_id, jwt_token, token_type, is_patient)

                if consultation_history is not None:
                    filter = request.GET.get('filter', None)
                    if filter is not None:
                        if filter == 'Old':
                            consultation_history = [consultation for consultation in consultation_history if consultation.get(
                                'consultation_date') <= utils.date_now()]
                        elif filter == 'Upcoming':
                            
                            consultation_history = [consultation for consultation in consultation_history if consultation.get(
                                'consultation_date') > utils.date_now()]

                    # status update
                    for c in consultation_history:
                        # should be and
                        if c.get('consultation_date') <= utils.date_now() or c.get('status') == 'approved':
                            
                            c['status'] = 'missed'

                    return render(request, CONSULTATION_MANAGE_TEMPLATE, {"consultation_history": consultation_history})

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occurred When Requesting Consultations: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    messages.error(
        request, 'Some error Occurred while requesting Consultations')
    return render(request, CONSULTATION_MANAGE_TEMPLATE, {"consultation_history": None})


def make_consultation(request):

    request.session['prediction_successful'] = False
    request.session['message_successful'] = False

    if request.method == 'POST':
        
        if not (request.POST['doctor_id'] and request.POST['diseaseinfo_id'] and request.POST['consultation_date'] and request.POST['status']):

            messages.error(request, METHOD_ERROR)
            return redirect(reverse('consultation'))

        else:
            try:
                user_id = request.session.get('user_id')
                if user_id is not None:

                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + \
                        '/consultations/make_consultation'

                    post_data = {
                        "doctor_id": request.POST['doctor_id'],
                        "diseaseinfo_id": request.POST['diseaseinfo_id'],
                        "consultation_date": request.POST['consultation_date'],
                        "status": request.POST['status']
                    }
                    post_data = json.dumps(
                        post_data, indent=4, ensure_ascii=False)

                    headers = {"Content-Type": JSON_DATA,
                               "Authorization": f"{token_type} {jwt_token}", }

                    response = requests.post(
                        api_url, data=post_data, headers=headers)
                    response.raise_for_status()

                    if response.status_code == 200:
                        api_response = response.json()
                        if api_response.get('status') == "success":
                            consultation_info = api_response.get('data')

                            consultation_url = reverse('consultation_view', args=[
                                                       consultation_info['consultation_id']])
                            return HttpResponseRedirect(consultation_url)

                    logging.error(
                        f"Error Occured When Requesting Consultations, User Id: {user_id}")

                else:
                    messages.error(request, USER_MESSAGE)

            except requests.RequestException as e:
                logging.error(
                    f"Error Occured When Requesting Consultations: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    return redirect(reverse('consultation'))


def consultation_view(request, consultation_id):

    request.session['prediction_successful'] = False
    request.session['message_successful'] = request.session.get(
        'message_successful')

    if request.method == 'POST' or request.method == 'GET':

        try:
            user_id = request.session.get('user_id')

            if user_id is not None and consultation_id is not None:

                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                headers = {"Content-Type": JSON_DATA,
                           "Authorization": f"{token_type} {jwt_token}", }

                api_url = os.getenv(
                    "API_ENDPOINT") + f'/consultations/consultation_view_patient/{consultation_id}'
                if request.session.get('is_patient') is False:
                    api_url = os.getenv(
                        "API_ENDPOINT") + f'/consultations/consultation_view_doctor/{consultation_id}'

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        consultation_info = api_response.get('data')

                        if consultation_info is not None:

                            # Formatting Consultation Info
                            consultation_info['consultation_date'] = utils.format_date(
                                consultation_info['consultation_date'])
                            consultation_info['diseaseinfo']['confidence'] = round(
                                consultation_info['diseaseinfo']['confidence'], 2)
                            consultation_info['list_symptoms'] = ', '.join(
                                map(str, consultation_info['diseaseinfo']['symptoms']))
                            consultation_info['doctor']['year_of_registration'] = utils.format_date(
                                consultation_info['doctor']['year_of_registration'])
                            consultation_info['doctor']['rating'] = round(
                                consultation_info['doctor']['rating'], 2)
                            consultation_info['patient']['dob'] = utils.format_date(
                                consultation_info['patient']['dob'])
                            consultation_info['patient']['age'] = utils.calculate_age(
                                consultation_info['patient']['dob'])
                            consultation_info['patient']['age'] = utils.calculate_age(
                                consultation_info['patient']['dob'])
                            consultation_info['days_elapsed_since'] = utils.days_elapsed_since(
                                consultation_info['consultation_date'])
                            # Formatting Chat Messages
                            consultation_chats = chat_messages(
                                request, consultation_id)
                            consultation_chats['length'] = len(
                                consultation_chats['chats'])
                            if consultation_chats is not None:
                                for chat in consultation_chats['chats']:
                                    chat['created_at'] = utils.format_date(
                                        chat['created_at'])

                            return render(request, CONSULTATION_MANAGE_TEMPLATE, {'consultation_info': consultation_info, 'consultation_chats': consultation_chats})

                        else:
                            messages.error(request, MESSAGE)

                logging.error(
                    f"Error Occured in Consultation View, User Id: {user_id}")

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occured in Consultation View: {e}, User Id: {user_id}")

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

                api_url = os.getenv(
                    "API_ENDPOINT") + f'/consultations/close_consultation/{consultation_id}'

                headers = {"Content-Type": JSON_DATA,
                           "Authorization": f"{token_type} {jwt_token}", }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        consultation_url = reverse(
                            'consultation_view', args=[consultation_id])
                        return HttpResponseRedirect(consultation_url)

                logging.error(
                    f"Error Occured When Consultation History, User Id: {user_id}")

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occured When Consultation History: {e}, User Id: {user_id}")

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

                api_url = os.getenv("API_ENDPOINT") + \
                    f'/consultations/create_review/{doctor_id}'

                post_data = {
                    "rating": request.POST['rating'],
                    "review": request.POST['review'],
                    "doctor_id": request.POST['doctor_id']
                }
                
                post_data = json.dumps(post_data, indent=4, ensure_ascii=False)
                headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }

                response = requests.post(
                    api_url, data=post_data, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    consultationID = request.POST['consultation_id']
                    if api_response.get('status') == "success":
                        return redirect('consultation_view', consultationID)

                logging.error(
                    f"Error Occured When Creating Reviews, User Id: {user_id}")

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occured When Creating Reviews: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    return redirect(reverse('consultation'))


def rate_prediction(request, consultation_id):
    
    stored_messages = messages.get_messages(request)
    for message in stored_messages:
        pass
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if not request.POST['diseasename'] or not request.POST['rating'] or not request.POST['doctor_id'] or not request.POST['diseaseinfo_id'] or not request.POST['consultation_id'] or not request.POST['symptoms']:
            messages.error(request, MESSAGE)
            
            redirect(reverse('home'))
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/consultations/rate_prediction'

                symptoms = request.POST['symptoms'].split(',')
                post_data = {
                    "symptoms": symptoms,
                    "rating": request.POST['rating'],
                    "diseasename": request.POST['diseasename'],
                    "doctor_id": request.POST['doctor_id'],
                    "diseaseinfo_id": request.POST['diseaseinfo_id'],
                    "consultation_id": request.POST['consultation_id'],
                }
                
                post_data = json.dumps(post_data, indent=4, ensure_ascii=False)
                headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}", }
                
                response = requests.post(api_url, data=post_data, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        messages.success(request, "Rating Prediction Posted Successfully")
                    
                        consultation_url = reverse('consultation_view', args=[consultation_id])
                        return HttpResponseRedirect(consultation_url)
                
                messages.error(f"Error Occured When Requesting FeedBack Data, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            messages.error(f"Error Occured When Requesting FeedBack Data, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
    
    redirect(reverse('consultation'))
    

def get_reviews_id(request, doctor_id):

    if request.method == 'POST':

        try:
            user_id = request.session.get('user_id')

            if user_id is not None:

                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + \
                    f'/consultations/get_reviews/{doctor_id}'

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

                logging.error(
                    f"Error Occured When Requesting Reviews, User Id: {user_id}")

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")

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

                api_url = os.getenv("API_ENDPOINT") + \
                    '/consultations/get_reviews'

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

                logging.error(
                    f"Error Occured When Requesting Reviews, User Id: {user_id}")

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occured When Requesting Reviews: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    return JsonResponse({"average_rating": 0, "Ratings": []})


# VideoCalling stuff.
def lauchvideocaller(request, consultation_id):

    if request.method == 'POST' or request.method == 'GET':
        try:
            user_id = request.session.get('user_id')
            if user_id is not None:
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')
                is_patient = request.session.get('is_patient')

                headers = {"Content-Type": JSON_DATA,
                           "Authorization": f"{token_type} {jwt_token}", }

                api_url = os.getenv(
                    "API_ENDPOINT") + f'/consultations/consultation_view_patient/{consultation_id}'
                if is_patient is False:
                    api_url = os.getenv(
                        "API_ENDPOINT") + f'/consultations/consultation_view_doctor/{consultation_id}'

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        consultation_info = api_response.get('data')

                        if consultation_info is not None:

                            # Formatting Consultation Info
                            # consultation_info['consultation_date'] = utils.format_date(consultation_info['consultation_date'])
                            patientname = consultation_info['patient']['name'] + \
                                consultation_info['patient']['surname']
                            doctorName = consultation_info['doctor']['name'] + \
                                consultation_info['doctor']['surname']
                            print(patientname, doctorName,
                                  consultation_info['consultation_date'])
                            roomName = generate_channel_name(
                                patientname, doctorName, consultation_info['consultation_date'])
                            
                            roomNameDisplay = f"{consultation_info['patient']['name']}_Dr{consultation_info['doctor']['name']}_consultation"
                            clientName = f"{consultation_info['patient']['name']} {consultation_info['patient']['surname']}" if is_patient else f"{consultation_info['doctor']['name']} {consultation_info['doctor']['surname']}"
                            otherUser= f"{consultation_info['patient']['name']} {consultation_info['patient']['surname']}" if not is_patient else f"{consultation_info['doctor']['name']} {consultation_info['doctor']['surname']}"
                            lobbyInfo = {
                                "clientName": clientName,
                                "roomNameDisplay": roomNameDisplay,
                                "roomName":roomName,
                                "consultation_id":consultation_id,
                                "otherUser":otherUser
                            }
                            return render(request, CONSULTATION_VIDEO_TEMPLATE, {'lobbyInfo': lobbyInfo})

                # create roomname or channelname for this consultation
                

                return render(request, CONSULTATION_VIDEO_TEMPLATE, {"lobby": 24})

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occurred When Launching video Consultation Lobby: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    messages.error(
        request, 'Some error Occurred while launching video Consultations Lobby')
    return render(request, CONSULTATION_VIDEO_TEMPLATE, {"lobby": 24})



def getToken(request,consultation_id):

    if request.method == 'POST' :
        try:
            user_id = request.session.get('user_id')
            if user_id is not None:
                is_doctor = request.session.get('is_doctor')
                numeric_uid_for_agora = generate_numeric_uid(user_id)
                chanel_for_agora = request.POST['room']
                username= request.POST['name']
                roomDisplay = request.POST['roomName']
                otherUser =  request.POST['otheruser']
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')
                headers = {"Content-Type": JSON_DATA,
                               "Authorization": f"{token_type} {jwt_token}", }
                if is_doctor: 
                    api_url = os.getenv("API_ENDPOINT") + f'/consultations/update_consultation/{consultation_id}'
                    post_data = {
                        "channel": chanel_for_agora,
                    }
                    #post_data = json.dumps(post_data, indent=4, ensure_ascii=False)                
                    response = requests.put(api_url, json=post_data, headers=headers)
                    response.raise_for_status()
                else:
                    api_url = os.getenv(
                    "API_ENDPOINT") + f'/consultations/consultation_view_patient/{consultation_id}'
                    #get the condultation 
                    response = requests.post(api_url, headers=headers)
                    response.raise_for_status()

                if response.status_code == 200:
                        api_response = response.json()
                        response_data = api_response.get('data')
                        
                        
                        appId = os.getenv("APP_ID")
                        appCertificate = os.getenv("APP_CERT")
                        # channelName = request.GET.get('channel')
                        # uid = random.randint(1, 230)  # must be a num 1-230
                        channelName=chanel_for_agora if is_doctor else response_data['channel']
                        uid=numeric_uid_for_agora
                        expirationTimeInSeconds = 3600*24  # when should the token expire?
                        currentTimeStamp = int(time.time())
                        privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
                        
                        role = 1 if is_doctor else 2 # 1 = host 2=guest

                        token = RtcTokenBuilder.buildTokenWithUid(
                            appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
                        
                        # create roomname or channelname for this consultation
                        videocall_data= {
                                    'UID': uid,
                                    'token': token,
                                    'room': channelName,
                                    'room_display':roomDisplay,
                                    'name': username,
                                    'app_id':appId,
                                    'other_user':otherUser
                                }
                        print(videocall_data)
                        return render(request, CONSULTATION_VIDEO_TEMPLATE, {"videocall_data": videocall_data})
                logging.error(
                    f"Error Occurred When Launching consultation : {e}, User Id: {user_id}")
                return None

            else:
                messages.error(request, USER_MESSAGE)

        except requests.RequestException as e:
            logging.error(
                f"Error Occurred When Launching video Consultation: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)

    messages.error(
        request, 'Some error Occurred while launching video Consultations')
    return render(request, CONSULTATION_VIDEO_TEMPLATE, {"lobby": 24})

    # return JsonResponse({'token': token, 'uid': uid}, safe=False)


def getTokenOld(request):

    appId = os.getenv("APP_ID")
    appCertificate = os.getenv("APP_CERT")
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)  # must be a num 1-230
    expirationTimeInSeconds = 3600*24  # when should the token expire?
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1  # 1 = host 2=guest

    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    # Ajax call made will take this response
    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name': data['name']}, safe=False)


# def getMember(request):
#     uid = request.GET.get('UID')
#     room_name = request.GET.get('room_name')

#     member = RoomMember.objects.get(
#         uid=uid,
#         room_name=room_name,
#     )
#     name = member.name
#     return JsonResponse({'name': member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)