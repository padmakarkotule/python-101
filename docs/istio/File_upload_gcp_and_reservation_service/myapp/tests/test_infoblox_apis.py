import json

import requests

# URL to test
URL = 'http://127.0.0.1:8000/api'

#Roles: can be Manager, User or Infoblox Admin
ROLE = 'Manager'

def test_networks_api_status_code():
    response = requests.get(URL+"/network?role="+ROLE)
    assert response.status_code == 200

def test_ip_status_api_status_code():
    response = requests.get(URL+"/ip_status?role="+ROLE+"&network=192.167.43.0/24")
    assert response.status_code == 200

def test_reserved_ip_list():
    response = requests.get(URL+"/reserve/list?role="+ROLE)
    assert response.status_code == 200

def test_reserved_ip_list_wrong_role():
    response = requests.get(URL+"/reserve/list?role="+ROLE)
    assert response.status_code == 200

def test_reserve_ip():
    request_body = {"ip":["192.167.43.45", "192.167.43.46", "192.167.43.47"], "userid":"5ea02622507c63fe614c02fc"}
    response = requests.post(URL+"/reserve/new?role="+ROLE, json=request_body)
    assert response.status_code == 201

def test_release_ip():
    request_body = {"ip":["192.167.43.45", "192.167.43.46", "192.167.43.47"], "userid":"5ea02622507c63fe614c02fc"}
    response = requests.delete(URL+"/release?role="+ROLE, json=request_body)
    assert response.status_code == 200

def test_reserve_ip_wrong_role():
    request_body = {"ip":["192.167.43.45", "192.167.43.46", "192.167.43.47"], "userid":"5ea02622507c63fe614c02fc"}
    response = requests.post(URL+"/reserve/new?role="+ROLE, json=request_body)
    assert response.status_code == 201

def test_release_ip_wrong_role():
    request_body = {"ip":["192.167.43.45", "192.167.43.46", "192.167.43.47"], "userid":"5ea02622507c63fe614c02fc"}
    response = requests.delete(URL+"/release?role="+ROLE, json=request_body)
    assert response.status_code == 200

def test_reserve_ip_atleast_one():
    request_body = {"ip":["192.167.43.45", "192.167.43.46", "192.167.43.47"], "userid":"5ea02622507c63fe614c02fc"}
    response = requests.post(URL+"/reserve/new?role="+ROLE, json=request_body)
    assert response.status_code == 201
