import requests
from behave import given, then

API_KEY = "regres-free-v1"
# Set up headers with the API key
HEADERS = {"x-api-key": API_KEY}

# Step definition to send a GET request with API key in headers
@given('I send a Get request to "{url}" with api key')
def step_send_get_request_with_api_key(context, url):
    context.response = requests.get(url, headers=HEADERS)       
    #print reponse body in a console
    print("\n==== Response Body ====")
    print(context.response.text)
    
# Step definition to check the response status code should be 200
@then('the response status code should be {status_code:d}')
def step_check_response_status_code(context, status_code):
    #Assert that the API returned the expected status code
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, but got {context.response.status_code}"