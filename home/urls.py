from django.urls import path
from . import views
urlpatterns = [
    path('upload', views.UploadView.as_view(), name='uploadfile'),
    path('order', views.OrderView.as_view(), name='order_view'),
]