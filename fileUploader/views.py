from django.conf import settings
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



@method_decorator(csrf_exempt, name='dispatch')
class FileCreateView(APIView):
    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file_path = serializer.save()
            # create the file URL
            file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
            return Response({'file_url': file_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FileDownloadView(APIView):
    def get(self, request, file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            file = open(file_path, 'rb')
            response = FileResponse(file)
            return response
        else:
            return Response({'error': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)
