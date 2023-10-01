from django.urls import path
from web_app import views

app_name = "web_app"
urlpatterns = [
    path("", views.index, name = 'index'),
    path("works", views.works, name = 'works'),
    path("about", views.about, name = 'about'),
    path("hireme", views.hireme, name = "hireme")
]