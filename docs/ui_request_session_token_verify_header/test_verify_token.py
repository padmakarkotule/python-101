import json
from requests import Request, Session, request, session
import requests
#from requests.auth import HTTPBasicAuth

#username = '7774005057'
username = 'user2'
password = 'Pass4321'
#role = 'usr'
email = 'user2@gslab.com'
url = "http://localhost:5004/jwt/verify_token/"

#url = "http://localhost:5001/users/"
#formdata = {'username':username, 'password':password, 'email': email, 'role':role}
formdata = {'username':username, 'password':password, 'email': email}

token = "'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIyIiwiZ3JvdXBzIjoidXNlcnMiLCJlbWFpbCI6InVzZXIyQGdzbGFiLmNvbSIsImNsaWV\
udF9pZCI6IkNsaWVudF9zZWxmIiwidG9rZW5fdHlwZSI6IkJlYXJlciJ9.xv19fIsLDfKatDTcb752UQfMUztoxLGYu_ZXV_71838'"

def verify_token(url):
    # response = requests.get(url)
    response = requests.post(url, data=token)
    #print("------First time execution", response.json(), response.status_code)
    try:
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

resp = verify_token(url)
print("-- Type of data", type(resp), resp)