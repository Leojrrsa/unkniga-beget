from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import UserSubscription
from .models import CorporateSubscription
from django.conf import settings

#отправка на почту заполненых форм
@receiver(post_save, sender=UserSubscription)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'Новая подписка на журнал'
        message = f'Новая подписка была оформлена на журнал. Проверьте детали здесь: {instance.get_absolute_url()}'
        recipients = ['leojkee@gmail.com',  'admin@a0881073.xsph.ru']
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)


@receiver(post_save, sender=CorporateSubscription)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'Новая корпоративная подписка на журнал'
        message = f'Новая корпоративная подписка была оформлена на журнал. Проверьте детали здесь: {instance.get_absolute_url()}'
        recipients = ['leojkee@gmail.com',  'admin@a0881073.xsph.ru']
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)

