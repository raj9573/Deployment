from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import ResponseSerializer

class Test(APIView):
    
    def get(self,request):

        data = {
            "error": False,
            "message": "Success"
        }
        serializer = ResponseSerializer(data)

        return Response(serializer.data)

