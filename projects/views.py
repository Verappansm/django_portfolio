from django.shortcuts import render
from .models import Project, Patent, Publication

def project_view(request):
    projects = Project.objects.all()
    patents = Patent.objects.all()
    publications = Publication.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects,
        'patents': patents,
        'publications': publications,
    })

