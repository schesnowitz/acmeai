from django.db import models
import uuid
from django.contrib.auth.models import User
import os
    

class Document(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=700, blank=False)
    path_to_file = models.FileField(upload_to='user_documents/')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    def filename(self):
        return os.path.basename(self.path_to_file.name)


class Session(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    document = models.ForeignKey(Document, related_name='sessions', on_delete=models.CASCADE)
    model_used = models.CharField(max_length=700, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    input = models.TextField(blank=False, null=False)
    response = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('-time',)
    def __str__(self):
            return self.input