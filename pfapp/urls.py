from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('home/', views.home_view, name="home"),
    path('login_user/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('editUser/', views.editUser_view, name="editUser")
]