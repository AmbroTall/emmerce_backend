"""Celery class to schedule reminders."""
from celery import shared_task


@shared_task
def schedule_reminder(reminder_id):
    """Task to send a reminder."""
git aff
    from crm.models import Reminder

    try:
        reminder = Reminder.objects.get(id=reminder_id, is_sent=False)
        # Logic for sending the reminder
        print(f"Reminder: {reminder.title} for Lead: {reminder.lead.name}")
        # Mark the reminder as sent
        reminder.is_sent = True
        reminder.save()
        return f"Reminder {reminder_id} sent successfully."
    except Reminder.DoesNotExist:
        return f"Reminder {reminder_id} not found or already sent."
