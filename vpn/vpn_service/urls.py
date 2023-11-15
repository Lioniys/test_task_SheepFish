from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.home, name='profile'),
    path('proxy/<str:user_site_name>/', views.proxy_view, name='proxy_view'),
    path('proxyy/<str:user_site_name>/<path:routes_on_original_site>/', views.proxy_view, name='proxy_view'),
]