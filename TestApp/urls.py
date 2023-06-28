from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>/', views.ItemDetail.as_view()),
    #path('OcrView/', views.OcrView.as_view()),
    path('FileUploadView/', views.FileUploadView.as_view()),
]