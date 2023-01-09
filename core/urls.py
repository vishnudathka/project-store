from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/",views.AboutView.as_view(),name="about")
]
