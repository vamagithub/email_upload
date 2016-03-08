from django import forms
from .models import Email
from django.core.mail import EmailMessage


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'attach','subject' ,'message']


    def _clean_email(self):
        email = self.cleaned_data.get('email')
        return email


    def _clean_subject(self):
        subject = self.cleaned_data.get('subject')
        return subject


    def _clean_message(self):
        message = self.cleaned_data.get('message')
        return message

    # def save(self, fail_silently=False):
    #      email = EmailMessage(to = self.recipient_list,
    #                           from_email = self.from_email,
    #                           body = self.message(),
    #                           subject = self.subject())
    #


    def _clean_attach(self):
        attach = self.cleaned_data.get('attach')
        return attach