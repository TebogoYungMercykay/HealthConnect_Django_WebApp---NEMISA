# HealthConnect Django Application Documentation

![HealthConnect Django Application](./main_app/static/img/about.jpg)

HealthConnect is a revolutionary healthcare platform that transcends traditional boundaries, offering accessible care anytime, anywhere. Our commitment to providing round-the-clock access to caring doctors ensures that you can receive assistance whenever you need it, be it day or night. What sets HealthConnect apart is its personalized healthcare experience, featuring one-on-one video sessions and secure prescriptions tailored to your specific needs. We believe in inclusive communication, delivering diagnosis letters in all South African languages to facilitate clear and understanding conversations between patients and healthcare providers. Through proactive wellness management and sentiment analysis, we prioritize your well-being by staying ahead of potential health issues and addressing concerns before they escalate. HealthConnect is not just a healthcare platform; it's a community-centric approach to well-being. We prioritize your health, ensuring your voice is heard and fostering a sense of community and mutual support among our users. Step into a world where healthcare revolves around you – join HealthConnect today and experience accessible, personalized, and proactive healthcare like never before.

## TECHNOLOGIES USED
- ### Main Application:
    - This is the Application in this Repository
    - **Backend:**
        - Django Web Framework: We chose this for additional backend capabilities and enhanced functionality using the MVC model.
        - FastAPI Integration: Utilizes FastAPI for a singleton connection to the database and all necessary queries as well as Auth.
        - NewsAPI Integration: Utilizes NewsAPI to enrich content and provide up-to-date information.
    - **Frontend:**
        - Python Jinja2 Syntax: Employs Python Jinja2 syntax for dynamic content rendering on the frontend.
        - Bootstrap: Uses Bootstrap, a front-end framework, to ensure a responsive and visually appealing design.
- ### Application Interfaces
    - ##### HealthConnect FastAPI:
        - **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
        - **Unit Testing:** Demonstrates the importance of testing through unit tests for different components of the API.
        - **CI/CD (Docker, Heroku):** Implements continuous integration and deployment using Docker for containerization and Heroku for cloud hosting.
        - **Database Migration Tools (Alembic):** Incorporates Alembic for managing database schema migrations.
        - **Authentication (JWT Tokens):** Implements token-based authentication using JWT (JSON Web Tokens).
        - **Virtual Environment:** Utilizes virtual environments for dependency isolation and management.
        - **Relational Databases (Postgres):** Integrates with Postgres as a relational database to store and manage data.
        - **Uvicorn ASGI Web Server:** Uses Uvicorn as the ASGI (Asynchronous Server Gateway Interface) web server for FastAPI.
        - **GitHub Jobs:** Example routes that demonstrate fetching data from the GitHub Jobs API.
        - **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database interaction.
        - ###### **Link:** [HealthConnect FastAPI](https://github.com/TebogoYungMercykay/Python_API_Development_Booth_FASTAPI)
        - ###### **Documentation:** [Live Documentation](https://healthconnect-python-fastapi-9b23b53a9ae4.herokuapp.com/docs)
    - ##### NewsAPI:
        - **Health Articles:** The News API provides us with access to latest and finest articles about health around the Globe.
        - ###### **Link:** [The NewsAPI](https://newsapi.org)
        - ###### **Documentation:** [Live Documentation](https://newsapi.org/docs)

## PROJECT STRUCTURE

- **`main_app/`:** The main application directory housing core functionalities and modules.
- **`healthconnect_backend/`:** Backend directory containing the Django application, integrating FastAPI and NewsAPI for robust backend operations.
- **`healthconnect_backend/settings.py`:** Configuration file for Django settings, including database configurations, middleware, and other application settings.
- **`main_app/templates/`:** Directory storing HTML templates for the frontend, utilizing Python Jinja2 syntax for dynamic content rendering.
- **`main_app/static/`:** Static files directory containing assets like images, stylesheets, and JavaScript files for the frontend.
- **`root/manage.py`:** Django management script for various project-related tasks, including running the development server, migrations, and more.
- **`requirements.txt`:** File listing all the Python packages and their versions required to run the application, facilitating easy dependency management.
- **`project-diagrams/`:** Directory housing visual representations such as system architecture diagrams, database schemas, or any relevant visualizations to aid in understanding the project's structure.
- **`README.md`:** Comprehensive documentation providing an overview of the project, including setup instructions, deployment guidelines, and any other pertinent information for developers and users alike.

## DATABASE TABLES DESIGN & RELATIONSHIPS

![ERD Diagramn](./project-diagramns/database-erd-diagramn-healthconnect.drawio.svg)

### REQUIREMENTS: Quick Setup/Guidelines for Running the Python API

- ###### Creating the Python Virtual Environment:
    ```markdown
    - sudo apt-get update
    - sudo apt-get install python3-venv
    - python3 -m venv <env_name>

    - pip install virtualenv
    - virtualenv -p python3 <env_name>

    # activating and deactivating virtualenv
    - source <env_name>/bin/activate
    - deactivate
    ```

- ###### Activating the Python Virtual Environment:
    ```markdown
    - source <env_name>/bin/activate
    ```

- ###### Deactivating the Python Virtual Environment:
    ```markdown
    - deactivate
    ```

- ###### Environment Variables:
    ```bash
    # Place the (.env) File in Root Directory
    API_ENDPOINT = 'VAL_API_ENDPOINT'
    TWIILO_ACCOUNT_SID = 'VAL_TWIILO_ACCOUNT_SID'
    TWIILO_AUTH_TOKEN = 'VAL_TWIILO_AUTH_TOKEN'
    TWIILO_MOBILE_NO = 'VAL_TWIILO_MOBILE_NO'
    CHATBOT_ID = 'VAL_CHATBOT_ID'
    API_KEY_NEWSAPI = 'VAL_API_KEY_NEWSAPI'

    EMAIL_PORT = 'VAL_EMAIL_PORT'
    EMAIL_HOST = 'VAL_EMAIL_HOST'
    EMAIL_RECEIVER = 'VAL_EMAIL_RECEIVER'
    EMAIL_HOST_USER = 'VAL_EMAIL_HOST_USER'
    EMAIL_HOST_PASSWORD = 'VAL_EMAIL_HOST_PASSWORD'

    # For Testing Purposes
    PATIENT='PATIENT'
    DOCTOR='DOCTOR'
    ADMIN='ADMIN'
    PASSWORD='PASSWORD'
    ```
---

### Running the Django Application:
- **Clone the Repository:**
   ```bash
   git clone https://github.com/DanPhala/HealthConnect---NEMISA.git
   cd <project_dir>
   ```

- **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

    # Alternatively use the script to avoid some installation errors
    bash requirements_script.sh
    ./requirements_script.sh

    # If you encounter a permission error, you may need to make the script executable. You can do this with the following command:
    chmod +x requirements_script.sh
    ./requirements_script.sh
    ```

- **Run Locally:**
    ```markdown
    python manage.py runserver
    ```

---

### Dataset Used:

https://www.kaggle.com/neelima98/disease-prediction-using-machine-learning


---
---

<p align="center">The End, Thank You!</p>

---