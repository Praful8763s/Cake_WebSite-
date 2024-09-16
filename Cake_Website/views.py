from django.shortcuts import render
from Cake_Website.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    # Render the home page (index.html)
    return render(request, 'index.html')

def about(request):
    # Render the about page (about.html)
    return render(request, 'about.html')

def services(request):
    # Render the services page (services.html)
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Create and save a new Contact object
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        # Pass a success message to the template after saving
        context = {
            'success': True,
            'message': "Thank you for reaching out! We will get back to you soon."
        }
    else:
        context = {
            'success': False
        }
    messages.success(request, 'Successfully Sent The Message!')
    # Render the contact page (contact.html) with context
    return render(request, 'contact.html', context)
