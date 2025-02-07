from django.db import models
from django.contrib.auth.models import User

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField(max_length=2000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_dict(self):
        return {
            'content': self.content
        }

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)