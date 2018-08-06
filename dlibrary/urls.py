from django.conf.urls import url
from django.views.generic import RedirectView

from dlibrary import views

urlpatterns = [
    url('^home/$',views.home,name='hme'),
    url('^about/$',views.about,name="about"),
    url('^front/$',views.front),
    url('^cse/$',views.MyListc.as_view(),name='cse'),
    url('^it/$', views.MyListi.as_view(), name='it'),
    url('^civil/$', views.MyListci.as_view(), name='civil'),
    url('^mech/$', views.MyListm.as_view(), name='mech'),
    url('^etc/$', views.MyListe.as_view(), name='etc'),
    url('^eee/$', views.MyListee.as_view(), name='eee'),
    url('^book/$', views.BookList.as_view(), name='blist'),
    url('^book/(?P<pk>[0-9]+)$', views.BookDetail.as_view(), name='bdet'),
    url('^chkstu/', views.chkstu, name="chkstu"),
    url('^chkeml/', views.chkeml, name="chkeml"),
    url(r'^edit_student/edit/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name='student_edit'),
    url('^feedback/$', views.FeedCreate.as_view(),name='feed'),
    url('^$',RedirectView.as_view(url='front')),
]