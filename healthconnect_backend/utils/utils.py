from datetime import datetime
from dateutil import parser
import random


TEMP_EMAIL = "temp@gmail.com"
TEMP_DATETIME = "Jan 29, 2024"
DOCTOR = "Medical Doctor"

def shuffled_images():
    posts_images = [
        'img/blog/blog-1.jpg', 'img/blog/blog-2.jpg', 'img/blog/blog-3.jpg',
        'img/blog/blog-4.jpg', 'img/blog/blog-5.jpg', 'img/blog/blog-6.jpg',
        'img/blog/blog-7.jpg', 'img/blog/blog-8.jpg', 'img/blog/blog-9.jpg'
    ]
    
    random.shuffle(posts_images)
    
    return posts_images


def shuffled_dr_images():
    dr_images = [
        'comments-1.jpg', 'comments-2.jpg', 'comments-3.jpg',
        'comments-4.jpg', 'comments-5.jpg', 'comments-6.jpg',
        'comments-1.jpg', 'comments-2.jpg', 'comments-3.jpg',
        'comments-4.jpg', 'comments-5.jpg', 'comments-6.jpg'
    ]
    
    random.shuffle(dr_images)
    
    return dr_images


def format_date(input_string):
    try:
        input_date = parser.parse(input_string)
        formatted_date = input_date.strftime("%b %d, %Y")
        return formatted_date

    except parser.ParserError:
        return "Jan 1, 2024"


def days_elapsed_since(start_date_str):
    start_date = datetime.strptime(start_date_str, '%b %d, %Y')
    current_date = datetime.now()
    days_elapsed = (current_date - start_date).days

    return abs(days_elapsed)


