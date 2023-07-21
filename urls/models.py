from django.db import models
import uuid
from django.contrib.auth.models import User

    

class Url(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=700, blank=False)
    url_path = models.URLField()
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('time',)
    def __str__(self):
            return self.url_path


class Urlsession(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User,related_name='user_id', on_delete=models.CASCADE)
    url_id = models.ForeignKey(Url, related_name='session_id', on_delete=models.CASCADE)
    model_used = models.CharField(max_length=700, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    input = models.TextField(blank=False, null=False)
    response = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('-time',)
    def __str__(self):
            return self.input