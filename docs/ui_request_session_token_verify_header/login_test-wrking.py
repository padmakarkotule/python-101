from requests import Request, Session
import requests
from requests.auth import HTTPBasicAuth
import json
from django.middleware.csrf import get_token
from requests import request, session

#url = "http://localhost:8051/login_user/"
username = 'user1'
password = 'Pass4321'
url = "http://localhost:5001/"
formdata = {'username':username, 'password':password}
#auth = HTTPBasicAuth(username, password)
#url = "http://localhost:8051/login_user/"
#client = requests.session()
# Retrieve the CSRF token first
#csrf = client.get(url).headers.get('name')
#print("ddd",csrf)


r = requests.get(url, verify=False)
print("\n--url-home--headers-", r.headers)
url = "http://localhost:5001/auth_login/"

try:
    r = requests.post(url=url, data=formdata)
    #print("Return status -", r.status_code)
except:
    r.status_code
    #print("Return Error --", r.status_code)

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

data = r.json()
data_uid = data['uid']
data_user = data['user']

url = "http://localhost:5001/"
r = requests.get(url, verify=False)
print("\n--url-home--text-", r.text)
print("\n--user, uid-", data_user, data_uid)

#print("set cookie values -", r.cookies)
#print("\n Headers values -", r.headers)
#data = r.json
#data_uid = data['uid']
#data_user = data['user']

#print("\n--uid - after accessing other url",data_uid)
#print("\n--user - after accessing other url",data_user)


"""
try:
    r = requests.post(url=url, data=data)
    print("return status ",r.status_code, r.text)
    #requests.sessions.Session.close()
except:
    r.status_code

if r:
    data = json.loads(r.text)
    print ("data received", type(data))
    uid = data['uid']
    print("---Returned Username as -- ", uid)
    print("session", )

del r.session
data = json.loads(r.text)
print ("data received", type(data))
uid = data['uid']
r.close()

print("---uid-", uid)

s = Session()
req = Request('POST', url=url, data=data, headers=headers, verify=False)
prepped = req.prepare()
resp = s.send(prepped)

if resp:
    print(resp.status_code)
    data = json.loads(resp.text)
    print("data received", type(data))
    uid = data['uid']
    print("---data--", data)

data = json.loads(resp.text)
print ("data received", type(data))
uid = data['uid']
print("--should -uid--",uid)

#requests.session.modified = True
url = "http://localhost:8051/logout_user/"
req = Request('POST', url=url)
prepped = req.prepare()
resp = s.send(prepped)

s.delete(url)
s.close()

print("---delete - uid--", uid, s.verify)
print("resp--",resp.text)
"""