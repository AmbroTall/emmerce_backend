"""Test suites for contacts."""
import pytest

from rest_framework import status
from rest_framework.reverse import reverse
from model_bakery import baker
from crm.models import Lead, Contact


@pytest.mark.django_db
class TestContactViews:
    """Test Class for Contact CRUD."""

    @pytest.fixture
    def lead(self, client):
        """Test Setup."""
        self.client = client

        # Create a Lead for associating with the Contact
        return baker.make(Lead, name="Test Lead", email="lead@example.com")

    @pytest.fixture
    def contact_data(self, lead):
        """Prepare data for creating a Contact."""
        return {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "9876543210",
            "lead": lead.id,
        }

    def test_create_contact(self, contact_data):
        url = reverse("crm:contact-list")
        response = self.client.post(
            url, data=contact_data, content_type="application/json"
        )

        contact = Contact.objects.first()

        assert response.status_code == status.HTTP_201_CREATED
        assert contact.first_name == contact_data["first_name"]
        assert contact.last_name == contact_data["last_name"]
        assert contact.email == contact_data["email"]
        assert contact.phone == contact_data["phone"]
        assert contact.lead.id == contact_data["lead"]

    def test_retrieve_contact(self, lead):
        """Test retrieving a contact."""

        contact = baker.make(
            Contact, first_name="Test", last_name="Contact", lead=lead
        )

        url = reverse("crm:contact-detail", kwargs={"pk": contact.id})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["first_name"] == "Test"
        assert response.data["last_name"] == "Contact"
        assert response.data["lead"] == lead.id

    def test_update_contact(self, lead):
        """Test updating a contact."""

        contact = baker.make(
            Contact, first_name="Old", last_name="Contact", lead=lead
        )

        updated_data = {"first_name": "Updated", "last_name": "Contact"}
        url = reverse("crm:contact-detail", kwargs={"pk": contact.id})
        response = self.client.patch(
            url, data=updated_data, content_type="application/json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["first_name"] == "Updated"
        assert response.data["last_name"] == "Contact"

    def test_list_contacts(self, lead):
        """Create multiple contacts for the test."""
        baker.make(Contact, lead=lead, _quantity=3)

        url = reverse("crm:contact-list")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3
