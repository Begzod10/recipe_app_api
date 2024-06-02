"""
views for recipe APIs

"""
from django.shortcuts import render
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Recipe, Tag
from .serializer import RecipeSerializer, RecipeDetailSerializer, TagSerializer


# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    """ View for manage recipe APIs """
    serializer_class = RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve recipes for authenticated user """
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """ return the serializer class for request """
        if self.action == "list":
            return RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """ create new recipe """
        serializer.save(user=self.request.user)


class TagViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """ Manage tags in the database. """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ filter queryset to authenticated user """
        return self.queryset.filter(user=self.request.user).order_by('-name')
