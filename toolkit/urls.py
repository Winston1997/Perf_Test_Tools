

from django.urls import path
from django.views.generic import TemplateView

from toolkit import views

urlpatterns = [
    path('top_result_tool1/', views.top_result_tool1, name='top_result_tool1'),
    path('top_result_tool2/', views.top_result_tool2, name='top_result_tool2'),
    path('ocr_api', views.ocr_api, name='ocr_api'),
]
