from celery import shared_task
from .serializers import *
from .models import Candidate
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def add(x, y):
    try:
        return x+y
    except Exception as e:
        raise e


@shared_task
def create_status(cid):
    data = {'candidateId': cid}
    try:
        serializer = CandidateStatusSerializer(data=data)
        if serializer.is_valid():
            candidate = serializer.save()
            print(candidate.id)
            return True
        else:
            print(serializer.errors)
            return False
    except Exception as e:
        print(e)
        return False


@shared_task
def sending_email():
    candidates = Candidate.objects.all()
    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    from_email = settings.EMAIL_HOST_USER
    try:
        for candidate in candidates:
            send_mail(subject, message, from_email, [candidate.email])
            print(f'email send to {candidate.email}')
        print('email sent successfully')
    except Exception as e:
        print(e)
