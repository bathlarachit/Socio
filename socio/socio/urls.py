"""socio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view
from eapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('out/',views.home.as_view(),name='home'),
    path('accounts/', include('allauth.urls')),
    path('friends/',views.list.as_view(),name='flist'),
    path('make/',views.makeFriends,name='makeFriends'),
    path('addfriend/<int:pk>/',views.addfriend,name='addfriend'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('chat/<int:pk>/',views.chat,name='chat'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('check/',views.check,name='check'),
    path('detail/<int:pk>/',views.ProfileDetail.as_view(),name='detail'),
    path('create/<int:pk>/',views.CreateWeb.as_view(),name='web'),
    path('post/<int:pk>/',views.CreatePost.as_view(),name='post'),
    path('postlist/',views.postlist,name='plist'),
    path('',views.h,name='out'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
