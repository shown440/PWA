# from django.urls import path

# from . import views

# urlpatterns = [
#     # path('/', views.base_layout),
#     path('', views.index),
# ]

from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'base_layout', views.index,name='base_layout'),
    # path(r'base_layout',views.base_layout,name='base_layout'),
    # path(r'getdata',views.getdata,name='getdata')
]