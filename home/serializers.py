from django.db.models import fields
from rest_framework import serializers
from .models import User
from .models import Home
# Create your models here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
