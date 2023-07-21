from django.urls import path
from chats.views import (
    IndexView,
    delete_view,
    chat_csv_view,
    chat_session_view,
    create_view,
    update_view,
)

app_name = "chats"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("delete/<int:pk>/", delete_view, name="delete"),
    path("csv/<int:pk>/", chat_csv_view, name="csv"),
    path("session/<int:pk>/", chat_session_view, name="chat"),
    path("create_with_file/", create_view, name="create"),
    path("update_with_file/<int:pk>/", update_view, name="update"),
]
