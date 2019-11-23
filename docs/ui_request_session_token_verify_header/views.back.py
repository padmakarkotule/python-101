from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import UserForm
import json
from django.contrib import messages
#from django import template
import os.path
from django.conf import settings
from requests import Request, Session
import requests
# Create your views here.


def homepage(request):
    jwt_toke = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
    L = [10, 20.3, "test", 'harshal@test.com', ([25,36],222),('abc', 30, "Ajinath")]
    T = ('touple', 12)
    jwt_token = {'jwt_token':jwt_toke, 'data': L, 'T':T}
    return render(request, 'ui/home/home.html', {'jwt_token': jwt_token})

"""
def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            # query_json = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
            # jwt_token = json.dumps(query_json)

            # Get logged in user i.e. uid
            uid = form.cleaned_data['username']

            #@register.filter
            def get_profile_image(uid):
                # User images path
                STATIC_ROOT = settings.STATIC_ROOT
                path_sep = "\\" + 'images' + "\\" + 'uid_{}'.format(uid) + "\\"
                path_sep1 = "\\" + 'images' + "\\" + 'images_product' + "\\"
                #print("ssss", STATIC_ROOT)
                folder_path = STATIC_ROOT + path_sep
                file = folder_path + 'uid_{}.jpg'.format(uid)
                #default_file = folder_path + 'blank-profile-picture.png'
                if os.path.exists(file):
                    image_path = path_sep + 'uid_{}.jpg'.format(uid)
                    #image_path = image_folder + 'uid_{}.jpg'.format(uid)
                    return image_path
                else:
                    default_image_path = path_sep1 + 'blank-profile-picture.png'
                    return default_image_path

            profile_image = get_profile_image(uid)

            # uid = 'paddy'
            gid = 'staff'
            token = get_token()
            message = 'Login Success !'

            payload = {'uid': uid, 'gid': gid, 'token': token, 'message': message, 'profile_image': profile_image}
            # print(payload)

            jwt_token = payload['token']
            # print(jwt_token)
            request.session['jwt_token'] = payload['token']
            request.session['uid'] = payload['uid']
            request.session['profile_image'] = payload['profile_image']
            request.session['gid'] = payload['gid']
            request.session['message'] = payload['message']

            if jwt_token:
                #return render(request, 'ui/home/home.html', {'message': payload, 'jwt_token': jwt_token})
                return redirect('enquiry')
            else:
                return render(request,'500.html', {'error' : "System error, token not generated."})
    else:
        return render(request, 'ui/iam/loginform.html', {'form': form})


def user_logout(request):
    try:
        del request.session['jwt_token']
        del request.session['uid']
        del request.session['gid']
        del request.session['profile_image']
        del request.session['message']
        #del request.session['token']
        #del request.session['uid']
        #del request.session['gid']

    except:
        pass
    #return HttpResponse("<strong>You are logged out.</strong>")
    return render(request, 'ui/iam/logout.html')


def user_signup(request):
    return render(request, 'ui/iam/signup.html')
"""

def enquiry(request):
    try:
        #header = get_header(request)
        #jwt_token = header['token']
        jwt_token = request.session['jwt_token']
    except:
        return redirect('login')

    if jwt_token is not None:
        pp = request.session['profile_image']
        data = {'fname': "Padmakar", 'lname':'Kotule', 'gid': "staff", 'token':jwt_token, 'profile_image':pp}
        return render(request, 'ui/enquiry/enquiry.html', {'data': data})


def get_token():
    jwt_token = "1234@ddds"
    return jwt_token


@api_view(['GET','POST'])
def fbapi_new(request):
    url_restbe_service = 'http://localhost:8026/fbapi/new/'

    """
    # Get method
    # r = requests.get(url=url_service_apiexample)

    # POST method
    r = requests.post(url=url_service_apiexample, data=data)
    #print("---Status code --",r.status_code)
    #if r.status_code == requests.codes.ok:
    if r.status_code == 201:
        #print("---Content Type--",r.headers['content-type'])
        #data = r.json()
        #return render(request, 'ui/enquiry/enquiry.html', {'data': data})
        return render(request, 'ui/enquiry/enquiry.html')
    else:
        return render(request, '500.html', {'error': r.status_code})
    """

    """
    Example with form
    """

    # Post data and redirect to home page after successful call.
    #form = LoginForm()
    if request.method == "POST":
        #form = LoginForm(request.POST)
        #if form.is_valid():
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            # query_json = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
            # jwt_token = json.dumps(query_json)

            # Get logged in user i.e. uid
        #    uid = form.cleaned_data['username']
            #data = {
            #    "contact": "9823123226",
            #    "email": "user1@gmail.com",
            #    "id": 9,
            #    "username": 'user1'
            #}

            reqdata = request.data
            print("---Type of reqdata", type(reqdata), reqdata)
            d= json.dumps(reqdata)
            print("---d", d)
            #data = {'username':d[-1], 'email':d[-2]}
            data = json.loads(d)
            print("---data", data)
            """
            data = {
                "contact": "9823123226",
                "email": "user1@gmail.com",
                "id": 9,
                "username": 'user1'
            }
            """

            #data1.append(reqdata)
            #print("----data1--", data1)
            #data2 = reqdata.json()
            #print("\n----data2--\n", data2)
            #r = reqdata.json()
            #data.append(r)
            #dataa = rr.json()
            #print("----updataed data", dataa)
            """
            data = {
                "contact": "9823123226",
                "email": "user1@gmail.com",
                "id": 9,
                "username": 'user1'
            }
            """
            #data.append(reqdata)
            r = requests.post(url=url_restbe_service, data=data)
            if r.status_code == 201:
                #return render(request, 'ui/fbapi/fbapi_list.html')
                return redirect('/fbapi/list/')
            else:
                return render(request,'500.html', {'error' : "System error, token not generated."})
    else:
        #return render(request, 'ui/fbapi/fbapi_new.html', {'form': form})
        return render(request, 'ui/fbapi/fbapi_new.html')



