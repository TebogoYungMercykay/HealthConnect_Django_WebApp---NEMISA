from django.shortcuts import render

# Create your views here.

# from django.test import TestCase

# # Create your tests here.

# import requests
# from django.http import HttpResponse
# import requests

# def post_to_external_api(request):
#     api_url = 'https://healthconnect-python-fastapi-9b23b53a9ae4.herokuapp.com'
#     data_to_send = {'key': 'value'}

#     response = requests.post(api_url, data=data_to_send)

#     if response.status_code == 200:
#         result = response.json()  # Assuming the response is in JSON format
#         # Process the result as needed
#         return HttpResponse(f"Result from external API: {result}")
#     else:
#         return HttpResponse(f"Failed to post data. Status code: {response.status_code}")

# def get_external_data(request):
#     api_url = 'https://healthconnect-python-fastapi-9b23b53a9ae4.herokuapp.com'
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         return HttpResponse(f"Data from external API: {data}")
#     else:
#         return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")
