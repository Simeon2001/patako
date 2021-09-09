from django.shortcuts import render
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from .serializers import profile_serializer

# Create your views here.
@api_view(['POST'])
def profile_create (request):
    permission_classes = (IsAuthenticated,)
    try:
        if request.method == "POST":
            user = request.user 
            avatar = request.data.get("ava")
            interest = request.data.get("int")
            create = Profile.objects.create(user=user,avatar=avatar,interest=interest)
            return Response(
                {
                    "status": True,
                    "message": "profile created",
                    "data": request.data
                }
            ) 
        else:
            return Response(
                {
                    "status": False,
                    "message": "error : use POST requests",
                    "data": request.data
                }
            ) 
    except:
        return Response(
                {
                    "status": False,
                    "message": "error : you can't create two profile twice",
                    "data": request.data
                }
            ) 

@api_view(['GET'])
def profile_read (request):
    permission_classes = (IsAuthenticated,)
    user = request.user
    read,created = Profile.objects.get_or_create(user=user,interest='in all')
    serializer_class  = profile_serializer(read)
    return Response (serializer_class.data)

def board_post (requests):
    permission_classes = (IsAuthenticated,)
    user = request.user
    profi = Profile.objects.get(user=user)
    
    serializer_class  = profile_serializer(read)
    return Response (serializer_class.data) 