from django import forms
from .models import Task

class AddTask(forms.Form):
    title = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-input'}))
    description = forms.CharField(required=True, max_length=250, widget=forms.Textarea(attrs={'class':'form-textarea'}))
    
    def save(self, user):
        return Task.objects.create(
            title=self.cleaned_data.get('title'),
            description=self.cleaned_data.get('description'),
            user=user
        )
        
    def update(self, task):
        task.title = self.cleaned_data.get('title')
        task.description = self.cleaned_data.get('description')
        task.save()