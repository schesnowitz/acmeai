from django.urls import path
from urls.views import url_index_view, interaction_view, delete_view, url_csv_view

app_name='urls'
urlpatterns = [
    path('', url_index_view, name='index'),
    path('interactions/<int:pk>/', interaction_view, name='interactions'),

    path('csv/<int:pk>/', url_csv_view, name='csv'),
    path('delete/<int:pk>/', delete_view, name='delete'),

]