from django.shortcuts import render

# Third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Local imports
from .serializers import PostSerializer
from .models import Post


class PostView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
       qs = Post.objects.all()
       serializer = PostSerializer(qs, many=True)
       return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)