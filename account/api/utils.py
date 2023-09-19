from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def Send_activation_email(recipient_email,activation_url):

    subject = 'Acticate you account on ' + settings.SITE_NAME
    from_email = settings.EMAIL_HOSTUSER
    to = [recipient_email]

    # load the HTML template :- 

    html_content = render_to_string('account/activation_email.html',{'activation_url':activation_url})

    # create the email body eith both HTML and plain text versions:

    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject,text_content,from_email,to)
    email.attach_alternative(html_content,text_content)
    email.send()


