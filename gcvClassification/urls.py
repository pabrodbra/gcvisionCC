# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from gcvClassification import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),#views.index()),
    url(r'^products/$', views.ProductPageView.as_view()),
    url(r'^categories/$', views.CategoryPageView.as_view()),
    url(r'^classify$', views.classifyImage, name="classifyImage"),
    url(r'^API/products$', views.APIgetProducts, name="APIgetProducts"),
    url(r'^API/categories$', views.APIgetCategory, name="APIgetCategory"),   
]