def days_between_dates(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%b %d, %Y')
    date2 = datetime.strptime(date_str2, '%b %d, %Y')
    days_difference = (date2 - date1).days

    return abs(days_difference)


def calculate_age(dob):
    dob_date = datetime.strptime(dob, '%b %d, %Y')
    current_date = datetime.now()

    age = current_date.year - dob_date.year

    if (current_date.month, current_date.day) < (dob_date.month, dob_date.day):
        age -= 1

    return age


def code_of_conduct():
    return [
        [
            "<strong>HealthConnect</strong> is an interactive platform designed to facilitate discussions and share information on various topics. We encourage a positive and respectful community where users can engage in meaningful conversations.",
            "<strong>Respect and Sensitivity</strong>: Users are prohibited from publishing sensitive or private information about other users without their explicit consent. Avoid making any allegations based on the content of posts.",
            "<strong>Non-Discrimination</strong>: Discrimination based on race, gender, religion, nationality, disability, sexual orientation, or any other factor is strictly prohibited. Users are encouraged to engage in inclusive and respectful discussions.",
            "<strong>Identity Protection</strong>: Users must refrain from attempting to expose the identity of others. Do not share personal information that could lead to the identification of individuals, both on the platform and off.",
            "<strong>Allergations</strong>: Making unsupported allegations against individuals or groups is not allowed. Users should provide factual and constructive contributions to discussions.",
            "<strong>Legal and Ethical Standards</strong>: Users are expected to comply with all applicable laws and ethical standards. Any content that violates legal regulations or ethical norms will be removed."
        ],
        "User Conduct and Sensitive Information Disclaimer",
        'img/blog/blog-inside-post.jpg',
        'img/blog/about.jpg'
    ]


def get_random_user():
    return {
        "user": {
            "id": 123,
            "email": "general@gmail.com",
            "created_at": "2023-11-20T08:15:30.123456Z"
        },
        "details": {
            "name": "General",
            "surname": "User",
            "address": "Lillian Ngoyi St, Pretoria Central, Pretoria, 0001",
            "mobile_no": 15551234567,
            "dob": "1900-01-01T10:00:00",
            "gender": "Other"
        }
    }


def get_posts_retrieval_error():
    shuffled_dr_image = shuffled_dr_images()
    return {
        "Post": {
            "title": "General Health Inquiry: Doctors' Insights Welcome",
            "content": "I have some general health concerns and would like to seek advice from doctors or healthcare professionals in the community. Feel free to share your insights on maintaining overall health, preventive measures, and when it's essential to consult with a medical professional.",
            "code_of_conduct": code_of_conduct()[1],
            "code_of_conduct_content": code_of_conduct()[0],
            "published": True,
            "id": 12,
            "created_at": TEMP_DATETIME,
            "owner_id": 8,
            "image_link": code_of_conduct()[3],
            "disclaimer_image": code_of_conduct()[2],
            "owner": {
                "id": 8,
                "email": TEMP_EMAIL,
                "created_at": TEMP_DATETIME
            }
        },
        "votes": 5,
        "replies": [
            {
                "post_id": 12,
                "content": "Your dedication to maintaining good health is truly admirable. Remember to lead a well-balanced lifestyle by incorporating healthy dietary choices, regular exercise, and adequate rest. Prioritizing preventive measures like vaccinations and routine health check-ups is essential. Seeking advice from healthcare professionals can provide valuable insights on when to address specific health concerns. Consistent communication with healthcare providers plays a crucial role in proactive health management.",
                "created_at": TEMP_DATETIME,
                "image_link": shuffled_dr_image[0]
            },
            {
                "post_id": 12,
                "content": "Commendations on your commitment to a healthy lifestyle. Ensure a balance in your daily routine by focusing on nutritious meals, physical activity, and ample rest. Give importance to preventive actions such as vaccinations and regular health check-ups. Seeking guidance from healthcare professionals will offer valuable insights on when to address specific health issues. Regular communication with healthcare providers is vital for effective proactive health management.",
                "created_at": TEMP_DATETIME,
                "image_link": shuffled_dr_image[2]
            },
            {
                "post_id": 12,
                "content": "Your dedication to maintaining good health is highly commendable. Strive for a balanced lifestyle through healthy eating, regular exercise, and sufficient rest. Emphasize preventive measures like vaccinations and routine health check-ups. Consulting with healthcare professionals will provide valuable insights on when to address specific health concerns. Consistent communication with healthcare providers is key to proactive health management.",
                "created_at": TEMP_DATETIME,
                "image_link": shuffled_dr_image[3]
            },
            {
                "post_id": 12,
                "content": "Admirable commitment to your health journey. Ensure a balance in your lifestyle with healthy eating, regular exercise, and enough rest. Prioritize preventive measures such as vaccinations and regular health check-ups. Seeking guidance from healthcare professionals will offer valuable insights on when to address specific health concerns. Regular communication with healthcare providers is essential for proactive health management.",
                "created_at": TEMP_DATETIME,
                "image_link": shuffled_dr_image[4]
            }
        ]
    }


def get_first_message():
    return  {
        "consultation_id": 100,
        "status": "closed",
        "chats": [
            {
                "consultation_id": 3,
                "created_at": "2024-01-11T10:34:09.062302",
                "message": "Welcome to our consultation chat. I'm Dr. Taylor and I'm here to assist you. It's great to connect with you! When you have some questions, concerns, or if there's anything you'd like to discuss, feel free to let me know. Your health is my priority.",
                "sender_id": 8
            }
        ]
    }


def get_symptoms():
    return sorted([
        'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
        'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination',
        'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
        'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
        'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
        'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
        'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
        'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
        'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
        'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
        'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
        'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
        'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
        'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
        'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
        'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
        'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
        'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
        'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
        'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
        'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
        'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
        'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
        'yellow_crust_ooze'
    ])


def news_retrieval_error():
    return [
        {
            "source": {
                "id": None,
                "name": "Netmeds.com"
            },
            "author": "Sowmya Binu",
            "title": "Diabetes Care: Manage Blood Sugar Levels With Smart Carbohydrate Choices - Netmeds.com",
            "description": "Read about carbohydrates and diabetes type 2 and how this ailment can be managed and blood sugar levels be kept in check by smart carbohydrate choices in daily life in the feature.",
            "url": "https://www.netmeds.com/health-library/post/diabetes-care-manage-blood-sugar-levels-with-smart-carbohydrate-choices",
            "urlToImage": "https://www.netmeds.com/images/cms/magefan_blog/nmslite/1706519863_Diabetes-care_480x180.jpg",
            "publishedAt": "2024-01-29T18:30:00Z",
            "content": "Diabetes is a chronic metabolic disorder categorised by elevated blood sugar levels and requires careful management to avert complications and maintain overall health. One key aspect of diabetes mana… [+4961 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "YouTube"
            },
            "author": None,
            "title": "Connection between Covid & diabetes - WSMV 4 Nashville",
            "description": "As Covid cases exploded across the country, doctors realized another virus was skyrocketing at the same time.   For more Local News from WSMV:  https://www.w...",
            "url": "https://www.youtube.com/watch?v=8zyuP8ETIzo",
            "urlToImage": "https://i.ytimg.com/vi/8zyuP8ETIzo/maxresdefault.jpg",
            "publishedAt": "2024-01-29T18:28:13Z",
            "content": None
        },
        {
            "source": {
                "id": None,
                "name": "Futurity: Research News"
            },
            "author": "National University of Singapore",
            "title": "Mosquito protein could block dengue virus infection - Futurity: Research News",
            "description": "A protein found in a mosquito's exoskeleton could offer protection against dengue virus, a new study shows.",
            "url": "https://www.futurity.org/mosquitos-protein-dengue-fever-viruses-317214/",
            "urlToImage": "https://www.futurity.org/wp/wp-content/uploads/2024/01/mosquito-dengue-1600.jpg",
            "publishedAt": "2024-01-29T18:27:02Z",
            "content": "Despite its role as a carrier of the dengue virus, the female Aedes aegypti mosquito could possess the key to discovering new anti-viral strategies to control dengue virus infection, researchers repo… [+3444 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "YouTube"
            },
            "author": None,
            "title": "How to navigate the different symptoms during cold and flu season - ABC11",
            "description": "The are certain questions to ask yourself to understand what you're body is dealing with.Story: https://abc11.com/covid-symptoms-common-cold-flu-season-how-t...",
            "url": "https://www.youtube.com/watch?v=5lri9KNmZlU",
            "urlToImage": "https://i.ytimg.com/vi/5lri9KNmZlU/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLAdYpZR9g26zfL9BNlG03DU_I0d8g",
            "publishedAt": "2024-01-29T18:22:38Z",
            "content": None
        },
        {
            "source": {
                "id": None,
                "name": "Nature.com"
            },
            "author": None,
            "title": "Signs of 'transmissible' Alzheimer's seen in people who received growth hormone - Nature.com",
            "description": "The findings support a controversial hypothesis that proteins related to the neurodegenerative disease can be ‘seeded’ in the brain through material taken from cadavers.",
            "url": "https://www.nature.com/articles/d41586-024-00268-5",
            "urlToImage": "https://media.nature.com/lw1024/magazine-assets/d41586-024-00268-5/d41586-024-00268-5_26671396.jpg",
            "publishedAt": "2024-01-29T17:18:19Z",
            "content": None
        },
        {
            "source": {
                "id": None,
                "name": "[Removed]"
            },
            "author": None,
            "title": "[Removed]",
            "description": "[Removed]",
            "url": "https://removed.com",
            "urlToImage": None,
            "publishedAt": "1970-01-01T00:00:00Z",
            "content": "[Removed]"
        },
        {
            "source": {
                "id": None,
                "name": "NDTV News"
            },
            "author": None,
            "title": "Haircare Tips: Nutritionist Explains Why Certain Vitamins Are Essential For Hair Health - NDTV",
            "description": "It's recommended to maintain a balanced diet, consult a healthcare professional, and follow their advice for personalised guidance on vitamin intake for hair health.",
            "url": "https://www.ndtv.com/health/haircare-tips-nutritionist-explains-why-certain-vitamins-are-essential-for-hair-health-4955316",
            "urlToImage": "https://c.ndtvimg.com/2022-06/p0hm464_haircare650_625x300_30_June_22.jpg",
            "publishedAt": "2024-01-29T15:33:00Z",
            "content": "Vitamin B5 strengthens hair follicles, reduces hair loss, and adds shine and softness to the hair strands\r\nVitamins play a crucial role in maintaining overall hair health. Nutritionist Anjali Mukerje… [+2467 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "The Indian Express"
            },
            "author": "Lifestyle Desk",
            "title": "Does switching from polished to unpolished rice control diabetes and weight? - The Indian Express",
            "description": "For weight management and diabetes control, consuming foods low in calories, fat, and sugar is key. This is where fibre shines, said Dr Vikas Jindal, consultant, dept of gastroenterology, CK Birla Hospital, Delhi",
            "url": "https://indianexpress.com/article/lifestyle/life-style/switch-polished-unpolished-rice-benefits-control-diabetes-weight-nutrients-how-to-cook-9123061/",
            "urlToImage": "https://images.indianexpress.com/2024/01/rice_types_1600_freepik.jpg",
            "publishedAt": "2024-01-29T15:32:59Z",
            "content": "There are so many theories floating around that the consumption of polished rice may not be good for individuals who are watching their weight or trying to lower their blood sugar levels. As such, ce… [+4309 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "[Removed]"
            },
            "author": None,
            "title": "[Removed]",
            "description": "[Removed]",
            "url": "https://removed.com",
            "urlToImage": None,
            "publishedAt": "1970-01-01T00:00:00Z",
            "content": "[Removed]"
        },
        {
            "source": {
                "id": None,
                "name": "[Removed]"
            },
            "author": None,
            "title": "[Removed]",
            "description": "[Removed]",
            "url": "https://removed.com",
            "urlToImage": None,
            "publishedAt": "1970-01-01T00:00:00Z",
            "content": "[Removed]"
        },
        {
            "source": {
                "id": None,
                "name": "KCRA Sacramento"
            },
            "author": None,
            "title": "Avian flu is devastating farms in California's 'Egg Basket' as outbreaks roil poultry industry - KCRA Sacramento",
            "description": "Last month, Mike Weber got the news every poultry farmer fears: His chickens tested positive for avian flu.",
            "url": "https://www.kcra.com/article/avian-flu-is-devastating-farms-in-californias-egg-basket-as-outbreaks-roil-poultry-industry/46569691",
            "urlToImage": "https://kubrick.htvapps.com/htv-prod-media.s3.amazonaws.com/images/gettyimages-1408473972-65b7bccc70eb1.jpg?crop=1.00xw:0.846xh;0,0.0711xh&resize=1200:*",
            "publishedAt": "2024-01-29T15:05:00Z",
            "content": "PETALUMA, Calif. —Last month, Mike Weber got the news every poultry farmer fears: His chickens tested positive for avian flu.\r\nFollowing government rules, Weber's company, Sunrise Farms, had to slaug… [+5546 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "CNET"
            },
            "author": None,
            "title": "What's Causing the Ringing in Your Ears and How to Stop It - CNET",
            "description": "That ringing in your ears is called tinnitus, and there are ways to make it less bothersome.",
            "url": "https://www.cnet.com/health/medical/whats-causing-the-ringing-in-your-ears-and-how-to-stop-it/",
            "urlToImage": "https://www.cnet.com/a/img/resize/eca08691fb77e5ee6f05819765b73d442253127b/hub/2024/01/25/54176717-d34e-44af-a3ac-c342396cf11e/gettyimages-1777374318.jpg?auto=webp&fit=crop&height=675&width=1200",
            "publishedAt": "2024-01-29T15:00:00Z",
            "content": "A ringing in your ears that comes and goes isn't just an annoyance that makes it difficult to concentrate, it could be a sign that you have tinnitus. Tinnitus can sound like a soft or loud buzzing, w… [+5113 chars]"
        }
    ]


