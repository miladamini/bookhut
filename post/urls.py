from django.urls import path, re_path

from . import views

appname = 'Po'
urlpatterns = [
    path('roman', views.catgory_roman.as_view(), name='catgory'),
    re_path(r'roman/(?P<slug>[-\w]+)$', views.RomanDitail.as_view(), name='postView'),
    # re_path(r'roman/(?P<slug>[-\w]+)$', views.Post_ditail.as_view(), name='postView'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('abute', views.AbuteView.as_view(), name='abute'),
    path('podcast', views.catgory_pad.as_view(), name='catgory_pad'),
    path('podcast/<str:slug>', views.Podcast_ditail.as_view(), name='PodcastView'),
    path('part/<str:slug>', views.PartView.as_view(), name='part'),
    path('sendboy', views.send_req2.as_view(), name='sen2'),
    path('verifyboy', views.verify2.as_view(), name='verify2'),
    path('part', views.UserAdminView.as_view(), name='part'),
    path('pdfnew', views.PdfView.as_view(), name='pdfnew'),
    # path('test/<str:slug>', views.RomanDitail.as_view(), name='test'),

]
