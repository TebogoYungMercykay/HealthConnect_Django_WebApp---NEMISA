from django.shortcuts import render, redirect
from django.contrib import messages
import requests, logging, json, os
from django.urls import reverse
from ..utils import utils

MESSAGE = "Some Error Occured, Please Try Again."
USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
POSTS_TEMPLATE = 'blog.html'
POST_TEMPLATE = 'blog-details.html'
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."

def all_posts(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            limit = 8
            
            if user_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/posts/all_posts?limit={limit}'

                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        api_response_data = api_response.get('data')
                        shuffled_images = utils.shuffled_images()
                        
                        for index, post in enumerate(api_response_data):
                            post_date = post["Post"]["created_at"]
                            post["Post"]["created_at"] = utils.format_date(post_date)

                            owner_date = post["Post"]["owner"]["created_at"]
                            post["Post"]["owner"]["created_at"] = utils.format_date(owner_date)

                            post["Post"]["image_link"] = shuffled_images[index % len(shuffled_images)]
                        
                        return render(request, POSTS_TEMPLATE, { 'all_posts': api_response_data} )
                
                logging.error(f"Error Occured When Requesting Posts Data, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Posts Data: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return render(request, POSTS_TEMPLATE, { 'all_posts': utils.post_retrieval_error()} )


def search_posts(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        if not request.POST['search']:
            return redirect(reverse('all_posts'))
            
        try:
            user_id = request.session.get('user_id')
            limit = 8
            search = request.POST['search']
            
            if user_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/posts/all_posts?search={search}&limit={limit}'

                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":

                        api_response_data = api_response.get('data')
                        
                        if len(api_response_data) == 0:
                            redirect(reverse('all_posts'))

                        shuffled_images = utils.shuffled_images()
                            
                        for index, post in enumerate(api_response_data):
                            post_date = post["Post"]["created_at"]
                            post["Post"]["created_at"] = utils.format_date(post_date)

                            owner_date = post["Post"]["owner"]["created_at"]
                            post["Post"]["owner"]["created_at"] = utils.format_date(owner_date)

                            post["Post"]["image_link"] = shuffled_images[index % len(shuffled_images)]
                        
                        return render(request, POSTS_TEMPLATE, { 'all_posts': api_response_data} )
                
                logging.error(f"Error Occured When Requesting Posts Data, User Id: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Posts Data: {e}, User Id: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return render(request, POSTS_TEMPLATE, { 'all_posts': utils.post_retrieval_error()} )


def create_post(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if request.POST['title'] and request.POST['content']:
        
            try:
                user_id = request.session.get('user_id')
                
                if user_id is not None:
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    post_data = {
                        "title": request.POST['title'],
                        "content": request.POST['content'],    
                    }

                    post_data = json.dumps(post_data, indent=4, ensure_ascii=False)
                    headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}",}

                    api_url = os.getenv("API_ENDPOINT") + '/posts/create_post'
                    response = requests.post(api_url, data=post_data, headers=headers)
                    response.raise_for_status()
                    
                    if response.status_code == 201:
                        api_response = response.json()
                        if api_response.get('status') == "success":

                            messages.info(request, "Successfully Created a Post")
                            return redirect('all_posts')
                    
                    logging.error(f"Error Occured When Creating Post, User Id: {user_id}")
                    messages.error(request, "Failed to Create a Post")
                
                else:
                    messages.error(request, USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Post: {e}, User Id: {user_id}")
                messages.error(request, "Error Occurred While Creating a Post")

        else:
            messages.error(request, MESSAGE)

    else:
        messages.error(request, METHOD_ERROR)
        messages.error(request, "Failed to Create a Post")
        
    return redirect(reverse('all_posts'))


def get_post(request, post_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/posts/{post_id}'

                headers = {
                    "Content-Type": JSON_DATA,
                    "Authorization": f"{token_type} {jwt_token}",
                }

                response = requests.post(api_url, headers=headers)
                response.raise_for_status()
                
                if response.status_code == 200:
                    api_response = response.json()
                    if api_response.get('status') == "success":
                        
                        api_response_data = api_response.get('data')
                        post_data = api_response_data["Post"]
                        
                        post_data["code_of_conduct"] = utils.code_of_conduct()[1]
                        post_data["code_of_conduct_content"] = utils.code_of_conduct()[0]
                        post_data["disclaimer_image"]: utils.code_of_conduct()[2]
                        
                        post_date = post_data["created_at"]
                        post_data["created_at"] = utils.format_date(post_date)

                        owner_date = post_data["owner"]["created_at"]
                        post_data["owner"]["created_at"] = utils.format_date(owner_date)

                        post_data["image_link"] = utils.code_of_conduct()[3]
                        
                        replies_data = api_response_data["replies"]
                        replies_images = utils.shuffled_dr_images()
                        
                        for index, reply in enumerate(replies_data):
                            reply_date = reply["created_at"]
                            reply["created_at"] = utils.format_date(reply_date)
                            reply["image_link"] = replies_images[index % len(replies_images)]
                            
                        return render(request, POST_TEMPLATE, {'post_details': api_response_data})
                
                logging.error(f"Error Occured When Requesting Post Data, Post ID: {post_id}, User ID: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Post Data: {e}, Post ID: {post_id}, User ID: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return render(request, POST_TEMPLATE, {'post_details': utils.get_posts_retrieval_error()})


def update_post(request, post_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        if request.POST['title'] and request.POST['content']:
            
            try:
                user_id = request.session.get('user_id')
                
                if user_id is not None:
                    
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    api_url = os.getenv("API_ENDPOINT") + f'/posts/{post_id}'

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
                    
                    logging.error(f"Error Occured When Requesting Post Data, Post ID: {post_id}, User ID: {user_id}")
                
                else:
                    messages.error(request, USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Requesting Post Data: {e}, Post ID: {post_id}, User ID: {user_id}")

        else:
            messages.error(request, "Missing Data, Please Try Again")
    
    else:
        messages.error(request, METHOD_ERROR)
        
    return None
    

def delete_post(request, post_id):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'GET' or request.method == 'POST':
        
        try:
            user_id = request.session.get('user_id')
            
            if user_id is not None:
                
                jwt_token = request.session.get('access_token')
                token_type = request.session.get('token_type')

                api_url = os.getenv("API_ENDPOINT") + f'/posts/{post_id}'

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
                
                logging.error(f"Error Occured When Requesting Post Data, Post ID: {post_id}, User ID: {user_id}")
            
            else:
                messages.error(request, USER_MESSAGE)
      
        except requests.RequestException as e:
            logging.error(f"Error Occured When Requesting Post Data: {e}, Post ID: {post_id}, User ID: {user_id}")

    else:
        messages.error(request, METHOD_ERROR)
        
    return None


def create_reply(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    post_id = 1
    
    if request.method == 'POST':
        
        if request.POST['post_id'] and request.POST['content']:
            
            try:
                user_id = request.session.get('user_id')
                post_id = request.POST['post_id']
                if user_id is not None:
                    jwt_token = request.session.get('access_token')
                    token_type = request.session.get('token_type')

                    post_data = {
                        "post_id": post_id,
                        "content": request.POST['content'],    
                    }

                    headers = { "Content-Type": JSON_DATA, "Authorization": f"{token_type} {jwt_token}",}
                    post_data = json.dumps(post_data, indent=4, ensure_ascii=False)
                    
                    api_url = os.getenv("API_ENDPOINT") + f'/posts/create_reply/{post_id}'
                    response = requests.post(api_url, data=post_data, headers=headers)
                    response.raise_for_status()
                    
                    
                    if response.status_code == 200:
                        api_response = response.json()
                        
                        if api_response.get('status') == "success":
                            messages.info(request, "Successfully Created a Reply")
                            return redirect('get_post', post_id=post_id)
                    
                    logging.error(f"Error Occured When Creating Reply, Post ID: {post_id}, User ID: {user_id}")
                
                else:
                    messages.error(request, USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Reply: {e}, Post ID: {post_id}, User ID: {user_id}")

        else:
            messages.error(request, MESSAGE)

    else:
        messages.error(request, METHOD_ERROR)
        
    return redirect(reverse('all_posts'))


def vote(request):
    
    request.session['prediction_successful'] = False
    request.session['message_successful'] = False
    
    if request.method == 'POST':
        
        if request.POST['post_id']: # and request.POST['dir']:
        
            try:
                user_id = request.session.get('user_id')
                
                if user_id is not None:
                    
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
                    
                    logging.error(f"Error Occured When Creating Reply, User Id: {user_id}")
                
                else:
                    messages.error(request, USER_MESSAGE)
        
            except requests.RequestException as e:
                logging.error(f"Error Occured When Creating Reply: {e}, User Id: {user_id}")

        else:
            messages.error(request, MESSAGE)
            return redirect(reverse(POSTS_TEMPLATE))

    else:
        messages.error(request, METHOD_ERROR)
        
    return None