def post_retrieval_error():
    shuffled_image = shuffled_images()
    
    return [
        {
            "Post": {
                "title": "Skin Health Inquiry: Dermatologists' Recommendations",
                "content": "I've noticed some changes in my skin health and would like to seek advice from dermatologists or doctors with expertise in skincare. Please share your insights on common skin concerns, preventive skincare measures, and when it's essential to consult with a dermatologist for a personalized assessment.",
                "published": 'true',
                "id": 4,
                "created_at": TEMP_DATETIME,
                "owner_id": 8,
                "image_link": shuffled_image[0],
                "owner": {
                    "id": 8,
                    "email": TEMP_EMAIL,
                    "created_at": TEMP_DATETIME
                }
            },
            "votes": 0,
            "replies": [
                {
                    "post_id": 4,
                    "content": "Hello there! It's great that you're proactive about your skin health. If you've noticed changes, it's advisable to maintain a consistent skincare routine with gentle cleansers and moisturizers. However, for personalized advice, it's essential to consult with a dermatologist. They can assess your specific skin type, address concerns, and recommend suitable products or treatments.",
                    "created_at": TEMP_DATETIME
                }
            ]
        },
        {
            "Post": {
                "title": "Weight Management: Doctor's Perspective Needed",
                "content": "I've been struggling with weight management and finding it challenging to achieve a healthy balance. Nutritionists or doctors, could you share insights on effective weight management strategies, potential underlying issues, and how to create a sustainable plan?",
                "published": 'true',
                "id": 10,
                "created_at": TEMP_DATETIME,
                "owner_id": 12,
                "image_link": shuffled_image[1],
                "owner": {
                    "id": 12,
                    "email": TEMP_EMAIL,
                    "created_at": TEMP_DATETIME
                }
            },
            "votes": 0,
            "replies": [
                {
                    "post_id": 10,
                    "content": "Achieving a healthy weight is a commendable goal. Consider consulting with a nutritionist to create a personalized diet plan tailored to your needs. Additionally, incorporating regular physical activity can greatly contribute to your weight management journey.",
                    "created_at": TEMP_DATETIME
                }
            ]
        },
        {
            "Post": {
                "title": "Nutrition Query: Seeking a Doctor's Opinion",
                "content": "I've been working on improving my diet, but I'm still unsure about the right balance of nutrients for my specific health goals. Nutritionists or doctors, could you provide guidance on crafting a personalized nutrition plan for overall health and well-being?",
                "published": 'true',
                "id": 6,
                "created_at": TEMP_DATETIME,
                "owner_id": 8,
                "image_link": shuffled_image[2],
                "owner": {
                    "id": 8,
                    "email": TEMP_EMAIL,
                    "created_at": TEMP_DATETIME
                }
            },
            "votes": 0,
            "replies": [
                {
                    "post_id": 6,
                    "content": "Navigating nutrition can be complex, but seeking professional advice is a great step. Consider consulting with a nutritionist or dietitian to create a personalized nutrition plan based on your health goals. They can provide valuable insights and guidance tailored to your individual needs.",
                    "created_at": TEMP_DATETIME
                }
            ]
        },
        {
            "Post": {
                "title": "Dealing with Chronic Pain: Seeking Guidance",
                "content": "I've been experiencing persistent chronic pain lately, and it's affecting my daily life. I'm reaching out to the community for advice on managing chronic pain. If any doctors are here, I would appreciate your insights on potential causes and treatment options.",
                "published": 'true',
                "id": 5,
                "created_at": TEMP_DATETIME,
                "owner_id": 8,
                "image_link": shuffled_image[3],
                "owner": {
                    "id": 8,
                    "email": TEMP_EMAIL,
                    "created_at": TEMP_DATETIME
                }
            },
            "votes": 0,
            "replies": [
                {
                    "post_id": 5,
                    "content": "I'm sorry to hear about your persistent chronic pain. It's recommended to consult with a healthcare professional, possibly a pain specialist, for a thorough evaluation. In the meantime, consider gentle exercises, heat therapy, and over-the-counter pain relievers as temporary relief. Professional advice is crucial for a comprehensive pain management plan.",
                    "created_at": TEMP_DATETIME
                }
            ]
        },
        {
            "Post": {
                "title": "Coping with Anxiety: Doctor's Advice Needed",
                "content": "Lately, I've been struggling with anxiety, and it's affecting my daily life. I would appreciate advice from mental health professionals or doctors on coping mechanisms, potential therapies, and lifestyle changes that could help manage anxiety effectively.",
                "published": 'true',
                "id": 7,
                "created_at": TEMP_DATETIME,
                "owner_id": 11,
                "image_link": shuffled_image[4],
                "owner": {
                    "id": 11,
                    "email": TEMP_EMAIL,
                    "created_at": TEMP_DATETIME
                }
            },
            "votes": 0,
            "replies": [
                {
                    "post_id": 7,
                    "content": "Dealing with anxiety can be challenging. It's important to consult with a mental health professional for personalized advice. In the meantime, consider incorporating relaxation techniques such as deep breathing and mindfulness into your daily routine. Professional support can make a significant difference.",
                    "created_at": TEMP_DATETIME
                }
            ]
        },
        {
            "Post": {
                "title": "Digestive Health Issues: Seeking Expert Opinions",
                "content": "I've been experiencing digestive health issues lately, and it's causing discomfort. Seeking advice from gastroenterologists or doctors on potential causes, dietary recommendations, and when I should consider seeking professional medical help for a thorough evaluation.",
                "published": 'true',
                "id": 1,
                "created_at": TEMP_DATETIME,
                "owner_id": 2,
                "image_link": shuffled_image[5],
                "owner": {
                    "id": 2,
                    "email": TEMP_EMAIL,
                    "created_at": TEMP_DATETIME
                }
            },
            "votes": 0,
            "replies": [
                {
                    "post_id": 1,
                    "content": "I'm sorry to hear that you're dealing with digestive health issues. While I'm not a doctor, I can offer some general suggestions. It's advisable to consult with a gastroenterologist for a personalized assessment. In the meantime, consider keeping a food diary to identify potential triggers, prioritize a balanced and easily digestible diet, and stay hydrated.",
                    "created_at": TEMP_DATETIME
                }
            ]
        }
    ]


