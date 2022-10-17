import imp
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Project
from .forms import ProjectForm
class ProjectsListView(ListView):
    model = Project
    context_object_name = "project"
    template_name: str = "Projects/list.html"

class ProjectCreationView(CreateView):
    template_name = "Projects/add.html"
    model = Project
    success_url = '/Projects'
    form_class = ProjectForm
   