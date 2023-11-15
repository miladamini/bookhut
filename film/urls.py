from django.urls import path, re_path

from . import views

appname = 'Film'
urlpatterns = [
    path('learning', views.FilmView.as_view(), name='learning'),
    re_path(r'learning/(?P<slug>[-\w]+)$', views.DitaylFilm.as_view(), name='DitaylFilm'),

]
