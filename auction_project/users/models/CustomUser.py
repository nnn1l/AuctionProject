from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='user-avatars',
        blank=True,
        null=True,
        verbose_name=_('Avatar')    #  <-- '_' is gettext_lazy()
    )

    biography = models.TextField(
        max_length=300,
        blank=True,
        default='',
        verbose_name=_('Biography')
    )

    last_info_changed = models.DateField(auto_now=True)
    auction_wins = models.IntegerField(default=0, verbose_name=_('Auction Wins'))
    auction_hosted = models.IntegerField(default=0, verbose_name=_('Auction Hosted'))

    def __str__(self):
        return self.username

    @property
    def avatar_url(self):
        """  Sets default avatar if avatar is not setted by user  """
        return self.avatar.url if self.avatar else '/media/default_images/default_avatar.png'