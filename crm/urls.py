from django.urls import path
from rest_framework.routers import DefaultRouter

from .statistics_view import (
    LeadStatsView,
    ContactStatsView,
    ReminderStatsView,
    NoteStatsView,
)
from .views import LeadViewSet, ContactViewSet, NoteViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r"leads", LeadViewSet, basename="lead")
router.register(r"contacts", ContactViewSet, basename="contact")
router.register(r"notes", NoteViewSet, basename="note")
router.register(r"reminders", ReminderViewSet, basename="reminder")

# Define the statistics routes manually
statistics_urls = [
    path("stats/leads/", LeadStatsView.as_view(), name="lead-stats"),
    path("stats/contacts/", ContactStatsView.as_view(), name="contact-stats"),
    path("stats/reminders/", ReminderStatsView.as_view(), name="reminder-stats"),
    path("stats/notes/", NoteStatsView.as_view(), name="note-stats"),
]

# Combine router URLs with statistics URLs
urlpatterns = router.urls + statistics_urls
