from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET']) #so aceita get
def get_users(request):

    if request.method == "GET":

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)

    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):

    try:
        user = User.objects.get(pk = nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user) #nao usa many pois deve devolver objeto único
        return Response(serializer.data)


#def databaseEmDjango():

#    data = User.objects.get(pk = 'nogsposito') #devolve objeto! (pegando primary key (username))
#    data = User.objects.filter(user_age='18') #devolve queryset, nao objeto! ineditavel
#    data = User.objects.exclude(user_age='18') #todos que NAO tem 18 (também queryset)
#
#    data.save()
#    data.delete()