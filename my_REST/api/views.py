from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestResults
from .serializers import Testresultserializer

class TestResult(APIView):

    def get(self,request):
        testresult1 = TestResults.objects.all()
        serializer=Testresultserializer(testresult1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        import pdb;pdb.set_trace()
        serializer = Testresultserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

