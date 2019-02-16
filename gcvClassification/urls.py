# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from gcvClassification import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),#views.index()),
    #url(r'^list/$', views.DataPageView.as_view()),
]
