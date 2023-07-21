from django.urls import path
from .views.index import index_view
from .views.delete_view import delete_cover_letter_view, delete_view
from .views.trigger_llm_and_list import trigger_and_list_view
from .views.create_cover import create_cover_view
from .views.update_description import update_description_view
from .views.edit_generated_text import edit_generated_text_view
from .views.view_pdf_as_html import pdf_as_html_view
from .views.view_pdf import pdf_view, pdf_download
from .views.user_job_profile import (
    user_job_profile_view,
    user_job_profile_pdf_view,
    user_job_profile_form_view
)
from .views.edit_cover_address_to import cover_address_view
from.views.list_job_covers import ListJobCovers


app_name = "resumes"

urlpatterns = [
    path("index/", index_view, name="index"),
    path("create/<int:pk>/", create_cover_view, name="create"),
    path("llm-and-list/<int:pk>/", trigger_and_list_view, name="trigger_and_list"),
    path(
        "update-description/<int:pk>/",
        update_description_view,
        name="update_description",
    ),
    path(
        "edit-generated-text/<int:pk>/",
        edit_generated_text_view,
        name="edit_generated_text",
    ),
    path("pdf-html/<int:pk>/", pdf_as_html_view, name="pdf_html"),
    path("cover-pdf/<int:pk>/", pdf_view, name="pdf_view"),
    path("download-pdf/<int:pk>/", pdf_download, name="pdf_download"),
    path("user-job-profile/<int:pk>/", user_job_profile_view, name="user_job_profile"),
    path("user-job-profile-form/<int:pk>/", user_job_profile_form_view, name="user_job_profile_form"),
    path("job-covers/<int:pk>/", ListJobCovers.as_view(), name="list_job_covers") ,
 
    path(
        "user-job-profile-pdf/<int:pk>/<int:id>/",
        user_job_profile_pdf_view,
        name="user_job_profile_pdf",
    ),
    path(
        "cover-address/<int:pk>/<int:pdf_key>/",
        cover_address_view,
        name="cover_address",
    ),
    path("delete/<int:pk>/", delete_view, name="delete"),
    path("delete-cover/<int:pk>/", delete_cover_letter_view, name="delete_cover"),
]
