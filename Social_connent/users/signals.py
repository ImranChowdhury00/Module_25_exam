# from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model
# from django.dispatch import receiver
# from .models import Profile

# User = get_user_model()

# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created,  **kwargs):
#     if created:
#         Profile.objects.create(User = instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     try:
#         instance.profile.save()
#     except Profile.DoesNotExist:
#         # A profile might not exist if the user was created in bulk or if it was deleted
#         pass