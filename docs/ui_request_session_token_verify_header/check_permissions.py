import json
from requests import Request, Session, request, session
import requests
#from requests.auth import HTTPBasicAuth

username = 'user6'
password = 'Pass4321'
role = 'users'
email = 'user6@gslab.com'
# ---------
group_name = 'users'


#url = "http://localhost:5002/permissions/"
#url = "http://localhost:5002/gateway/"
#url = "http://localhost:5001/user_info/"
url = "http://localhost:5001/check_permission/"
#url = "https://api.github.com/users"

#url = "http://localhost:5001/"
#url = "http://localhost:5001/users/"
formdata = {'username':username, 'password':password, 'email': email, 'role':role, 'group':group_name}
#formdata = {'username':username, 'group_name':group_name}
s = Session()
#req = Request('POST', url=url, data=formdata)
req = Request('POST', url=url, data=formdata)
#req = Request('GET', url=url)
#req = Request('GET', url=url, data=formdata)

prepped = req.prepare()
resp = ''

try:
    resp = s.send(prepped)
except:
    resp.status_code

print("\n--resp status-", resp.status_code)
#print("\n--resp status-", resp.json)
#user_info = resp.json()
#print("-- User info", user_info)

url1 = "https://api.github.com/users"
#resp1 = ''
try:
    #resp1 = Request('GET', url=url)
    resp1 = requests.get(url1)
    print("--",resp1)
except:
    resp1 = None
#print("--------",resp1.json())
# Form field attributes
#self.fields['some_field'].widget.attrs['readonly'] = True
#... and accessing it in a template:
#{{ form.some_field.field.widget.attrs.readonly }}