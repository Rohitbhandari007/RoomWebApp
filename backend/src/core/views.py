from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data={
            'name':'rohit',
            'age': '20'
        }
        return Response(data)