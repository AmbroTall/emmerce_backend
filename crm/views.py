"""ViewSet for managing crud operations for CRM."""

from rest_framework.viewsets import ModelViewSet

from .filters import LeadFilter, ContactFilter, NoteFilter, ReminderFilter
from .models import Lead, Contact, Note, Reminder
from .serializers import (
    LeadSerializer,
    ContactSerializer,
    NoteSerializer,
    ReminderSerializer,
)


class LeadViewSet(ModelViewSet):
    """Base class for the Lead Views."""

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filterset_class = LeadFilter
    search_fields = ["name", "email", "phone"]
    ordering_fields = ["created_at", "updated_at"]


class ContactViewSet(ModelViewSet):
    """Base class for the Contact Views."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_class = ContactFilter
    search_fields = ["first_name", "last_name", "email", "phone"]
    ordering_fields = ["created_at", "updated_at"]


class NoteViewSet(ModelViewSet):
    """Base class for the Note Views."""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filterset_class = NoteFilter


class ReminderViewSet(ModelViewSet):
    """Base class for the Reminder Views."""

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    filterset_class = ReminderFilter
    ordering_fields = ["scheduled_time", "created_at"]
