"""topsis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^pegawai/$', 'core.views.pegawai', name='pegawai'),
    url(r'^pegawai/tambah/$', 'core.views.tambah_pegawai', name='tambah_pegawai'),
    url(r'^pegawai/(?P<id>.+)/$', 'core.views.edit_pegawai', name='edit_pegawai'),

    url(r'^kriteria/$', 'core.views.kriteria', name='kriteria'),
    url(r'^kriteria/tambah/$', 'core.views.tambah_kriteria', name='tambah_kriteria'),

    url(r'^penilaian/$', 'core.views.penilaian', name='penilaian'),

    url(r'^login/$', 'core.views.user_login', name='login'),
    url(r'^logout/$', 'core.views.user_logout', name='logout'),
]
