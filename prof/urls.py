from django.urls import path

from . import views

appname = 'Porof'
urlpatterns = [
    path('prof', views.profView.as_view(), name='profView'),
    path('reset', views.Passwordreset.as_view(), name='Passwordreset'),
]
