from django.shortcuts import render
from .models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'home_page': 'active'
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'home_page': 'active'
    }
    return render(request, 'project_details.html', context)