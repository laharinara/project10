from django.urls import path
from app3.views import *
app3_name="something"



urlpatterns=[
    path("page5/",page5,name="page5"),
    path("page6/",page6,name="page6")
]