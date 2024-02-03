from django.template import Template, Context
from django.shortcuts import render, redirect
import requests, logging, os, random
from django.contrib import messages
from .form import ContactForm
from ..utils import utils
# import mailtrap as mt

USER_MESSAGE = "Incorrect User Id Used, Please Try Again."
JSON_DATA = 'application/json'
METHOD_ERROR = "Incorrect Method Used, Please Try Again."
REMOVED = "[Removed]"
CONTACT_EMAIL = 'contact.html'    

def dashboard(request):
    
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


def health_news(request):
    
    articles_slice = None
    
    try:
        api_key = os.getenv("API_KEY_NEWSAPI")
        
        if request.session.get('user_id') is not None and api_key is not None and request.method == 'GET':

            api_url = f"https://newsapi.org/v2/top-headlines?language=en&category=health&apiKey={api_key}"
            response = requests.get(api_url)
            
            if response.status_code == 200:
                api_response = response.json()
                articles_slice = api_response.get('articles')[:12]
                        
    except Exception as e:
            logging.error(f"Error Occured When Requesting News Articles: {e}")

    if not articles_slice:
        articles_slice = utils.news_retrieval_error()
    
    for article_data in articles_slice:
        
        if not article_data['publishedAt']:
            article_data['publishedAt'] = "2024-01-29T18:22:38Z"
            
        if not article_data['author'] or article_data['author'] == REMOVED:
            article_data['author'] = "Sowmya Binu"
            
        if not article_data['urlToImage'] or article_data['urlToImage'] == REMOVED:
            article_data['urlToImage'] = "https://images.indianexpress.com/2024/01/rice_types_1600_freepik.jpg"  
             
        if not article_data['url'] or article_data['url'] == REMOVED:
            article_data['url'] = "https://removed.com"
            
        if not article_data['title'] or article_data['title'] == REMOVED:
            article_data['title'] = "Does switching from polished to unpolished rice control diabetes and weight? - The Indian Express"
                
        if not article_data['description'] or article_data['description'] == REMOVED:
            article_data['description'] = "For weight management and diabetes control, consuming foods low in calories, fat, and sugar is key. This is where fibre shines, said Dr Vikas Jindal, consultant, dept of gastroenterology, CK Birla Hospital, Delhi"              
        
        if not article_data['source']['name'] or article_data['source']['name'] == REMOVED:
            article_data['source']['name'] = "The Indian Express"
        
        article_data['publishedAt'] = utils.format_date(article_data['publishedAt'])
    
    if request.session.get('is_admin') and request.session.get('name') in 'Admin User':
        return render(request, 'admin-blog.html', { "articles": articles_slice })
    
    else:
        return render(request, 'articles.html', { "articles": articles_slice })


def sendmail(request):
    print("Send Mail: Here")
    if request.method == 'POST':
        
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                client_email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                
                template = Template("""
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    </head>
                    <body style="font-family: sans-serif;">
                        <div style="display: block; margin: auto; max-width: 600px;" class="main">
                            <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">
                                Health App Form Enquiry
                            </h1>
                            <p>Thank you for your interest in our Health App! We have received your form enquiry and will get back to you as soon as possible.</p>
                            <p>Here are the details you provided:</p>
                            <ul>
                                <li><strong>Name:</strong> {{ name }}</li>
                                <li><strong>Email:</strong> {{ email }}</li>
                                <li><strong>Subject:</strong> {{ subject }}</li>
                                <li><strong>Message:</strong> {{ message }}</li>
                            </ul>
                            <p>Our team will review your information and respond to your enquiry promptly. If you have any additional questions or concerns, feel free to reach out to us.</p>
                            <p>Thank you for choosing our HealthConnect App!</p>
                        </div>
                        <!-- Example of invalid for email HTML/CSS, will be detected by Mailtrap: -->
                        <style>
                            .main {
                                background-color: white;
                            }

                            a:hover {
                                border-left-width: 1em;
                                min-height: 2em;
                            }
                        </style>
                    </body>
                </html>
                """)
                
                context = Context({'name': name, 'email': client_email, 'subject': subject, 'message': message})
                html_content = template.render(context)

                mail = mt.Mail(
                    sender=mt.Address(email = os.environ.get('EMAIL_RECEIVER'), name = "Mailtrap Test"),
                    to = [mt.Address(email = client_email, name = "HealthConnect")],
                    subject = subject,
                    text = "Congrats for sending an email to HealthConnect",
                    html = html_content,
                    category = "Test",
                    headers = {"X-MT-Header": "HealthConnect"},
                    custom_variables = {"year": 2024},
                )

                client = mt.MailtrapClient(token=os.environ.get('EMAIL_HOST_PASSWORD'))
                client.send(mail)
                
                return render(request, CONTACT_EMAIL, {'status': "success", 'data': "Email sent successfully"})
            
            else:
                return render(request, CONTACT_EMAIL, {'status': "error", 'data': "Mailtrap is checking your domain credibility, it usually takes one business day"})

        except Exception as e:
            logging.error(f"Error Occurred When Sending Email: {e}")

            
    return render(request, CONTACT_EMAIL, {'status': "success", 'data': "Email sent successfully"})
