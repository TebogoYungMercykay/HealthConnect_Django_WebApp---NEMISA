# RANDOM README
---

- Create an Error log in the root directory and name it: ``` server_healthconnect.log ```
- This is so that all errors can be logged there and we can address them as they occur

- To Run the APP, Use these commands:
    ```bash
    pip install -r requirements.txt
    ```
    ```bash 
    python manage.py runserver
    ```
    - If any error is encountered: Run ``` python manage.py migrate --fake```
    - So that we can fake migrations and be able to store session data for logging purposes

- To send a request to the API Check Example:
    ```python
    request_data = {
        'attr1': 'value1',
        'attr2': 'value2',
    }

    api_url = os.getenv("API_ENDPOINT") + '/router'
                
    request_data = json.dumps(request_data, indent=4, ensure_ascii=False)
    headers = {
        'Content-Type': JSON_DATA,
    }
    
    response = requests.post(api_url, data=request_data, headers=headers)
    response.raise_for_status()
    
    if response.status_code == 200:
        print("Success, Do Something with the Data")
    else:
        print("Error, Fix Error")
    
    ```

---
---

<p align="center">The End, Thank You!</p>