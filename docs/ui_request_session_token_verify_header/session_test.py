import json
from requests import Request, Session, request, session
#from requests.auth import HTTPBasicAuth

username = 'admin'
password = 'Pass4321'
url = "http://localhost:5001/auth_login/"
formdata = {'username':username, 'password':password}

s = Session()
req = Request('POST', url=url, data=formdata)
prepped = req.prepare()
resp = s.send(prepped)

data_user = ''
if resp:
    print(resp.status_code)
    data = json.loads(resp.text)
    uid = data['uid']
    data_user = data['username']
else:
    print("--POST-", resp.status_code)

#
data = json.loads(resp.text)
print ("data received, resp.txt", data)

url = "http://localhost:5001/"
req = Request('GET', url=url,)
prepped = s.prepare_request(req)
resp = s.send(prepped)

if resp:
    print(resp.status_code)
    print ("GET data - received, resp.txt", resp.text)
else:
    print(resp.status_code)

print("\n--url-home--text-", resp.text)
print("\n--user, uid-", data_user)