"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tasks.views.student.listPostStudentView import ListPostStudentView
from tasks.views.student.dgpStudentView import DGPStudentView
from tasks.views.discipline.listPostDisciplineView import ListPostDisciplineView
from tasks.views.discipline.dgpDisciplineView import DGPDisciplineView
from tasks.views.task.listPostTaskView import ListPostTaskView
from tasks.views.task.dgpTaskView import DGPTaskView


urlpatterns = [
    path('api/student/', ListPostStudentView.as_view()),
    path('api/student/<int:student_id>/', DGPStudentView.as_view()), 

    path('api/discipline/', ListPostDisciplineView.as_view()), 
    path('api/discipline/<int:discipline_id>/', DGPDisciplineView.as_view()),

    path('api/task/', ListPostTaskView.as_view()), 
    path('api/task/<int:task_id>/', DGPTaskView.as_view())
]
