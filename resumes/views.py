from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .models import Resume

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  
            resume.save()
            return redirect('dashboard')
    else:
        form = ResumeForm()
    return render(request, 'resumes/upload.html', {'form': form})

@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user) 
    return render(request, 'resumes/dashboard.html', {'resumes': resumes})
