from django.urls import path
from projects import views

urlpatterns = [
    path("", views.projects_list_view, name="list"),
    path("list/", views.projects_list_view, name="list"),
    path("experience/", views.exp_list_view, name="experience"),
    # path('list/newproject/', views.new_projects_view, name='newproject'),
    path('list/newproject/', views.ProjectCreateView.as_view(), name='newproject'),
]