def cards():
    cards = [
        {
            "period": "Today",
            "value": (1415 + random.randint(-105, 105)),
            "percentage": (10 + random.randint(-8, 8)),
        },
        {
            "period": "This Month",
            "value": f"R{(1455 + random.randint(-500, 500))}",
            "percentage": (10 + random.randint(-8, 8)),
        },
        {
            "period": "This Year",
            "value": (1245 + random.randint(10, 50)),
            "percentage": (10 + random.randint(-8, 8)),
        },
    ]

    random.shuffle(cards)

    return cards


def recent_activity():
    recent_activity = [
        {
            "time": f"{random.randint(2, 9)} mins ago",
            "badge": "text-success",
            "type": "update",
            "link": "#",
            "text": "Posted a new update on the feed",
        },
        {
            "time": f"{random.randint(2, 9)} mins ago",
            "badge": "text-danger",
            "type": "consultation",
            "link": "#",
            "text": "Had a consultation with Dr. Smith",
        },
        {
            "time": f"{random.randint(4, 9)} mins ago",
            "badge": "text-primary",
            "type": "health tip",
            "link": "#",
            "text": "Shared a health tip on the feed",
        },
        {
            "time": f"{random.randint(2, 6)} mins ago",
            "badge": "text-info",
            "type": "follow-up consultation",
            "link": "#",
            "text": "Scheduled a follow-up consultation",
        },
        {
            "time": f"{random.randint(5, 9)} mins ago",
            "badge": "text-warning",
            "type": "disease post",
            "link": "#",
            "text": "Liked a disease post on the feed",
        },
        {
            "time": f"{random.randint(2, 9)} mins ago",
            "badge": "text-muted",
            "type": "virtual consultation",
            "link": "#",
            "text": "Attended a virtual consultation",
        },
        {
            "time": f"{random.randint(2, 9)} mins ago",
            "badge": "text-success",
            "type": "update",
            "link": "#",
            "text": "Posted another update on the feed",
        },
        {
            "time": f"{random.randint(1, 8)} mins ago",
            "badge": "text-warning",
            "type": "discussion",
            "link": "#",
            "text": "Participated in a discussion",
        },
        {
            "time": f"{random.randint(3, 6)} mins ago",
            "badge": "text-info",
            "type": "tip",
            "link": "#",
            "text": "Shared a useful tip",
        },
        {
            "time": f"{random.randint(2, 8)} mins ago",
            "badge": "text-muted",
            "type": "webinar",
            "link": "#",
            "text": "Joined a medical webinar",
        }
    ]
    
    processed_activities = []
    for activity in recent_activity:
        text_parts = activity["text"].split(" ")
        text_b = " ".join(text_parts[:-2])
        type_verb = text_parts[-2]
        text_a = text_parts[-1]

        processed_activity = {
            "time": activity["time"],
            "badge": activity["badge"],
            "type": activity["type"],
            "link": activity["link"],
            "text_b": text_b,
            "type_verb": type_verb,
            "text_a": text_a,
        }

        processed_activities.append(processed_activity)

    random.shuffle(processed_activities)

    return processed_activities


