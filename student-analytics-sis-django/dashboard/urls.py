from django.urls import path
from . import views

app_name="dashboard"

urlpatterns=[
    path('corrView3', views.corr_view3, name="corr_view3"),
    path('corrView3/getEnrollYear', views.corr_view3_getEnrollYear),
    path('corrView3/getSection', views.corr_view3_getSection),
    path('corrView3/updateVisualization', views.corr_view3_updateVisualization),
    path('', views.home_view, name="home"),
]