from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adoption/', views.adoption_page, name='adoption_page'),
    path('donate/', views.donate, name='donate'),
     path('adoption/<int:child_id>/', views.adopt_child, name='adopt_child'),  

]