def top_selling_medication():
    random_number = random.randint(30, 50)
    top_selling_medication = [
        {
            "preview": "https://media.biogen.co.za/wp-content/uploads/6009544945475-multi-vitamin-50plus-advanced-value-pack.jpg",
            "product": {
                "name": "Vitamin Supplements",
                "link": "#",
                "class": "text-primary fw-bold",
            },
            "price": "R64",
            "sold": random_number + 23,
            "revenue": f"R{(random_number + 23) * 64}",
        },
        {
            "preview": "https://www.firstaider.co.za/wp-content/uploads/2021/08/electrical-kit.jpg",
            "product": {
                "name": "First Aid Kit",
                "link": "#",
                "class": "text-primary fw-bold",
            },
            "price": "R46",
            "sold": random_number + 67,
            "revenue": f"R{(random_number + 67) * 46}",
        },
        {
            "preview": "https://www.dischem.co.za/media/catalog/product/cache/41fea429c8575e0d68f148c3fb0cdd35/6/2/62a343f0085e2_8006540339169.jpg",
            "product": {
                "name": "Cough Syrup",
                "link": "#",
                "class": "text-primary fw-bold",
            },
            "price": "R59",
            "sold": random_number + 10,
            "revenue": f"R{(random_number + 10) + 59}",
        },
        {
            "preview": "https://images.apollo247.in/pub/media/catalog/product/c/r/cro0007_1.jpg",
            "product": {
                "name": "Pain Relief Tablets",
                "link": "#",
                "class": "text-primary fw-bold",
            },
            "price": "R32",
            "sold": random_number + 20,
            "revenue": f"R{(random_number + 20) * 32}",
        },
        {
            "preview": "https://www.capricorn-scientific.com/capricorn/product%20pictures/Cell%20Culture%20Reagents/Antibiotics/AAS-B%20Zweitbild.jpg",
            "product": {
                "name": "Antibiotic Solution",
                "link": "#",
                "class": "text-primary fw-bold",
            },
            "price": "R79",
            "sold": random_number + 5,
            "revenue": f"R{(random_number + 5) * 79}",
        },
    ]

    random.shuffle(top_selling_medication)

    return top_selling_medication


