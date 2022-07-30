import stat
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as stus

from .helpers import genrateRandom, genrateRandomWithLength

from .serializer import RandomGenratorSerializer


@api_view(['GET'])
def randomGenrator(request):
    """_summary_
        This gives a random generated password of the random length
    Args:
        request

    Returns:
        Response: Randomly Generated Password
    """
    password = genrateRandom()
    data = {
        'password': password
    }
    return Response({"data": data, "message": f"Successfully Generated Random Password"}, status=stus.HTTP_200_OK)


@api_view(['GET'])
def randomGenratorWithLength(request):
    """_summary_
        This gives a random generated password of the given length
    Args:
        request

    Returns:
        Response: Randomly Generated Password
    """
    serializedData = RandomGenratorSerializer(data=request.data)
    if serializedData.is_valid():
        length = int(serializedData.data['Length'])
        password = genrateRandomWithLength(length)
        data = {
            'password': password
        }
        return Response({"data": data, "message": f"Successfully Generated Random Password of {length} characters"}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)
