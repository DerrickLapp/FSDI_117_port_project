from django.shortcuts import render
from .models import Project, Experience

# Create your views here.
def projects_list_view(request):

    projects = Project.objects.all().order_by('-year')

    return render(request, "projects/list.html", {"projects": projects})

def exp_list_view(request):

    experience = Experience.objects.all().order_by('-end_date')

    return render(request, "projects/exp.html", {"exp": experience})