def recent_consultations():
    recent_consultations = [
        {
            "consultationId": "#2457",
            "patient": "None",
            "diseasename": "None",
            "consultationCostPrice": "R64",
            "status": "Open",
            "badge": "success"
        },
        {
            "consultationId": "#2147",
            "patient": "None",
            "diseasename": "None",
            "consultationCostPrice": "R47",
            "status": "Pending",
            "badge": "warning"
        },
        {
            "consultationId": "#2049",
            "patient": "None",
            "diseasename": "None",
            "consultationCostPrice": "R147",
            "status": "Open",
            "badge": "success"
        },
        {
            "consultationId": "#2644",
            "patient": "None",
            "diseasename": "None",
            "consultationCostPrice": "R67",
            "status": "Closed",
            "badge": "danger"
        },
        {
            "consultationId": "#2644",
            "patient": "None",
            "diseasename": "None",
            "consultationCostPrice": "R165",
            "status": "Open",
            "badge": "success"
        },
    ]
    
    disease_names = [
        "COVID-19",
        "Malaria",
        "Influenza",
        "Diabetes",
        "Hypertension",
        "Alzheimer's disease",
        "Cancer",
        "Heart disease",
        "Stroke",
        "Osteoporosis",
    ]

    for consultation in recent_consultations:
        consultation["patient"] = " ".join([random.choice(["John", "Jane", "Alice", "Bob", "Eva", "Mike", "Sophie", "Chris", "Olivia", "Daniel"]),
                                        random.choice(["Smith", "Doe", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Davis", "Rodriguez", "Martinez"])])
        
        consultation["diseasename"] = random.choice(disease_names)

    random.shuffle(recent_consultations)

    return recent_consultations


def admin_table():
    return [
        {
            "id": 1,
            "diseasename": "Common Cold",
            "confidence": 75,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Fever", "Runny Nose", "Cough"],
            "no_of_symp": 3,
            "consultation_date": "2023-03-15",
            "status": "closed"
        },
        {
            "id": 2,
            "diseasename": "Flu",
            "confidence": 80,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Fever", "Body Aches", "Fatigue"],
            "no_of_symp": 3,
            "consultation_date": "2023-02-20",
            "status": "active"
        },
        {
            "id": 3,
            "diseasename": "Allergies",
            "confidence": 60,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Sneezing", "Itchy Eyes"],
            "no_of_symp": 2,
            "consultation_date": "2023-04-10",
            "status": "closed"
        },
        {
            "id": 4,
            "diseasename": "COVID-19",
            "confidence": 90,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Fever", "Shortness of Breath", "Loss of Taste"],
            "no_of_symp": 4,
            "consultation_date": "2023-01-05",
            "status": "active"
        },
        {
            "id": 5,
            "diseasename": "Migraine",
            "confidence": 70,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Headache", "Nausea"],
            "no_of_symp": 2,
            "consultation_date": "2023-06-02",
            "status": "closed"
        },
        {
            "id": 6,
            "diseasename": "Stomach Flu",
            "confidence": 85,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Nausea", "Vomiting", "Diarrhea"],
            "no_of_symp": 3,
            "consultation_date": "2023-03-28",
            "status": "active"
        },
        {
            "id": 7,
            "diseasename": "Hay Fever",
            "confidence": 55,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Sneezing", "Runny Nose"],
            "no_of_symp": 2,
            "consultation_date": "2023-07-15",
            "status": "closed"
        },
        {
            "id": 8,
            "diseasename": "Chickenpox",
            "confidence": 80,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Fever", "Itchy Rash"],
            "no_of_symp": 2,
            "consultation_date": "2023-09-10",
            "status": "closed"
        },
        {
            "id": 9,
            "diseasename": "Diabetes",
            "confidence": 65,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Frequent Urination", "Increased Thirst"],
            "no_of_symp": 2,
            "consultation_date": "2023-11-03",
            "status": "active"
        },
        {
            "id": 10,
            "diseasename": "Asthma",
            "confidence": 75,
            "consultdoctor": "DOCTOR",
            "symptoms": ["Shortness of Breath", "Wheezing"],
            "no_of_symp": 2,
            "consultation_date": "2023-08-20",
            "status": "active"
        }
    ]


def admin_card():
    
    return [
        {
            "icon": "bi bi-chat-square-quote",
            "value": 2000,
            "status": {
                "label": "increase",
                "count": 1
            }
        },
        {
            "icon": "bi bi-check-circle",
            "value": 2000,
            "status": {
                "label": "increase",
                "count": 1
            }
        },
        {
            "icon": "bi bi-x-circle",
            "value": 2000,
            "status": {
                "label": "increase",
                "count": 1
            }
        }
    ]