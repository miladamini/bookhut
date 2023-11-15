from django.urls import path, re_path

from . import views

urlpatterns = [

    path('panel', views.PanelView.as_view(), name='admin')

]
