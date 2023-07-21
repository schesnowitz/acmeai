from django.db import models
import uuid
from django.contrib.auth.models import User
import os
from ckeditor.fields import RichTextField


class Resume(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=700, blank=False)
    resume_path = models.FileField(upload_to="user_resumes")
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.resume_path.name)


class CoverLetter(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_id = models.ForeignKey(
        Resume, related_name="resumes", on_delete=models.CASCADE
    )
    model_used = models.CharField(max_length=700, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=False, null=False)
    text_area = RichTextField(blank=False, null=False)
    job_description_url = models.URLField(blank=True, null=True)
    description_text = models.TextField(blank=False, null=False)
    person = models.CharField(max_length=1000, blank=True, null=True)
    company_name = models.CharField(max_length=1000, blank=False, null=False)
    content = RichTextField(blank=True, null=True)
    show_company_name_on_pdf = models.BooleanField(default=True)
    street = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state_provence = models.CharField(max_length=1000, blank=True, null=True)
    postal_zip_code = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return self.company_name

    class Meta:
        ordering = ("-time",)


class PdfContent(models.Model):
    # cover_letter = models.ForeignKey(CoverLetter, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(auto_now_add=True)
    llm_text = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.ForeignKey(
        CoverLetter, related_name="covers", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.cover_letter.company_name

    class Meta:
        ordering = ("-time",)


class UserJobProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="job_profile"
    )
    content = RichTextField(blank=True, null=True)
    full_name = models.CharField(max_length=1000, blank=False, null=False)
    show_my_name_on_pdf = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    street = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state_provence = models.CharField(max_length=1000, blank=True, null=True)
    postal_zip_code = models.CharField(max_length=1000, blank=True, null=True)
    telephone = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username


from django.db.models.signals import post_save


def create_user_job_profile(sender, instance, created, **kwargs):
    if created:
        job_profile = UserJobProfile(user=instance)
        job_profile.save()


post_save.connect(create_user_job_profile, sender=User)
