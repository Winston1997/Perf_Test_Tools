from django.urls import path

from core import views

urlpatterns = [
    path('userinfo/<int:id>/', views.get_user_info, name='get_user_info'),
    path('usermenu/<int:id>/', views.get_user_menu, name='get_user_menu'),
    path('login/', views.my_login, name='login'),
]
