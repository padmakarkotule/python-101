import sys
import os
from django.conf import settings
from django.conf.urls.static import static

# Class - Used to upload files.
class FileUpload():
    def __init__(self, filename, *args):
        self.filename = filename


    def handle_uploaded_file(self):
        filew = 'static/' + self.filename
        with open(filew, 'wb+') as destination:
            for chunk in self.filename.chunks():
                destination.write(chunk)