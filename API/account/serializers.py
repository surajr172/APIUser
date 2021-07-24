from django.db import models
from rest_framework import serializers

from account.models import Account

class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = ['id','email', 'username', 'password', 'password2', 'first_name', 'last_name',]

        extra_kwargs = {
            'password2' : {'wright_only' : True},
        }
    def save(self):
        print(self)
        account = Account(
            email= self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})
        account.set_password(password)
        account.save()
        return account

 