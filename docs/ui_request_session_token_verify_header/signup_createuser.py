import json
from requests import Request, Session, request, session
#from requests.auth import HTTPBasicAuth

username = 'user6'
password = 'Pass4321'
#role = 'usr'
email = 'user6@gslab.com'
url = "http://localhost:5001/signup/"

#url = "http://localhost:5001/users/"
#formdata = {'username':username, 'password':password, 'email': email, 'role':role}
formdata = {'username':username, 'password':password, 'email': email}

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

#print("\n--resp status-", resp.status_code, resp.json())
print("\n--resp status-", resp.status_code)

""" 
if resp:
    print(resp.status_code)
    data = resp.json()
else:
    print("--POST--Error", resp.status_code)

print("\n--data type --", type(data))
d1 = data['data']
d2 = d1[0]
print("\n--datatype of d1", type(d1))
print("\n--datatype of d2", type(d2))

print("\n-d1-",d1)
print("\n-d2-username-",d2['username'])
"""