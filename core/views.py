# from django.shortcuts import render
# from django.http import HttpResponse

# def home_view(request):
#     template_name="core/home.html"
#     return render(request,template_name)

from django.views import generic as views


class HomeView(views.TemplateView):
    template_name="core/home.html"


class AboutView (views.TemplateView):
    template_name="core/about.html"   