from celery import shared_task
from django.utils.timezone import now
from .models import Reminder

@shared_task
def send_reminder(reminder_id):
    """Task to send a reminder."""
    try:
        reminder = Reminder.objects.get(id=reminder_id, is_sent=False)
        # Logic for sending the reminder (e.g., send an email, notification, etc.)
        print(f"Reminder: {reminder.title} for Lead: {reminder.lead.name}")
        # Mark the reminder as sent
        reminder.is_sent = True
        reminder.save()
        return f"Reminder {reminder_id} sent successfully."
    except Reminder.DoesNotExist:
        return f"Reminder {reminder_id} not found or already sent."
