from django.shortcuts import render
from .models import Project, Experience
from .forms import ProjectForm
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

# Create your views here.
def projects_list_view(request):

    projects = Project.objects.all().order_by('-year')

    return render(request, "projects/list.html", {"projects": projects})

def exp_list_view(request):

    experience = Experience.objects.all().order_by('-end_date')

    return render(request, "projects/exp.html", {"exp": experience})

# def new_projects_view(request):
#     form = ProjectForm()
#     return render(request, 'projects/newproject.html', {"form": form})

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/newproject.html"
    success_url = reverse_lazy("list")
