from django.db.models import constraints
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from account.serializers import AccountSerializer
import numpy as np 
from account.models import Account
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.models import Token



def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        data = {}
        args_list = list(request.data.keys())
        entities = ['first_name', 'last_name', 'email', 'username',
                    'password', 'password2']

        non_entered_fields = np.setdiff1d(entities, args_list) 
        if len(non_entered_fields) > 0:
            return Response({"message": "{} is required".format(non_entered_fields[0]),
                            }, status=status.HTTP_404_NOT_FOUND)   


        email = request.data.get('email').lower()

        if validate_email(email) != None :
            data['message'] = 'That email is already in use.'
            data['status'] = 400
            return Response(data)                                     

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully register new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)    


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sample_api(request):
    print(request.user)
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)                          

class ListAccountAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    '''authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]'''
    #filter_backends=[SearchFilter]
    #search_fields=['username']
    #search_fields=['username','email','last_name']
    #search_fields=['^username']
    #search_fields=['=first_name']
    filter_backends =[DjangoFilterBackend]
    filterset_fields=['username']


