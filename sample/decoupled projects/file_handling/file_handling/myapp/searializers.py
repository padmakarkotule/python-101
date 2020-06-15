from rest_framework import serializers

from myapp.models import Roles, Users, File


class RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

