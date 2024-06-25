from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def user_view(request):
    return Response({'name': 'Viraj Kadam'})