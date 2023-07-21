from django.urls import path
from .views import index_view, document_interact_view, document_csv_view, delete_view
app_name = 'documents'

urlpatterns = [
    path('index/', index_view, name='index'),
    path('interact/<int:pk>/', document_interact_view, name='interact'),
    path('csv/<int:pk>/', document_csv_view, name='csv'),
    path('delete/<int:pk>/', delete_view, name='delete'), 
]