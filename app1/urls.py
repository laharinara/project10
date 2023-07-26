from django.urls import path
from app1.views import *
app1_name="something"



urlpatterns=[
    path("page1/",page2,name="page1"),
    path("page2/",page2,name="page2")
]