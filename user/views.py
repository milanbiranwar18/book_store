# Create your views here.
import json
import logging

from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Registration(APIView):
    """
    Class for user Registration
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            if request.method == 'POST':
                user = User.objects.create_user(first_name=data.get('first_name'), last_name=data.get('last_name'),
                                                username=data.get('username'), password=data.get('password'),
                                                email=data.get('email'), mob_number=data.get('mob_number'),
                                                location=data.get('location'))
                return Response({'Message': 'User Registered',
                                 'data': {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                                          'username': user.username, 'password': user.password, 'email': user.email,
                                          'mob_number': user.mob_number, 'location': user.location}})
            return Response({"Message": "Method not allowed"}, status=400)
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)


class Login(APIView):
    """
    Class for user login
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            if request.method == 'POST':
                user = authenticate(username=data.get('username'), password=data.get('password'))
                if user:
                    return Response({"Message": "login successful"})
                return Response({"Message": "Invalid Credential"}, status=204)
            return Response({"Message": "Method not allowed"}, status=400)
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)
