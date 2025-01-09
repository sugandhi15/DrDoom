from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import WebUser
from .serializers import WebUserSerializer
import datetime
from django.conf import settings
from rest_framework import status
import jwt
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
import random



class RegisterView(APIView):
    def post(self, request):
        try:
            # signup=signupserializer(request.data)
            # if signup.is_valid
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            phone_number = request.data['phone_number']
            password = request.data['password']
            if not (first_name and last_name and phone_number and email and password):
                return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the email is already registered
            if WebUser.objects.filter(email=email).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            data = {
                "first_name" : first_name,
                "last_name" : last_name,
                "email" : email,
                "phone_number" : phone_number,
                "password" : password
            }
            serilizer = WebUserSerializer(data = data)
            if serilizer.is_valid():
                serilizer.save()
                payload = {
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1), 
                    "iat": datetime.datetime.utcnow(), 
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
                return JsonResponse({
                    "msg":token
                },status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"msg" : "Please enter valid credentials"},status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return JsonResponse({
                "msg" :  "Please enter valid credentials"
            },status=status.HTTP_400_BAD_REQUEST)
        




def generate_otp():
    return str(random.randint(100000, 999999))




class LoginView(APIView):

    def post(self,request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = WebUser.objects.get(email = email)
            if not user:
                return JsonResponse({"error" : "No user exist with this email"})
            if check_password(password,user.password):
                payload = {
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1), 
                    "iat": datetime.datetime.utcnow(), 
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
                response=Response({"jwt_token":token})
                response.set_cookie(key='jwt_token',value=token)
                # resp = f"token = {token}"
                return JsonResponse({
                    "msg":token
                }, status=status.HTTP_200_OK)
            else:
                return JsonResponse({
                "error" : "Please enter valid credentials"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({
                "error" : "Please enter valid credentials"
            }, status=status.HTTP_400_BAD_REQUEST)
        
