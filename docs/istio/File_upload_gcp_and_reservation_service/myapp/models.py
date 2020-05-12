from django.db import models
from django.core.validators import MinLengthValidator


class Roles(models.Model):
    role_name = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    description = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    username = models.CharField(max_length=20, validators=[MinLengthValidator(5)])
    lastname = models.CharField(max_length=20, blank=True)
    firstname = models.CharField(max_length=20, blank=True)
    role_name = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    groups = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    username=models.CharField(max_length=20)
    def __str__(self):
        return self.file.name