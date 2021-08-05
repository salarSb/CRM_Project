from celery import shared_task

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.html import strip_tags
from config import settings
from organizations.models import Organization
from sale.enums import EmailStatuses
from sale.models import EmailHistory


@shared_task(serializer='json')
def send_email_task(content, sender, receiver):
    try:
        send_mail('Quote for Your Purchase',
                  strip_tags(content),
                  settings.EMAIL_HOST_USER,
                  [receiver],
                  html_message=content,
                  fail_silently=False)
        EmailHistory.objects.create(receiver=Organization.objects.get(owner_email=receiver),
                                    status=EmailStatuses.DONE,
                                    sender=get_user_model().objects.get(username=sender))
        return 'Email has been Send Successfully.'
    except:
        EmailHistory.objects.create(receiver=Organization.objects.get(owner_email=receiver),
                                    status=EmailStatuses.FAILED,
                                    sender=get_user_model().objects.get(username=sender))
        return 'Email has not been Send.'
