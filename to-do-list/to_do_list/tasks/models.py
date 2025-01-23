import uuid
from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from django.db.models.signals import pre_save

class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=250, null=False, blank=False)
    completed = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_dict(self):
        return {
            'title' : self.title,
            'description' : self.description
        }

def set_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title)
        
        while Task.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
            
        instance.slug = slug
        
pre_save.connect(set_slug, sender=Task)
