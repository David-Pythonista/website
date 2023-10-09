from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    return render(request,'home.html')

def cv(request):
    return render(request,'cv.html')

def programming(request):
    return render(request,'programming.html')

def activities(request):
    return render(request,'activities.html')

def teszt(request):
    return render(request,'teszt.html')

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_message = EmailMessage(
                # headers = {'name': name},
                subject = subject,
                body = message,
                from_email = email,
                to = ['m.david.official@gmail.com'],
                reply_to = [email],
            )

            email_message.send()

            return render(request, 'home.html')

    return render(request, 'contact.html', {'form':form})

def project_01(request):
    return render(request,'project_01.html')

def project_02(request):
    return render(request,'project_02.html')