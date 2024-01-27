import random
from datetime import datetime

TEMP_EMAIL = "temp@gmail.com"
TEMP_DATETIME = "Jan 29, 2024"

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
        input_date = datetime.strptime(input_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_date = input_date.strftime("%b %d, %Y")
        return formatted_date
    
    except ValueError:
        return "Jan 1, 2024"


def code_of_conduct():
    return [[
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