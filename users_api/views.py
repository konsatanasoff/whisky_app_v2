from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users_api.models import UserModel
from users_api.serializers import UserSerializer, LoginSerializer


class UserListView(generics.ListAPIView):
    # def get(self, request):
    #     users = UserModel.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    pass


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


# TODO
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
