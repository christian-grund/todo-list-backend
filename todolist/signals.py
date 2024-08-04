# In deiner Django-Anwendung (z.B. 'todos/signals.py')
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import TodoItem
import datetime

User = get_user_model()

@receiver(post_save, sender=User)
def create_initial_todo(sender, instance, created, **kwargs):
    if created:
        TodoItem.objects.create(
            title='This is my first todo!',
            author=instance,
            created_at=datetime.date.today(),
            checked=False
        )
