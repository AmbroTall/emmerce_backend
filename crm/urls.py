from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, ContactViewSet, NoteViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r"leads", LeadViewSet, basename="lead")
router.register(r"contacts", ContactViewSet, basename="contact")
router.register(r"notes", NoteViewSet, basename="note")
router.register(r"reminders", ReminderViewSet, basename="reminder")

urlpatterns = router.urls
