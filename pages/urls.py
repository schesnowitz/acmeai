from django.urls import path
from .views import index_view, profile_view, private_view
app_name = 'pages'
urlpatterns = [
    path('private', private_view, name='private'),
    path('', index_view, name='index'),
    path('accounts/profile/<int:pk>/', profile_view, name='user_profile'),

]