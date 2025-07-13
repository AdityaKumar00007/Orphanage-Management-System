from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('adoption/', views.adoption_page, name='adoption_page'),
    path('donate/', views.donate, name='donate'),
    path('adoption/<int:child_id>/', views.adopt_child, name='adopt_child'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
]