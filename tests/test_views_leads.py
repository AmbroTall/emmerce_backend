import os
import django

# Set the settings module explicitly
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.reverse import reverse
import json

from crm.models import Lead


@pytest.mark.django_db
class TestLeadViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        # This method runs before each test, baking a lead object to be used in tests
        self.client = client
        self.lead = baker.make(Lead, name="Test Lead", email="test@example.com")

    def test_create_lead(self):
        data = {
            "name": "New Lead",
            "email": "newlead@example.com",
            "phone": "9876543210",
            "status": "new",
        }

        url = reverse("crm:lead-list")
        response = self.client.post(
            url, content_type="application/json", data=json.dumps(data)
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] is not None
        assert response.data["name"] == data["name"]
        assert response.data["email"] == data["email"]

    def test_retrieve_lead(self):
        url = reverse("crm:lead-detail", kwargs={"pk": str(self.lead.id)})  # Use the baked lead
        response = self.client.get(url, content_type="application/json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Test Lead"
        assert response.data["email"] == "test@example.com"
        assert response.data["id"] == self.lead.id

    def test_update_lead(self):
        data = {"name": "Updated Lead"}
        url = reverse("crm:lead-detail", kwargs={"pk": str(self.lead.id)})  # Use the baked lead
        response = self.client.patch(
            url, data=json.dumps(data), content_type="application/json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Updated Lead"
        assert response.data["id"] == self.lead.id

    def test_list_leads(self):
        baker.make(Lead, name="Lead 1")
        baker.make(Lead, name="Lead 2")

        url = reverse("crm:lead-list")  # Adjust based on your router configuration
        response = self.client.get(url, content_type="application/json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 2
        assert "Lead 1" in [lead["name"] for lead in response.data]
        assert "Lead 2" in [lead["name"] for lead in response.data]

    def test_delete_lead(self):
        url = reverse("crm:lead-detail", kwargs={"pk": str(self.lead.id)})  # Use the baked lead
        response = self.client.delete(url, content_type="application/json")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Lead.objects.count() == 0
