from django.urls import path
from . import views

app_name="dashboard"

urlpatterns=[
    #page urls
    path('corrView3/', views.corr_view3, name="corr_view3"),
    path('corrView2/', views.corr_view2, name="corr_view2"),
    
    # urls of corr 2
    path('corrView2/getEnrollYear', views.corr_view2_getEnrollYear),
    path('corrView2/getSection', views.corr_view2_getSection),
    path('corrView2/updateVisualization', views.corr_view2_updateVisualization),
    
    # urls of corr 3
    path('corrView3/getEnrollYear', views.corr_view3_getEnrollYear),
    path('corrView3/getSection', views.corr_view3_getSection),
    path('corrView3/updateVisualization', views.corr_view3_updateVisualization),
    
    #Main Dashboard view
    path('', views.home_view, name="home"),
]