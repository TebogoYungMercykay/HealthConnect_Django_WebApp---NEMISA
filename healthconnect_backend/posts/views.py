from django.shortcuts import render
from django.http import HttpResponse
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


def get_posts(request):
    
    if request.method == 'GET' or request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/posts/'

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
                
                logging.error(f"Error Occured When Requesting Posts Data: {e}: User_id: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Posts Data: {e}: User_id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def all_posts(request):
    
    if request.method == 'GET' or request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/posts/all_posts'

                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        return render(request, POSTS_TEMPLATE, {'all_posts': api_response.get('data')})
                
                logging.error(f"Error Occured When Requesting Posts Data: {e}: User_id: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Posts Data: {e}: User_id: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def create_post(request):
    
    if request.method == 'POST':
        
        if request.POST['title'] and request.POST['content']:
        
            try:
                user_id = request.session.get('user_id')
                
                if user_id != None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + '/posts/create_post'

                    post_data = {
                        "title": request.POST['title'],
                        "content": request.POST['content'],    
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

                            messages.info(request, "Successfully Created a Post")
                            return api_response.get('data')
                    
                    logging.error(f"Error Occured When Creating Post: {e}: User_id: {user_id}")
                    return None
                
                else:
                    raise PermissionDenied(USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Post: {e}: User_id: {user_id}")
                return None

        else:
            messages.error(request, MESSAGE)
            return redirect(reverse(POSTS_TEMPLATE))

    else:
        messages.error(request, METHOD_ERROR)
        return None


def get_post(request, post_id):
    
    if request.method == 'GET' or request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/posts/{post_id}'

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
                
                logging.error(f"Error Occured When Requesting Post Data: {e}: Post ID: {post_id}, User ID: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Post Data: {e}: Post ID: {post_id}, User ID: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def update_post(request, post_id):
    
    if request.method == 'GET' or request.method == 'POST':
        
        if request.POST['title'] and request.POST['content']:
            
            try:
                user_id = request.session.get('user_id')
                
                if user_id != None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + '/posts/{post_id}'

                    post_data = {
                        "title": request.POST['title'],
                        "content": request.POST['content'],    
                    }
                    
                    headers = {
                        "Content-Type": JSON_DATA,
                        "Authorization": f"{token_type} {jwt_token}",
                    }

                    response = requests.put(api_url, data=post_data, headers=headers)
                    response.raise_for_status()
                    
                    if response.status_code == 200:
                        api_response = response.json()
                        if api_response.get('status') == "success":

                            messages.info(request, "Post updated Successfully")
                            return api_response.get('data')
                    
                    logging.error(f"Error Occured When Requesting Post Data: {e}: Post ID: {post_id}, User ID: {user_id}")
                    return None
                
                else:
                    raise PermissionDenied(USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Requesting Post Data: {e}: Post ID: {post_id}, User ID: {user_id}")
                return None

        else:
            messages.error(request, "Missing Data, Please Try Again")
            return None
    
    else:
        messages.error(request, METHOD_ERROR)
        return None


def delete_post(request, post_id):
    
    if request.method == 'GET' or request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            
            if user_id != None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + '/posts/{post_id}'

                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.delete(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        messages.info(request, api_response.get('data'))
                        return api_response.get('data')
                
                logging.error(f"Error Occured When Requesting Post Data: {e}: Post ID: {post_id}, User ID: {user_id}")
                return None
            
            else:
                raise PermissionDenied(USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Post Data: {e}: Post ID: {post_id}, User ID: {user_id}")
            return None

    else:
        messages.error(request, METHOD_ERROR)
        return None


def create_reply(request, post_id):
    
    if request.method == 'POST':
        
        if request.POST['title'] and request.POST['content']:
        
            try:
                user_id = request.session.get('user_id')
                
                if user_id != None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + '/posts/create_reply'

                    post_data = {
                        "post_id": post_id,
                        "content": request.POST['content'],    
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

                            messages.info(request, "Successfully Created a Reply")
                            return api_response.get('data')
                    
                    logging.error(f"Error Occured When Creating Reply: {e}: Post ID: {post_id}, User ID: {user_id}")
                    return None
                
                else:
                    raise PermissionDenied(USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Reply: {e}: Post ID: {post_id}, User ID: {user_id}")
                return None

        else:
            messages.error(request, MESSAGE)
            return redirect(reverse(POSTS_TEMPLATE))

    else:
        messages.error(request, METHOD_ERROR)
        return None


def vote(request):
    
    if request.method == 'POST':
        
        if request.POST['post_id']: # and request.POST['dir']:
        
            try:
                user_id = request.session.get('user_id')
                
                if user_id != None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + '/posts/vote'

                    post_data = {
                        "post_id": request.POST['post_id'],
                        "dir": 1,    
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

                            messages.info(request, "Successfully Created a Reply")
                            return api_response.get('data')
                    
                    logging.error(f"Error Occured When Creating Reply: {e}: User_id: {user_id}")
                    return None
                
                else:
                    raise PermissionDenied(USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Reply: {e}: User_id: {user_id}")
                return None

        else:
            messages.error(request, MESSAGE)
            return redirect(reverse(POSTS_TEMPLATE))

    else:
        messages.error(request, METHOD_ERROR)
        return None

