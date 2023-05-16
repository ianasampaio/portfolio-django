from django.views.generic import ListView 
from portfolio.models.base.Project import Project 

class ProjectListView(ListView): 	
    model = Project 	
    template_name = 'potfolio/projects_list.html'