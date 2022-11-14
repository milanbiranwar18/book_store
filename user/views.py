# Create your views here.
import json
import logging
# Create your views here.
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import User

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def user_registration(request):
    """
    Function for registering user
    """
    try:
        data = json.loads(request.body)
        if request.method == 'POST':
            user = User.objects.create_user(first_name=data.get('first_name'), last_name=data.get('last_name'),
                                       username=data.get('username'), password=data.get('password'),
                                       email=data.get('email'), mob_number=data.get('mob_number'),
                                       location=data.get('location'))
            return JsonResponse({'Message': 'User Registered',
                                 'data': {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                                          'username': user.username, 'password': user.password, 'email': user.email,
                                          'mob_number': user.mob_number, 'location': user.location}})
        return JsonResponse({"Message": "Method not allowed"}, status=400)
    except Exception as e:
        logging.error(e)
        return JsonResponse({"message": str(e)}, status=400)


def user_login(request):
    """
    Function for user login
    """
    try:
        data = json.loads(request.body)
        if request.method == 'POST':
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user:
                return JsonResponse({"Message": "login successful"})
            return JsonResponse({"Message": "Invalid Credential"}, status=204)
        return JsonResponse({"Message": "Method not allowed"}, status=400)
    except Exception as e:
        logging.error(e)
        return JsonResponse({"message": str(e)}, status=400)