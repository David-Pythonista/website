from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cv',views.cv, name='cv'),
    path('programming',views.programming, name='programming'),
    path('activities',views.activities, name='activities'),
    path('contact',views.contact, name='contact'),
    path('teszt',views.teszt, name='teszt'),
    path('project_01', views.project_01, name='project_01'),
    path('project_02', views.project_02, name='project_02'),
]
