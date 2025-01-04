"""Test Suites For Reminders."""

import pytest

from rest_framework import status
from rest_framework.reverse import reverse
from crm.models import Lead, Note
from model_bakery import baker


@pytest.mark.django_db
class TestNoteViews:
    """Test Class for Reminders' CRUD."""

    @pytest.fixture
    def lead(self, client):
        """Test Setup."""
        self.client = client
        # Create a Lead for associating with the Note
        return baker.make(Lead, name="Test Lead", email="lead@example.com")

    @pytest.fixture
    def note_data(self, lead):
        """Prepare data for creating a Note."""
        return {"content": "This is a note for the lead.", "lead": lead.id}

    def test_create_note(self, note_data):
        """Test creating a note."""

        url = reverse("crm:note-list")
        response = self.client.post(
            url, data=note_data, content_type="application/json"
        )

        note = Note.objects.first()

        assert response.status_code == status.HTTP_201_CREATED
        assert note.content == note_data["content"]
        assert note.lead.id == note_data["lead"]

    def test_retrieve_note(self, lead):
        """Test retrieving a note."""

        note = baker.make(Note, content="Test Note Content", lead=lead)

        url = reverse("crm:note-detail", kwargs={"pk": note.id})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["content"] == "Test Note Content"
        assert response.data["lead"] == lead.id

    def test_update_note(self, lead):
        """Test updating a note."""

        note = baker.make(Note, content="Old Note Content", lead=lead)

        updated_data = {"content": "Updated Note Content"}
        url = reverse("crm:note-detail", kwargs={"pk": note.id})
        response = self.client.patch(
            url, data=updated_data, content_type="application/json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["content"] == "Updated Note Content"

    def test_list_notes(self, lead):
        """Test listing a note."""

        # Create multiple notes for the test
        baker.make(Note, lead=lead, _quantity=3)

        url = reverse("crm:note-list")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3
