from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserActivityLog

# Флаг для проверки, что сигнал не был вызван рекурсивно
is_logging = False

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    global is_logging
    if is_logging:  # Проверяем, был ли уже вызван сигнал
        return
    is_logging = True
    try:
        UserActivityLog.objects.create(
            user=user,
            action='LOGIN',
            details=f'User {user.username} logged in.',
        )
    finally:
        is_logging = False  # Сбрасываем флаг после завершения обработки

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    global is_logging
    if is_logging:
        return
    is_logging = True
    try:
        UserActivityLog.objects.create(
            user=user,
            action='LOGOUT',
            details=f'User {user.username} logged out.',
        )
    finally:
        is_logging = False

@receiver(post_save)
def log_object_create(sender, instance, created, **kwargs):
    global is_logging
    if is_logging:  # Проверяем, был ли уже вызван сигнал
        return
    is_logging = True
    try:
        if created and hasattr(instance, 'user'):
            UserActivityLog.objects.create(
                user=instance.user,
                action='CREATE',
                object_type=sender.__name__,
                object_id=instance.id,
                details=f'{sender.__name__} object created.',
            )
    finally:
        is_logging = False

@receiver(post_delete)
def log_object_delete(sender, instance, **kwargs):
    global is_logging
    if is_logging:  # Проверяем, был ли уже вызван сигнал
        return
    is_logging = True
    try:
        if hasattr(instance, 'user'):
            UserActivityLog.objects.create(
                user=instance.user,
                action='DELETE',
                object_type=sender.__name__,
                object_id=instance.id,
                details=f'{sender.__name__} object deleted.',
            )
    finally:
        is_logging = False
