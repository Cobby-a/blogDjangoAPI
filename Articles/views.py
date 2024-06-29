from django.shortcuts import render
from rest_framework import generics, permissions

# from rest_framework import viewsets

from .models import Articles
from .serializers import ArticlesSerializer, UserSerializer

from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

from rest_framework.parsers import MultiPartParser, FormParser


class ArticlesList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    parser_classes = (MultiPartParser, FormParser)

class ArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    parser_classes = (MultiPartParser, FormParser)

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# Create your views here.


#-- Using ViewPoints -- provides both a list view and a detail view for us. And we no longer have to repeat the same queryset and serializer_class for each view

# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAdminUser]
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer