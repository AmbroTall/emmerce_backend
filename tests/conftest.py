import os
import django


def pytest_configure():
    """Configure the Django settings for pytest."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "core.settings"
    )  # Update with your settings module
    django.setup()
