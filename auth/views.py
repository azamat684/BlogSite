from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_201_CREATED



class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"username": user.username}, status=HTTP_201_CREATED)


class LoginUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response({"key": data})
    

class LogOutUserAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out!"})

