from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.paginaprincipal,name='paginaprincipal'),
    url(r'^pacientes$', views.listar_pacientes,name='listar_pacientes'),
    url(r'^paciente/nuevo/$', views.paciente_nuevo, name='paciente_nuevo'),
    url(r'^paciente/(?P<pk>[0-9]+)/edit/$', views.paciente_edit, name='paciente_edit'),
    url(r'^paciente/(?P<pk>\d+)/remove/$', views.paciente_remove, name='paciente_remove'),

    url(r'^doctores$', views.listar_doctores,name='listar_doctores'),
    url(r'^doctor/nuevo/$', views.doctor_nuevo, name='doctor_nuevo'),
    url(r'^doctor/(?P<pk>[0-9]+)/edit/$', views.doctor_edit, name='doctor_edit'),
    url(r'^doctor/(?P<pk>\d+)/remove/$', views.doctor_remove, name='doctor_remove'),

    url(r'^consultas$', views.listar_consultas,name='listar_consultas'),
    url(r'^analisis/nuevo/$', views.analisis_nuevo, name='analisis_nuevo'),


]
