from django.urls import path
from portfolio.views.ProjectListView import ProjectListView

urlpatterns = [
 path("projects/", ProjectListView.as_view(), name='project-list')
]
