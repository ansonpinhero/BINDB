from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('check_benign/', views.check_benign),
    path('check_malware/', views.check_malware),
    path('export/malware_data',views.export_malware_files),
    path('export/benign_data',views.export_benign_files),
    
    
]