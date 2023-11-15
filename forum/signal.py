from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserChatModel
from django.utils import timezone


@receiver(post_save, sender=UserChatModel)
def create_reply_notification_signal(sender, instance, created, *args, **kwargs):
    timedel = timezone.datetime.now() - timezone.timedelta(days=7)
    ioj = UserChatModel.objects.get(p_time__gte=timedel)
    ioj.delete()
