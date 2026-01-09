from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Applicant


@receiver(post_delete, sender=Applicant)
def send_delete_email(sender, instance, **kwargs):
    if instance.email:
        send_mail(
            subject="Your application status – IKOIA",
            message=(
                f"Hello {instance.first_name},\n\n"
                "Thank you for applying to IKOIA.\n"
                "At this stage we will not continue with your application.\n\n"
                "We wish you success,\nIKOIA HR"
            ),
            from_email=None,
            recipient_list=[instance.email],
        )
