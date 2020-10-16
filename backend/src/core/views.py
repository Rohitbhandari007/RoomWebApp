from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post


#third party imports
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

#POST API
class PostView(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)


class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all

    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)



class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
      qs = Post.objects.all()
      serializer = PostSerializer(qs, many=True)
      return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })