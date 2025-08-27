from django.urls import path
from .views import upload_resume, dashboard, register  

urlpatterns = [
    path('upload/', upload_resume, name='upload_resume'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
]
