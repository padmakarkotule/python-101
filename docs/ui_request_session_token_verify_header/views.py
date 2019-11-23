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

# Modules used for Image upload (PIL, *PIL is deprecated so use Pillow

# Modules use to copy InMemoryUploadedFile to Disk
from .services import FileUpload


def homepage(request):
    jwt_toke = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
    L = [10, 20.3, "test", 'harshal@test.com', ([25,36],222),('abc', 30, "Ajinath")]
    T = ('touple', 12)
    jwt_token = {'jwt_token':jwt_toke, 'data': L, 'T':T}
    return render(request, 'ui/home/home.html', {'jwt_token': jwt_token})


# Using form
def fbapi_uf_list(request):
    form = UserForm()
    if request.method == "GET":
        if form.is_valid():
            username = form.cleaned_data['username']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            data = {
                "username": username,
                "contact": contact,
                "email": email,
            }
        else:
            return render(request, '500.html', {'error': status})
    else:
        #return render(request, 'ui/enquiry/enquiry.html', {'form': form})
        return render(request, 'ui/home/home.html', {'form': form})



# Using form
@api_view(['GET','POST'])
def fbapi_uf_new(request):
    # Post data and redirect to home page after successful call.
    form = UserForm
    if request.method == "POST":
        form = form(request.POST, request.FILES)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            formdata = form.cleaned_data
            #file = request.FILES['file']

            # File upload
            # Write uploaded file **   # IMP
            """
            file = request.FILES['filename']
            file.name  # Gives name
            file.content_type  # Gives Content type text/html etc
            file.size  # Gives file's size in byte
            file.read()  # Reads file
            """
            file_name = ''
            file_data = ''
            file_content_type = ''
            file_size = ''
            if formdata['upload_image']:
                file_name = form.cleaned_data['upload_image'].name
                file_data = form.cleaned_data['upload_image'].read()
                file_content_type = form.cleaned_data['upload_image'].content_type
                file_size = form.cleaned_data['upload_image'].size

            print("---File data --", file_name, file_content_type, file_size, type(formdata['upload_image']), type(file_data))
            def handle_uploaded_file(f_name, f_data):
                #complete_file_path = os.path.join(save_path, file_name)
                p = settings.STATIC_ROOT
                with open(os.path.join(p,file_name), 'wb+') as destination:
                    #with open(file_name, 'wb+') as destination:
                    #destination.write(file_data)
                    destination.write(file_data)

            # Call handle to upload file
            if file_name:
                    handle_uploaded_file(file_name, file_data)

            data = {
                'username': formdata['username'],
                'password': formdata['password'],
                'time': formdata['time']
            }
            print("---data - ", type(data), data)
            return render(request, 'ui/fbapi2/fbapi_uf_list.html', {'data':data, 'formdata': formdata, 'file':file_name})
                #return render(request, 'ui/fbapi/fbapi_list.html')
                #return redirect('/fbapi_uf/list/')
            #else:
            #   return render(request,'500.html', {'error': r.status_code})
        else:
            # Following commented exmaple returns error data in dic.
            # return render(request,'500.html', {'error':form.errors.as_data()})
            # Following commented exmaple returns error data in json
            # Returns the errors as a dictionary suitable for serializing to JSON. Form.errors.as_json()
            # returns serialized JSON, while this returns the error data before it’s serialized.
            return render(request, '500.html', {'error': form.errors.as_json()})
    else:
        #return render(request, 'ui/fbapi/fbapi_new.html', {'form': form})
        return render(request, 'ui/fbapi2/fbapi_uf_new.html', {'form': form})

