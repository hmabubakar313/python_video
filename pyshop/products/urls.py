from django.urls import path
from . import views
urlpatterns =[
    path("",views.index),
    path("new",views.new)
# products/next_page
]