from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return JsonResponse({'success': True})
    return render(request, 'main/contact.html')
