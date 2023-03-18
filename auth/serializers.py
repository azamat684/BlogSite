from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError({"error": "User doesn't exists!"})
        return super().validate(attrs)
    
    
    def create(self, validated_data):
        username = validated_data.get("username")
        user = User.objects.get(username=username)
        token = Token.objects.create(user=user)
        return token.key
    

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(min_length=6, max_length=128)
    password2 = serializers.CharField(min_length=6, max_length=128)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")
        if password1 != password2:
            raise ValidationError({"error": "Password didn't match!"})
        return super().validate(attrs)

    def create(self, validated_data):
        user = User(
            email = validated_data.get("email"),
            username = validated_data.get("username")
        )
        user.set_password(validated_data.get("password1"))
        user.save()
        return user