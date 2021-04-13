"""cbdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('banner',views.BannerList.as_view(),name='banner'),
    path('miniBanner',views.MiniBanner.as_view(),name='miniBanner'),
    path('topStories',views.TopStoriesList.as_view(),name='topStories'),
    path('successStories',views.SuccessStoryList.as_view(),name='successStories'),
    path('query',csrf_exempt(views.PostQuery.as_view()),name='query'),
    path('members',views.MembersList.as_view(),name='members'),
    path('courses',views.CourseList.as_view(),name='courses'),
    path('courses/<slug:slug>',views.CourseRetrieveView.as_view(),name='course'),
    path('events',views.EventsList.as_view(), name='events'),
    path('events_callback', views.EventsCallbakcView.as_view(), name='events_callback'),
    path('events/<slug:slug>',views.EventRetrieveView.as_view(),name='event'),
    path('universe',views.UniverseRetrieveView.as_view(),name='universe')

]
