from django.urls import path
from app2.views import *
app2_name="nothing"



urlpatterns=[
    path("page3/",page3,name="page3"),
    path("page4/",page4,name="page4")
]