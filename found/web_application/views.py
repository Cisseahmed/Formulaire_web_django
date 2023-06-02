from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Contact_lists
from .models import Contact





def HomePage(request):
    
    if request.method == "POST":
        form = Contact_lists(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = Contact_lists
     
    return render(request, 'index.html', {'form': form} ) 



def Donnee(request):
    donnees  = Contact.objects.all()
    return render(request, 'contacts.html', {'donnees':donnees})