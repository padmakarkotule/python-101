import requests
import json
URL = 'http://127.0.0.1:8000/api/users'

def test_get_users():
    response = requests.get(URL)
    # print(response.content)
    assert response.status_code == 200

def test_post_and_delete_users():
    data = {"role_name": "test1","username": "usrasd1"}
    response = requests.post(URL, json=data)
    assert response.status_code == 201
    json_resp = json.loads(response.content)
    print(json_resp)
    del_response = requests.delete(URL+"/"+json_resp['_id'])
    assert del_response.status_code == 200

def test_without_role_or_username():
    data = {"role_name": "test1"}
    response = requests.post(URL, json=data)
    assert response.status_code == 422
    data2 = {"username": "usrasd1"}
    response = requests.post(URL, json=data2)
    assert response.status_code == 422

def test_with_existing_username_or_non_existing_role():
    data = {"role_name": "test1", 'username': 'ykate'}
    response = requests.post(URL, json=data)
    assert response.status_code == 422
    data2 = {"username": "usrasd1", "role_name": "aswert"}
    response = requests.post(URL, json=data2)
    assert response.status_code == 422

def test_wrong_username_role():
    data = {"role_name": "test1", 'username': 'yka'}
    response = requests.post(URL, json=data)
    assert response.status_code == 422
    data2 = {"username": "usrasd1", "role_name": "qwe"}
    response = requests.post(URL, json=data2)
    assert response.status_code == 422