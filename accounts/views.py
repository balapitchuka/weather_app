from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from accounts.serializers import RegisterSerializer

# Create your views here.
class SignUpView(APIView):
    """
    Signup view for  new user registration

    Sample body to send:
    {
        "username" : "test_user",
        "password" : "Avengers123@",
        "password2" : "Avengers123@",
        "first_name" : "Jack",
        "last_name" : "Sparrow",
        "email" : "testuser23@gmail.com"
    }
    """
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            # user validation success
            serializer.save()
            data = {
                "message" : "User got Registered successfully"
            }
            return Response(data=data)
        else:
            # user validation failed
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors, status=status_code)
    
