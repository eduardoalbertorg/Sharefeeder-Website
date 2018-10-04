"""
Serializers allow complex data such as querysets and model instances to be converted to
native Python datatypes that can then be easily rendered into JSON, XML or other content types.
"""

from rest_framework import serializers
from .models import Feeder, Galileo, Credential, User

class FeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeder
        fields = '__all__'

class GalileoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galileo
        fields = '__all__'

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'