"""Serializers to handle data."""

from rest_framework import serializers
from .models import Lead, Contact, Note, Reminder


class LeadSerializer(serializers.ModelSerializer):
    """Serializer Lead."""

    class Meta:
        """Define Lead Serializer."""
        model = Lead
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Serializer Contact."""

    class Meta:
        """Define Contact Serializer."""
        model = Contact
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    """Serializer Note."""

    class Meta:
        """Define Note Serializer."""
        model = Note
        fields = "__all__"


class ReminderSerializer(serializers.ModelSerializer):
    """Serializer Reminder."""

    class Meta:
        """Define Reminder Serializer."""
        model = Reminder
        fields = "__all__"
