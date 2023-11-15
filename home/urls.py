from django.urls import path

from . import views

appname = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homeView'),
    path('serch', views.Serch.as_view(), name='serhc'),
    path('NOT', views.NotPdf.as_view(), name='NOT'),
    path('eshtrak', views.esh.as_view(), name='eshtrak'),
    path('details', views.profile.as_view(), name='profile'),
    path('robots.txt', views.Robot.as_view(), name='robots.txt'),
    path('send', views.send_req.as_view(), name='sen'),
    path('verify', views.verify.as_view(), name='verify'),
    path('hmkari', views.hamkati.as_view(), name='hm'),
    path('Autherroman', views.AutherromanView.as_view(), name='Autherroman'),
    path('Romantic', views.CorrectionView1.as_view(), name='Correction1'),
    path('scary', views.CorrectionView2.as_view(), name='Correction2'),
    path('fantasy', views.CorrectionView3.as_view(), name='Correction3'),
    path('Short', views.CorrectionView4.as_view(), name='Correction4'),
    path('social', views.CorrectionView5.as_view(), name='Correction5'),
    path('comedy', views.CorrectionView6.as_view(), name='Correction6'),
    path('police', views.CorrectionView7.as_view(), name='Correction7'),
    path('BDSM', views.CorrectionView8.as_view(), name='Correction8'),
    path('audio-book', views.Category1View.as_view(), name='audio_book'),
    path('podcastt', views.Category2View.as_view(), name='podcastt'),
    path('Audio-novel', views.Category3View.as_view(), name='Audio_novel'),
    path('bookchat', views.My_chat.as_view(), name='My_chat'),

    path('jvayez<int:id>', views.CompetitionView.as_view(), name='.Competition'),




]
