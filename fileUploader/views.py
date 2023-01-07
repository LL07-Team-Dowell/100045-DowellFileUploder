from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class FileCreateView(APIView):
    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"info":"File uploaded successfully"}, status=status.HTTP_201_CREATED)
        return Response({"info": "toodles , files are not uploaded successful"}, status=status.HTTP_400_BAD_REQUEST)
    