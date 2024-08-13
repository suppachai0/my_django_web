from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutUs, name="aboutUs"),
    path("contact/", views.contactUs, name="contactUs"),
    path("test/", views.forPage, name="for_test"),  
    path("card/", views.cardPage, name="card-page"),
    path("card_color/", views.cardcolorpage, name="color-page")
    
]
