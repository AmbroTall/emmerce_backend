"""Test Suites For Reminders."""

import pytest

from rest_framework import status
from rest_framework.reverse import reverse
from crm.models import Lead, Reminder
from model_bakery import baker


@pytest.mark.django_db
class TestReminderViews:
    """Test Class for Reminders' CRUD."""

    @pytest.fixture
    def lead(self, client):
        """Test Setup."""
        self.client = client
        # Create a Lead for associating with the Reminder
        return baker.make(Lead, name="Test Lead", email="lead@example.com")

    @pytest.fixture
    def reminder_data(self, lead):
        """Prepare data for creating a Reminder."""
        return {
            "title": "Test Reminder",
            "scheduled_time": "2025-01-05T10:00:00+00:00",
            "lead": lead.id,
        }

    def test_create_reminder(self, reminder_data):
        """Testing creating a reminder."""
        url = reverse("crm:reminder-list")
        response = self.client.post(
            url, data=reminder_data, content_type="application/json"
        )

        reminder = Reminder.objects.first()

        assert response.status_code == status.HTTP_201_CREATED
        assert reminder.title == reminder_data["title"]
        assert (reminder.scheduled_time.isoformat() ==
                reminder_data["scheduled_time"])
        assert reminder.lead.id == reminder_data["lead"]

    def test_retrieve_reminder(self, lead):
        """Testing retrieving a reminder."""

        reminder = baker.make(Reminder, title="Test Reminder", lead=lead)

        url = reverse("crm:reminder-detail", kwargs={"pk": reminder.id})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Test Reminder"
        assert response.data["lead"] == lead.id

    def test_update_reminder(self, lead):
        """Testing updating a reminder."""

        reminder = baker.make(Reminder, title="Old Reminder", lead=lead)

        updated_data = {"title": "Updated Reminder"}
        url = reverse("crm:reminder-detail", kwargs={"pk": reminder.id})
        response = self.client.patch(
            url, data=updated_data, content_type="application/json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Updated Reminder"

    def test_list_reminders(self, lead):
        """Testing listing a reminder."""

        # Create multiple reminders for the test
        baker.make(Reminder, lead=lead, _quantity=3)

        url = reverse("crm:reminder-list")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3
