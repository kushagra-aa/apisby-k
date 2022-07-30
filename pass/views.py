import stat
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as stus

from .serializer import TestSerializer


@api_view(['GET'])
def test(request):
    serializedData = TestSerializer(data=request.data)
    if serializedData.is_valid():
        userName = serializedData.data['Name']
        return Response({"data": f'Welcome {userName}!'}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)
