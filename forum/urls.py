from django.urls import path

from . import views
from rest_framework.documentation import include_docs_urls

appname = 'ch'
urlpatterns = [
    path('userchat', views.ChatView.as_view(), name='userchat'),
    path('partapi', views.PartVeiw.as_view(), name='partapi'),
    path('PartGert/<int:pk>', views.PartGert.as_view(), name='PartGert'),
    path('gap', views.GapView.as_view(), name='gap'),
    path('textpost', views.UserChatViewPost.as_view(), name='textpost'),
    path('gappost', views.UserChatViewPost.as_view(), name='gappost'),
    path('text/<int:pk>', views.UserChatView.as_view(), name='text'),
    path('del/<int:pk>', views.DelView.as_view(), name='DelView'),
    path('pyam/<int:pk>', views.TextView.as_view(), name='TextView'),
    path('docs/', include_docs_urls(title='My API title', public=True))

]
