# from email.mime.text import MIMEText
from email.mime.text import MIMEText

from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from email_upload import settings
from .forms import EmailForm


def send_email(request):
    if request.method != 'POST':
        form = EmailForm()
        context = {
            "form": form
        }
        return render(request,'email.html', context)

    form = EmailForm(request.POST, request.FILES)

    if form.is_valid():
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        email   = form.cleaned_data.get("email")
        a  = request.FILES['attach']
        # try:
        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['vamagithub@gmail.com'])
        # mail.attach(a.name, MIMEText(a.read().decode("utf-8")) , a.content_type)
        mail.attach(a.name, a.read().decode("utf-8") , a.content_type)
        mail.send()
        context ={
            "message": 'Sent email to %s' % email
        }
        return render(request,'email.html',context)

        # except Exception as e:
        #     str(e)
        #     context = {
        #         "message": 'Either the attachment is too  big or corrupt'
        #     }
        #     return render(request,'error.html',context)

        return render(request,'email.html', {'message': 'Unable to send email. Please try again later'})