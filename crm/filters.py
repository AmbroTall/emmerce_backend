"""Filters for the viewsets of the CRM."""

from django_filters import rest_framework as filters

from .models import (
    Lead,
    Contact,
    Note,
    Reminder,
)


class LeadFilter(filters.FilterSet):
    """Filter Lead."""

    class Meta:
        """Define filter options."""

        model = Lead
        fields = "__all__"


class ContactFilter(filters.FilterSet):
    """Filter Contact."""

    class Meta:
        """Define filter options."""

        model = Contact
        fields = "__all__"


class NoteFilter(filters.FilterSet):
    """Filter Note."""

    class Meta:
        """Define filter options."""

        model = Note
        fields = "__all__"


class ReminderFilter(filters.FilterSet):
    """Filter Reminder."""

    class Meta:
        """Define filter options."""

        model = Reminder
        fields = "__all__"
