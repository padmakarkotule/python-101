import json
from requests import Request, Session, request, session
import requests
#from requests.auth import HTTPBasicAuth

#username = '7774005057'
username = 'user2'
password = 'Pass4321'
#role = 'usr'
email = 'user2@gslab.com'
url = "http://localhost:5001/signup/"

#url = "http://localhost:5001/users/"
#formdata = {'username':username, 'password':password, 'email': email, 'role':role}
formdata = {'username':username, 'password':password, 'email': email}

def create_user(url):
    # response = requests.get(url)
    response = requests.post(url, data=formdata)
    #print("------First time execution", response.json(), response.status_code)
    try:
        response.raise_for_status()
        # Must have been a 200 status code
        json_obj = response.json()
        #json_obj = {'data': response.json(), 'status_code': response.status_code, 'url':url}
        #print("--Return response --", json_obj)
        #return json_obj
        return json_obj
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        #print("--Type of e --", type(e))
        #json_obj = {'data':response.json(), 'status_code': response.status_code, 'http_error_msg':e}
        #json_obj = {'data': response.json(), 'status_code': response.status_code, 'url':url}
        #print("--Return response --", json_obj)
        #return json_obj
        #eturn e
        return "Error: " + str(e)

resp = create_user(url)
print("-- Type of data", type(resp), resp)
#resp_username = resp['data']['username']
token = resp['data']['jwt_token']
print("\n--In client type of token (from account service) and Received TOKEN :",type(token), token)
#token = json.dumps(token)

url = "http://localhost:5004/jwt/verify_token/"
#bearer_token = 'Bearer ' + token
bearer_token = token
header = {'Authorization': bearer_token}
#headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization':token}
jwtdata = {'username':username}
def verify_token(url):
    # response = requests.get(url)
    response = requests.post(url, data=jwtdata, headers=header)
    print("\n--Received return status and data from JWT verify token", type(response), response)
    #print("------First time execution", response.json(), response.status_code)
    try:
        response.raise_for_status()
        json_obj = response.json()
        return json_obj
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)


token_verify_resp = verify_token(url)
print("--\nReceived Type of data from JWT verify token:", type(token_verify_resp), token_verify_resp)
print("\n--Msg and type from JWT service verfiy_token", type(token_verify_resp), token_verify_resp)


"""
---Working code using session--
s = Session()
req = Request('POST', url=url, data=formdata)
#req = Request('GET', url=url, data=formdata)

prepped = req.prepare()
#resp = s.send(prepped)
resp = ''
try:
    resp = s.send(prepped)
except:
    resp.status_code
"""