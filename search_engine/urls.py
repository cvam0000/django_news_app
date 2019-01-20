from . import views 
from django.urls import paths

urlpatterns=[
    path('',views.search , name='home')
]
