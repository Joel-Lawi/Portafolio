from django.urls import path
from . import views

urlpatterns = [
    path("", views.home ,name='home'),
    path("signup/" , views.signup, name='signup'),
    path("tasks/",views.tasks , name='tasks'),
    path("logout/",views.signout, name='logout'),
    path("signin/",views.signin,name='signin'),
    path('projects/', views.projects ,name="projects"),
    path("create_project/", views.create_project, name="create_project")
]
