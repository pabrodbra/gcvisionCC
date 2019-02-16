from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        print("---- TEST ----")
        return render(request, 'index.html', context=None)