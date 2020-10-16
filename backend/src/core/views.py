from django.shortcuts import render
from django.http import JsonResponse

def test_view(request):
    data = {
        'name':'rohit',
        'age':'20'
    }
    return JsonResponse(data)