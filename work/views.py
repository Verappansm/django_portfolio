# views.py
from rest_framework import viewsets
from .models import WorkExperience
from .serializers import WorkExperienceSerializer
from django.shortcuts import render
from .models import WorkExperience

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

def work_experience_view(request):
    experiences = WorkExperience.objects.all().order_by('-start_date')
    internships = experiences.filter(experience_type=WorkExperience.INTERNSHIP)
    responsibilities = experiences.filter(experience_type=WorkExperience.RESPONSIBILITY) 
    context = {
        'internships': internships,
        'responsibilities': responsibilities,
    }
    return render(request, 'work/work_experience.html', context)