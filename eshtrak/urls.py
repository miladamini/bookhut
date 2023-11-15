from django.contrib import admin
from django.urls import path
from . import views


admin.autodiscover()

urlpatterns = [
    path('eshtrakDay', views.eshtrakDay.as_view(), name='eshtrak7'),
    path('eshtrakWeek', views.eshtrakWeek.as_view(), name='eshtrakWeek'),
    path('eshtrakMonth', views.eshtrakMonth.as_view(), name='eshtrakMonth'),
    path('eshtrak3Month', views.eshtrak3Month.as_view(), name='eshtrak3Month'),
    path('del', views.delMi.as_view(), name='delmi'),
    path('nemodar', views.rezapanel.as_view(), name='nemodar'),
]
