from django import forms
from .models import Publication, Comment

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['content']
        
    def save(self, user, commit=True):
        publication = super().save(commit=False)
        publication.user = user
        
        if commit:
            publication.save()
            return publication
        
        return publication
    
class ComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']