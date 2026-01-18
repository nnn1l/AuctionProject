from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from users.models.Wallet import Wallet

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    '''  Creates a wallet for every user, that was registered  '''
    if created:
        Wallet.objects.create(user=instance)
