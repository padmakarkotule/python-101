from requests import Request, Session
import requests
from requests.auth import HTTPBasicAuth
import json
from django.middleware.csrf import get_token
from requests import request, session

username = 'user10'
password = 'Pass4321'
url = "http://localhost:5001/auth_login/"
formdata = {'username':username, 'password':password}

#r = requests.get(url, verify=False)
#print("\n--url-home--headers-", r.headers)
#url = "http://localhost:5001/auth_login/"

req = Request('POST', url=url, data=formdata)
prepped = req.prepare()

try:
    resp = requests.post(url=url, data=formdata)
    #print("Return status -", r.status_code)
except:
    resp.status_code
    #print("Return Error --", r.status_code)

if resp:
    print("\n--url-home--auth_login--headers--", resp.headers)
    print("\n--url-home--auth_login--coockies--", resp.cookies)
    print("\n--url-home--auth_login--apparent_encoding--", resp.apparent_encoding)
    print("\n--url-home--auth_login--content--", resp.content)
    print("\n--url-home--auth_login--iter_content--", resp.iter_content())
    print("\n--url-home--auth_login--text--", resp.text)
    print("\n--url-home--auth_login--json--", resp.json())
    print("\n--url-home--auth_login--status_code--", resp.status_code)
    #print ("\n--r.text--",r.text )

    #Dump into json
    data = resp.text
    print("\n--url-home--auth_login--text--", resp.text)
    print("\n--url-home--auth_login--r.text type--", type(resp.text))
    data_json = json.loads(data)
    print("\n--url-home--auth_login--data(in text after json.loads)--", data_json)

    data = resp.json()
    data_uid = data['uid']
    data_user = data['username']

    print("\n--url-home--auth_login--r.json type--", type(resp.json()))
    print("\n--url-home--auth_login--data['uid']--", data_uid)
    print("\n--url-home--auth_login--data['user']--", data_user)
    #r.close()
else:
    print("Error", resp.text)

data = resp.json()
#data_uid = data['uid']
try:
    if request.session['username']:
        data_user = request.session['username']
except:
    data_user = None
#data_user = data['username']

url = "http://localhost:5001/"
resp = requests.get(url, verify=False)
print("\n--url-home--text-", resp.text)
print("\n--user, uid-", data_user)

