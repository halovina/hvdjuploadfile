from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import UploadFileSerializer
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

class UploadFileView(APIView):
    def post(self, *args, **kwargs):
        try:
            data = self.request.data
            serializer = UploadFileSerializer(data=data)
            if serializer.is_valid():
                request_file = data['files']
                fs = FileSystemStorage()
                fs.save(request_file.name, request_file)
                return JsonResponse({
                "message": "data berhasil di upload"
                }, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({
                "message": str(e)
                }, status=400)