from django.db import models
import uuid
from django.contrib.auth.models import User

    

class Instruction(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=False)
    prompt = models.TextField(blank=False, null=False)
    data = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    data_text = models.FileField(upload_to="text_files/")
    class Meta:
        ordering = ('-time',)

    
class Chat(models.Model): 
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    instruction_id = models.ForeignKey(Instruction, related_name='chats', on_delete=models.CASCADE)
    model_used = models.CharField(max_length=700, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    input = models.TextField(blank=False, null=False)
    response = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('-time',)
    def __str__(self):
            return self.input