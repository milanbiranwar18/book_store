import logging

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response

from user.models import User

logging.basicConfig(filename="serializer.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'mob_number', 'location']

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        try:
            return User.objects.create_user(**validated_data)
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)})


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if not user:
            raise Exception('Invalid credentials')
        return user
