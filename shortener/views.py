from django.shortcuts import render, redirect
from .models import Url
import re
from django.http import JsonResponse, HttpResponse
import json
from .models import Url
from django.utils.crypto import get_random_string

URL_REGEX = "^(https?|http)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$"

def generate_new_url_code()-> str:
    url_code = get_random_string(length=4)
    return url_code

def decode_request_body(request_body: bytes) -> str:
    string_dictionary = request_body.decode("ASCII")
    json_data = json.loads(string_dictionary)
    url = json_data["url"]
    return url

def save_url_db(url: str, url_code: str) -> None:
    url = Url(url=url, url_code=url_code)
    url.save()

# Create your views here.
def render_template(request):
    return render(request, "shortener/index.html")

def generate_short_URL(request):
    full_url = decode_request_body(request.body)
    full_url_code = None
    url_object = Url.objects.filter(url=full_url).values()

    if not re.search(URL_REGEX, full_url):
        response = {"message":"Please, enter a valid url"}
        return JsonResponse(response)

    if not url_object: 
        full_url_code = generate_new_url_code()
        save_url_db(full_url, full_url_code)
    
    if full_url_code is None:
        full_url_code = url_object[0]["url_code"]
    
    shortened_url = f"http://localhost:8000/redirect-url/{full_url_code}"
    
    return JsonResponse({"shortened_url":shortened_url})

def redirect_url(request, url_code):
    url_object = Url.objects.filter(url_code=url_code).values()

    if not url_object:
        return HttpResponse("There are not any url with that url code")

    full_url = url_object[0]["url"]

    return redirect(full_url)