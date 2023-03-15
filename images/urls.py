from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index_view, name='images-index'),
    path('upload/', views.upload_view, name='images-upload'),
    path('wallet/', TemplateView.as_view(template_name='wallet.html'), name='wallet'),

]