from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_template, name="index"),
    path('generate-short-url/', views.generate_short_URL, name="short_url"),
    path('redirect-url/<str:url_code>', views.redirect_url, name="redirect_url"),
]