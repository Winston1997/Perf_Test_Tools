from django.urls import path
from django.views.generic import TemplateView

from frontend import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html"), name='index')
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('todo/', views.todo, name='todo'),
    path('toolkit/top-commoand', views.top_command_tool1, name='top_command_tool1'),
    path('toolkit/top-commoand2', views.top_command_tool2, name='top_command_tool2'),
    path('toolkit/ocr_api1', views.ocr_api, name='ocr_api'),
]
