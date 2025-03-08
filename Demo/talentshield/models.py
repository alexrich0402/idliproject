from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('candidate', _('Candidate')),
        ('hr-manager', _('HR Manager')),
    ]
    
    role = models.CharField(
        _('Role'), 
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='candidate'
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    class Meta:
        verbose_name = _('Custom User')
        verbose_name_plural = _('Custom Users')

    def __str__(self):
        return self.username or self.email