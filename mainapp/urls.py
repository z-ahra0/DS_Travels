from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('book/',views.book,name='book'),
    path('info/',views.info,name='info'),
     path('news/',views.news,name='news'),
    path('flight/',views.flight,name='flight'),
    path('hotels/',views.hotels,name='hotels'),
    path('trip/',views.trip,name='trip'),
    path('cars/',views.cars,name='cars'),
    path('activities/',views.activities,name='activities')
    
]