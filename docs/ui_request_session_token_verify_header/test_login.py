from requests import Request, Session, request, session
import requests
from requests.auth import HTTPBasicAuth
import json
#from django.middleware.csrf import get_token


url = "http://localhost:5002/auth_login/"
username = 'user2'
#username = '7774005057'
#username = 'dladmin'
#username = 'admin'
password = 'Pass4321'
formdata = {'username':username, 'password':password}
#r = ''

def check_authentication(URL):
    #response = requests.get(url)
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
print("-- Type of data", type(resp))
resp_username = resp['data']['username']

resp_status = resp['status_code']
if resp_status == 200:
    resp_msg = resp['data']['log_msg']
else:
    resp_msg = resp['data']['error_msg']
resp_url = resp['url']
#print("-- Received data", resp, "\n-- Username --",username)
print("\n-- Username --",resp_username, "\n-- log_msg --", resp_msg, "\n-- Status code --", resp_status, "\n-- url --", resp_url)


"""
try:
    resp = requests.post(url=url, data=formdata)
    print("Return status -", r.status_code)
    print("\n--url-home--auth_login--headers--", r.headers)
    print("\n--url-home--auth_login--coockies--", r.cookies)
    print("\n--url-home--auth_login--apparent_encoding--", r.apparent_encoding)
    print("\n--url-home--auth_login--content--", r.content)
    print("\n--url-home--auth_login--iter_content--", r.iter_content())
    print("\n--url-home--auth_login--text--", r.text)
    print("\n--url-home--auth_login--json--", r.json())
    print("\n--url-home--auth_login--status_code--", r.status_code)
    #print ("\n--r.text--",r.text )
except requests.exceptions.HTTPError as e:
    r = requests.post(url=url, data=formdata)
    #r = None
    #r.status_code
    print("-- Error in login")
    print("Error", r.text)

 
if r:
    print("\n--url-home--auth_login--headers--", r.headers)
    print("\n--url-home--auth_login--coockies--", r.cookies)
    print("\n--url-home--auth_login--apparent_encoding--", r.apparent_encoding)
    print("\n--url-home--auth_login--content--", r.content)
    print("\n--url-home--auth_login--iter_content--", r.iter_content())
    print("\n--url-home--auth_login--text--", r.text)
    print("\n--url-home--auth_login--json--", r.json())
    print("\n--url-home--auth_login--status_code--", r.status_code)
    #print ("\n--r.text--",r.text )

    #Dump into json
    data = r.text
    print("\n--url-home--auth_login--text--", r.text)
    print("\n--url-home--auth_login--r.text type--", type(r.text))
    data_json = json.loads(data)
    print("\n--url-home--auth_login--data(in text after json.loads)--", data_json)

    data = r.json()
    data_uid = data['uid']
    data_user = data['user']
    print("\n--url-home--auth_login--r.json type--", type(r.json()))
    print("\n--url-home--auth_login--data['uid']--", data_uid)
    print("\n--url-home--auth_login--data['user']--", data_user)
    #r.close()
else:
    print("Error", r.text)

"""