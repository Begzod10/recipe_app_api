"""
views for user api

"""

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import UserSerializers, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """ create user in system """

    serializer_class = UserSerializers


class CreateTokenView(ObtainAuthToken):
    """ Create a  new auth token """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """ manage the authenticated user """
    serializer_class = UserSerializers
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """ retrieve and return the authenticated user"""
        return self.request.user
