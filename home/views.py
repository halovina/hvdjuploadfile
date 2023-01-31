import imp
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home/index.html'
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    
    
class UploadView(TemplateView):
    template_name = 'home/form.html'
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    
    def post(self, *args, **kwargs):
        request_file = self.request.FILES['uploadfile'] if 'uploadfile' in self.request.FILES else None
        if request_file:
            fs = FileSystemStorage()
            file = fs.save(request_file.name, request_file)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            fileurl = fs.url(file)
            messages.success(self.request,"file berhasil di upload")
        return HttpResponseRedirect("/home/upload")
    

class OrderView(TemplateView):
    template_name = 'order/index.html'
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context