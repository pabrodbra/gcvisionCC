from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import io
import sqlite3

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class ProductPageView(TemplateView):
    def get(self, request, **kwargs):
        connection = sqlite3.connect("./database.sqlite3")

        c = connection.cursor()
        c.execute("SELECT * FROM products")

        products = c.fetchall()
        
        user_input = request.GET.get('input')
        if not user_input:
            user_input = ''
        rows = []

        for x in products:
            url = x[2] if "http" in x[2] else x[2].rsplit('/',1)[-1]
            rows.append({'category': x[0], 'url': url, 'score': round(x[1], 2)})
            print(rows[-1])

        print(rows)

        return render(request, 'list.html', context={'rows': rows, 'input': user_input})

class CategoryPageView(TemplateView):
    def get(self, request, **kwargs):
        connection = sqlite3.connect("./database.sqlite3")

        c = connection.cursor()
        c.execute("SELECT * FROM categories")

        categories = c.fetchall()
        
        user_input = request.GET.get('input')
        if not user_input:
            user_input = ''
        rows = []

        rows = [{'description':category[0]} for category in categories]

        print(rows)

        return render(request, 'list.html', context={'rows': rows, 'input': user_input})

@csrf_exempt
def APIgetProducts(request):

    response = {'image_categories': image_categories}
    return JsonResponse(response)

@csrf_exempt
def APIgetCategory(request):
    
    response = {'image_categories': image_categories}
    return JsonResponse(response)

@csrf_exempt
def classifyImage(request):
    image = request.FILES['image']

    fs = FileSystemStorage() # .replace('(', '-').replace(')', '-').replace(' ', '_').rsplit('/', 1),
    file_name = fs.save("gcvClassification/static/images/" + str(image), image)
    
    uploaded_image_url = fs.url(file_name)


    client = vision.ImageAnnotatorClient()

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    connection = sqlite3.connect("./database.sqlite3")
    c = connection.cursor()

    c.execute("SELECT description FROM categories")
    categories = c.fetchall()
    categories = [category[0] for category in categories]

    image_categories = []

    for label in labels:
        if (label.description.lower() in categories) and label.score >= 0.9:
            image_categories.append({'score': label.score, 'category': label.description})
            print("Included {} with percentage {} in category {}".format(file_name, label.score, label.description.lower()))
            c.execute("INSERT INTO products (category, percentage, image_path) VALUES (?,?,?)", (label.description.lower(), label.score*100, file_name))
    
    connection.commit()
    response = {'image_categories': image_categories}
    return JsonResponse(response)


