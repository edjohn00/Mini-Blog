import pytest
from factories import BloggerFactory


@pytest.mark.django_db
def test_blogger():
    blogger = BloggerFactory(
        email="gmail.com",
        password="pass",
        first_name="fName",
        last_name="lName",
        is_staff=False,
        is_superuser=False,
    )
    assert blogger.get_full_name() == "fName lName"
    assert blogger.is_staff == False
    assert blogger.is_superuser == False
