from django.urls import path
from . import views
urlpatterns = [
    path('v1/upload-file', views.UploadFileView.as_view(), name='api_uploadfile'),
]