def fbapi_list(request):
    url_service_apiexample = 'http://localhost:8026/fbapi/list/'
    # GET Data and display on page.
    if request.method == "GET":
        r = requests.get(url=url_service_apiexample)
        if r.status_code == requests.codes.ok:
            data = r.json()
            return render(request, 'ui/fbapi/fbapi_list.html', {'data': data})
        else:
            return render(request, '500.html', {'error': r.status_code})
    else:
        #return render(request, 'ui/enquiry/enquiry.html', {'form': form})
        return render(request, 'ui/home/home.html', {'form': form})


# Using form
def fbapi_uf_list(request):
    """
    url_service_apiexample = 'http://localhost:8026/fbapi2/list/'
    # GET Data and display on page.
    if request.method == "GET":
        r = requests.get(url=url_service_apiexample)
        if r.status_code == requests.codes.ok:
            data = r.json()
            print("----data type", type(data), data)
            return render(request, 'ui/fbapi/fbapi_uf_list.html', {'data': data})
    """
    form = UserForm()
    if request.method == "POST":
        form = form.UForm(request.POST)
        # form = form(request.POST)
        if form.is_valid():
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            # query_json = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
            # jwt_token = json.dumps(query_json)

            # Get logged in user i.e. uid
            id = form.cleaned_data['id']
            username = form.cleaned_data['username']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            data = {
                "id": id,
                "username": username,
                "contact": contact,
                "email": email,
            }


    # GET Data and display on page.
        else:
            return render(request, '500.html', {'error': r.status_code})
    else:
        #return render(request, 'ui/enquiry/enquiry.html', {'form': form})
        return render(request, 'ui/home/home.html', {'form': form})



# Using form
@api_view(['GET','POST'])
def fbapi_uf_new(request):
    url_restbe_service = 'http://localhost:8026/fbapi2/new/'

    """
    # Get method
    # r = requests.get(url=url_service_apiexample)

    # POST method
    r = requests.post(url=url_service_apiexample, data=data)
    #print("---Status code --",r.status_code)
    #if r.status_code == requests.codes.ok:
    if r.status_code == 201:
        #print("---Content Type--",r.headers['content-type'])
        #data = r.json()
        #return render(request, 'ui/enquiry/enquiry.html', {'data': data})
        return render(request, 'ui/enquiry/enquiry.html')
    else:
        return render(request, '500.html', {'error': r.status_code})
    """

    """
    Example with form
    """

    # Post data and redirect to home page after successful call.
    form = UserForm()

    if request.method == "POST":
        form = form.UForm(request.POST)
        #form = form(request.POST)
        if form.is_valid():
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            # query_json = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
            # jwt_token = json.dumps(query_json)

            # Get logged in user i.e. uid
            id = form.cleaned_data['id']
            username = form.cleaned_data['username']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            data = {
                "id": id,
                "username": username,
                "contact": contact,
                "email": email,
            }

            #reqdata = request.data
            #print("---Type of reqdata", type(reqdata), reqdata)
            print("---data - ", type(data), data)
            #d= json.dumps(reqdata)
            #print("---d", d)
            #data = {'username':d[-1], 'email':d[-2]}
            #data = json.loads(d)
            #print("---data", data)
            """
            data = {
                "contact": "9823123226",
                "email": "user1@gmail.com",
                "id": 9,
                "username": 'user1'
            }
            """

            #data1.append(reqdata)
            #print("----data1--", data1)
            #data2 = reqdata.json()
            #print("\n----data2--\n", data2)
            #r = reqdata.json()
            #data.append(r)
            #dataa = rr.json()
            #print("----updataed data", dataa)
            """
            data = {
                "contact": "9823123226",
                "email": "user1@gmail.com",
                "id": 9,
                "username": 'user1'
            }
            """
            #data.append(reqdata)
            r = requests.post(url=url_restbe_service, data=data)
            if r.status_code == 201:
                #return render(request, 'ui/fbapi/fbapi_list.html')
                return redirect('/fbapi_uf/list/')
            else:
                return render(request,'500.html', {'error': r.status_code})
    else:
        #return render(request, 'ui/fbapi/fbapi_new.html', {'form': form})
        return render(request, 'ui/fbapi2/fbapi_uf_new.html', {'form': form})

