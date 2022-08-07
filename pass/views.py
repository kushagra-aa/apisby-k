from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as stus

from .genrators import *

from .serializer import *


@api_view(['GET'])
def randomGenrator(request):
    """_summary_
        This gives a random generated password of the random length
    Args:
        request

    Returns:
        Response: Randomly Generated Password
    """
    password = generateRandom()
    data = {
        'password': password
    }
    return Response({"data": data, "message": f"Successfully Generated Random Password"}, status=stus.HTTP_200_OK)


@api_view(['GET'])
def randomGenratorWithLength(request):
    """_summary_
        This gives a random generated password of the given length
    Args:
        request:
            length

    Returns:
        Response: Randomly Generated Password
    """
    serializedData = RandomGenratorSerializer(data=request.data)
    if serializedData.is_valid():
        length = int(serializedData.data['Length'])
        password = generateRandomWithLength(length)
        data = {
            'password': password
        }
        return Response({"data": data, "message": f"Successfully Generated Random Password of {length} characters"}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)


@api_view(['GET'])
def randomWithArguments(request):
    """_summary_
        This gives a random generated password of the given length
        according to the given arguments.
        Arguments determine the kind of characters in the password
    Args:
        request:
            length, Upper, Lower, Digits, Symbols

    Returns:
        Response: Randomly Generated Password
    """
    serializedData = RandomWithArgumentsSerializer(data=request.data)
    if serializedData.is_valid():
        length = int(serializedData.data['Length'])
        isUpper = int(serializedData.data['Upper'])
        isLower = int(serializedData.data['Lower'])
        isDigit = int(serializedData.data['Digits'])
        isSymbol = int(serializedData.data['Symbols'])
        password = generateRandomWithArguments(
            length, isUpper, isLower, isDigit, isSymbol)
        data = {
            'password': password
        }
        return Response({"data": data, "message": f"Successfully Generated Random Password of {length} characters"}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)


@api_view(['GET'])
def randomWithMinimum(request):
    """_summary_
        This gives a random generated password of the given length
        according to the given arguments.
        Arguments determine that there must be at least one of given characters
    Args:
        request:
            length, Upper, Lower, Digits, Symbols

    Returns:
        Response: Randomly Generated Password
    """
    serializedData = RandomWithMinimumSerializer(data=request.data)
    if serializedData.is_valid():
        length = int(serializedData.data['Length'])
        Upper = int(serializedData.data['Upper'])
        Lower = int(serializedData.data['Lower'])
        Digit = int(serializedData.data['Digits'])
        Symbol = int(serializedData.data['Symbols'])
        password = generateRandomWithMinimum(
            length, Upper, Lower, Digit, Symbol)
        data = {
            'password': password
        }
        return Response({"data": data, "message": f"Successfully Generated Random Password of {length} characters"}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)


@api_view(['GET'])
def randomWithCustom(request):
    """_summary_
        This gives a random generated password of the given length
        according to the given arguments.
        Arguments determine the number of given characters i password
    Args:
        request:
            length, Upper, Lower, Digits, Symbols

    Returns:
        Response: Randomly Generated Password
    """
    serializedData = RandomWithCustomSerializer(data=request.data)
    if serializedData.is_valid():
        length = int(serializedData.data['Length'])
        Upper = int(serializedData.data['Upper'])
        Lower = int(serializedData.data['Lower'])
        Digit = int(serializedData.data['Digits'])
        Symbol = int(serializedData.data['Symbols'])
        password = generateRandomWithCustom(
            length, Upper, Lower, Digit, Symbol)
        data = {
            'password': password
        }
        return Response({"data": data, "message": f"Successfully Generated Random Password of {length} characters"}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)


@api_view(['GET'])
def randomPerfect(request):
    """_summary_
        This gives a random generated password of atleast 2 of each type of character.
    Args:
        request

    Returns:
        Response: Randomly Generated Password
    """
    password = generateRandomPerfect()
    data = {
        'password': password
    }
    return Response({"data": data, "message": f"Successfully Generated Random Password of 10 characters"}, status=stus.HTTP_200_OK)


@api_view(['GET'])
def fromString(request):
    """_summary_
        This gives a random generated password from given string
    Args:
        request:
            string,perfect

    Returns:
        Response: Randomly Generated Password
    """
    serializedData = FromStringSerializer(data=request.data)
    if serializedData.is_valid():
        string = serializedData.data['String']
        isPerfect = serializedData.data['Perfect']
        password = generateFromString(string, isPerfect)
        data = {
            'password': password
        }
        return Response({"data": data, "message": f"Successfully Generated Password from {string}"}, status=stus.HTTP_200_OK)
    else:
        return Response({"data": serializedData.errors}, status=stus.HTTP_300_MULTIPLE_CHOICES)
