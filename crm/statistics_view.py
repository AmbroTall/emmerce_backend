from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lead, Reminder, Note, Contact


class LeadStatsView(APIView):
    """API view for lead statistics."""

    def get(self, request):
        stats = {
            "total_leads": Lead.objects.count(),
            "new_leads": Lead.objects.filter(status="new").count(),
            "contacted_leads": Lead.objects.filter(status="contacted").count(),
            "qualified_leads": Lead.objects.filter(status="qualified").count(),
            "lost_leads": Lead.objects.filter(status="lost").count(),
        }
        return Response(stats)


class ContactStatsView(APIView):
    """API view for contact statistics."""

    def get(self, request):
        stats = (
            Contact.objects.values("lead__id", "lead__name")
            .annotate(contact_count=Count("id"))
            .order_by("-contact_count")
        )
        return Response(stats)


class ReminderStatsView(APIView):
    """API view for reminder statistics."""

    def get(self, request):
        stats = {
            "total_reminders": Reminder.objects.count(),
            "sent_reminders": Reminder.objects.filter(is_sent=True).count(),
            "pending_reminders": Reminder.objects.filter(is_sent=False).count(),
        }
        return Response(stats)


class NoteStatsView(APIView):
    """API view for note statistics."""

    def get(self, request):
        stats = (
            Note.objects.values("lead__id", "lead__name")
            .annotate(note_count=Count("id"))
            .order_by("-note_count")
        )
        return Response(stats)
