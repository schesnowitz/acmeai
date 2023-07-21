from .libraries import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class ListJobCovers(LoginRequiredMixin, ListView):
    paginate_by = 10 
    model = CoverLetter
    context_object_name = "covers"
    template_name = 'resumes/list_job_covers.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id)

        return queryset 