from django.urls import path,include
from django.conf.urls import url
from .views import login, auth_view, logout, loggedin, invalidlogin
from django.contrib.auth import views as auth_views

from evoterid import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^adduserinfo/$', views.adduserinfo),
    url(r'^addmodificationinfo/$', views.addmodificationinfo),
    url(r'^deluserinfo/$', views.deluserinfo),
    url(r'^getuserinfo/$', views.getuserinfo),
    url(r'^addsuccess/$', views.addsuccess),
    url(r'^getuserinfo/form6.html', views.form6),
    url(r'^getuserinfo/form7.html', views.form7),
    url(r'^getuserinfo/form8.html', views.form8),
    url(r'^getuserinfo/search.html', views.search),
    url(r'^getuserinfo/treak.html', views.treak),
    url(r'^getuserinfo/verify.html', views.verify),
    url(r'^getuserinfo/admin.html', views.admin),
    url(r'^getuserinfo/about.html', views.about),
    url(r'^getuserinfo/soon.html', views.soon),
    url(r'^getuserinfo/contact.html', views.contact),
    url(r'^getuserinfo/sugcom.html', views.sugcom),
    url(r'^login/$',views.login),
    url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalidlogin/$', views.invalidlogin),
    url(r'^searchresult/$', views.searchresult),
    url(r'^getsearchname/$', views.getsearchname),
    url(r'^login1/$',views.login1),
    url(r'^suggestion/$', views.suggestion),
    url(r'^loggedin1/$', views.loggedin1),
    url(r'^invalidlogin1/$', views.invalidlogin1),
    url(r'^feedback/$', views.feedback),
    url(r'^addsugcom/$', views.addsugcom),
    url(r'^verification/$',views.verification),
    url(r'^update/$',views.update),
    url(r'^updateview/$',views.updateview),
    url(r'^view/$',views.view),
    path('users/', views.UserListView.as_view(), name = 'users'),
    path('modification/',views.modificationListView.as_view(), name = 'modification')
]
