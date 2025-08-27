from django.db import models
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .pdf, .doc, .docx allowed.')

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    file = models.FileField(upload_to='resumes/', validators=[validate_file_extension])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')  # Add this

    def __str__(self):
        return f"{self.name}'s Resume"
