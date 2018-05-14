from django.urls import path

from . import views

urlpatterns = [
    path('send', views.schedule_send, name='Страница загрузки файла'),
    path('show', views.show_cells, name='Показ ячеек'),
    path('', views.index, name='index'),
]