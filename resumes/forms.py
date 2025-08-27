from django import forms
from .models import Resume, validate_file_extension  

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'file']

    file = forms.FileField(validators=[validate_file_extension])
