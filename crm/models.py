"""Models for the data storage and strucure."""
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from crm.tasks import schedule_reminder


class Lead(models.Model):
    """Lead models."""
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('lost', 'Lost'),
    ]

    name = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Name must contain only letters and spaces.')])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?[0-9\s\-]+$', 'Phone number must be valid.')])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the lead name."""
        return self.name


class Contact(models.Model):
    """Contact models."""
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'First name must contain only letters and spaces.')])
    last_name = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Last name must contain only letters and spaces.')])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?[0-9\s\-]+$', 'Phone number must be valid.')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the Contact names."""

        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    """Note models."""

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the name of the note owner."""
        return f"Note for {self.lead.name}"


class Reminder(models.Model):
    """Reminder models."""

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='reminders')
    title = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # When the reminder is being created (not updated)
            super().save(*args, **kwargs)  # Save the instance to get an ID
            schedule_reminder.apply_async(args=[self.id])  # Schedule reminder asynchronously
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        """Return name owner of the reminder."""

        return f"Reminder for {self.lead.name} - {self.title}"
