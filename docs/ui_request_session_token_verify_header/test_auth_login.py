from requests import Request, Session, request, session
import requests
from requests.auth import HTTPBasicAuth
import json
#from django.middleware.csrf import get_token


url = "http://localhost:5001/accounts/login/"
#url = "http://localhost:5002/auth_login/"
#username = '7774005057'
username = 'dladmin'
#username = 'admin'
password = 'Pass4321'
formdata = {'username':username, 'password':password}

def check_authentication(URL):
    #response = requests.get(url)
    #response = requests.post(url)
    response = requests.post(url, data=formdata)
    #print("------First time execution", response.json(), response.status_code)
    try:
        response.raise_for_status()
        # Must have been a 200 status code
        #json_obj = response.json()
        json_obj = {'data': response.json(), 'status_code': response.status_code, 'url':url}
        #print("--Return response --", json_obj)
        return json_obj
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        #print("--Type of e --", type(e))
        #json_obj = {'data':response.json(), 'status_code': response.status_code, 'http_error_msg':e}
        json_obj = {'data': response.json(), 'status_code': response.status_code, 'url':url}
        #print("--Return response --", json_obj)
        return json_obj
        #eturn e
        #return "Error: " + str(e)

resp = check_authentication(url)
print("-- Type of data", type(resp), resp)
#resp_username = resp['data']['username']
#resp_status = resp['status_code']
#print("\n-- Status code --", resp_status)