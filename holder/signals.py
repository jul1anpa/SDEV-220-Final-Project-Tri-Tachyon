from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from holder.models import Cart

# The signals.py file defines a signal handler function that will delete a Cart
# object upon session expiration

@receiver(pre_delete, sender=Session)
def session_end_handler(sender, instance, **kwargs):
    session_key = instance.session_key
    try:
        cart = Cart.objects.get(session_key=session_key)
        cart.delete()
    except Cart.DoesNotExist:
        pass