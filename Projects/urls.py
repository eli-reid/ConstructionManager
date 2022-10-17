from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.ProjectsListView.as_view(), name='projects.list'),
    path('add/', views.ProjectCreationView.as_view(),name='Project.add')
]