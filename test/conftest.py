# import pytest

# from factories import BloggerFactory
# from pytest_factoryboy import register
# from blogs.models import Author

# register(BloggerFactory)

import os
import django
import pytest

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# Ensure Django is set up
django.setup()

# Import Django-related modules after setup
from factories import BloggerFactory
from pytest_factoryboy import register
from blogs.models import Author

# Register factories
register(BloggerFactory)
