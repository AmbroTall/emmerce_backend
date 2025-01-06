import random
from django.core.management.base import BaseCommand
from faker import Faker
from crm.models import Lead, Contact, Reminder, Note

class Command(BaseCommand):
    help = "Seed the database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data (optional)
        self.stdout.write("Deleting existing data...")
        Lead.objects.all().delete()
        Contact.objects.all().delete()
        Reminder.objects.all().delete()
        Note.objects.all().delete()

        self.stdout.write("Seeding data...")

        # Create Leads
        leads = []
        for _ in range(50):  # Adjust the number of leads as needed
            lead = Lead.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                company=fake.company(),
                status=random.choice(["new", "contacted", "qualified", "lost"]),
            )
            leads.append(lead)

        # Create Contacts
        for lead in leads:
            for _ in range(random.randint(1, 5)):  # 1-5 contacts per lead
                Contact.objects.create(
                    lead=lead,
                    first_name=fake.name(),
                    last_name=fake.name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                )

        # Create Notes
        for lead in leads:
            for _ in range(random.randint(1, 3)):  # 1-3 notes per lead
                Note.objects.create(
                    lead=lead,
                    content=fake.text(max_nb_chars=200),
                )

        # Create Reminders
        for lead in leads:
            for _ in range(random.randint(1, 2)):  # 1-2 reminders per lead
                Reminder.objects.create(
                    lead=lead,
                    title=fake.word().capitalize(),
                    scheduled_time=fake.future_datetime(end_date="+30d"),
                    is_sent=random.choice([True, False]),
                )

        self.stdout.write(self.style.SUCCESS("Database seeding completed!"))
