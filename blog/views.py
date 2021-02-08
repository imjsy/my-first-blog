from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class TestView(APIView):

    def get(self, request):

        if request.query_params.get('a'):
            a = int(request.query_params.get('a'))
            b = int(request.query_params.get('b'))

            a = a * b
        else:
            a = 2

        return JsonResponse(dict(
            status='OK',
            message='SUCCESS',
            data=str(a)
        ))
