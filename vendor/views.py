from django.shortcuts import render
from rest_framework.views import APIView
from vendor.serializers import LoginSerializers
from rest_framework.response import Response
# Create your views here.
class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)