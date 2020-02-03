from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import redirect


def index(request):
    return render(request, 'index/index.html')


def about(request):
    return render(request, 'index/about.html')


# def contact(request):
#     return render(request, 'index/contact.html')

def contact(request):
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                # send_mail(contact_name, contact_message, contact_email, ['a-economic@gmx.de'])
                email = EmailMessage(
                    contact_name,
                    contact_message,
                    'andrasz_the_polzer@gmx.de',
                    ['andrasz_the_polzer@gmx.de'],
                    reply_to=[contact_email],
                    headers={'Message-ID': 'foo'},
                )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Success! Thank you for your message.')

    return render(request, "index/contact.html", {'form': form})
