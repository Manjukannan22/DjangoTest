from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from TestApp.models import Item
from .serializers import ItemSerializer


from paddleocr import PaddleOCR
#from pathlib import Path
import os
from django.conf import settings

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    
    
    """def post(self, request):
        file = request.data['file']
        ocr = PaddleOCR()
        result = ocr.ocr(file)
        text = [line[1][0] for line in result]
        return Response({'text': text})"""
        
    def post(self, request):
        file = request.data['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        
        """ocr = PaddleOCR(lang='en')
        output = ocr.ocr(uploaded_file_url)
        text = [line[1][0] for line in output]
        print(text)"""
        print(settings.MEDIA_ROOT)
        print(settings.MEDIA_URL)
        print(settings.MEDIA_ROOT+'\\'+filename)
        #data = ''
        
        file_path = fs.path(filename)
        print(file_path)
        ocr = PaddleOCR(lang='en')
        output = ocr.ocr(file_path)
        text = [line[1][0] for line in output]
        print(text)
        
        """if fs.exists(filename):
            # Open the file
            with fs.open(filename) as file:
                # Read the file content
                #content = file.read()
                #print(content)
                ocr = PaddleOCR(lang='en')
                output = ocr.ocr(file)
                text = [line[1][0] for line in output]
                print(text)"""
        
        
        return Response({'uploaded_file_url': text})
        
"""class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.data['file']
        # handle the uploaded file here
        return Response(status=201)"""
    

        

