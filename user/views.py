# Create your views here.

import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializer import RegistrationSerializer, LoginSerializer

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
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message":"Registered Successfully", "data":serializer.data, "status":201})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)


class Login(APIView):
    """
    Class for user login
    """

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response({"message":"Login Successfully", "status":202})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)
