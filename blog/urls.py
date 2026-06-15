from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index_view, name='index-view'),
]



