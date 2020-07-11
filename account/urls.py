from django.urls import path 
from . import views


urlpatterns=[
    path("destinations", views.destinations, name="destinations"),
	path("login",views.login,name="login"),
	path("register", views.register, name="register"),
	path("logout", views.logout, name="logout"),
	path("index", views.index, name="index"),
	


]

	