from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .forms import PublicationForm, ComentForm
from .models import Publication

def add_publication(request):
    form = PublicationForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid() and request.user.is_authenticated:
        form.save(request.user)
        return redirect('index')
    
    return render(request, 'publications/add.html', {'form':form})

@login_required(login_url='index')
def my_publications(request):
    publications = Publication.objects.filter(user=request.user)
    
    return render(request, 'publications/me.html', {'publications':publications})

@login_required(login_url='index')
def delete_publication(request, pk):
    publication = get_object_or_404(Publication, id=pk)
    
    if publication.user != request.user:
        return redirect('index')
    
    publication.delete()
    return redirect('me')
    
@login_required(login_url='index')
def update_publication(request, pk):
    publication = get_object_or_404(Publication, id=pk)
    
    if publication.user != request.user:
        return redirect('index')
    
    form = PublicationForm(instance=publication)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publication)
        
        if form.is_valid():
            form.save(user=request.user)
            return redirect('me')
        
    return render(request, 'publications/edit.html', {
        'form':form
    })
    
@login_required(login_url='login')
def add_comment(request, pk):
    publication = get_object_or_404(Publication, id=pk)
    form = ComentForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.publication = publication
        comment.save()
        
        return redirect('index')
    
    return redirect('index')