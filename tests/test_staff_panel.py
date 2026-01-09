import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from applicants.models import Applicant

@pytest.fixture
def staff_user(db):
    return User.objects.create_user(
        username="staff", password="password", is_staff=True
    )

@pytest.fixture
def regular_user(db):
    return User.objects.create_user(username="user", password="password")

@pytest.fixture
def applicant(db):
    return Applicant.objects.create(
        first_name="Test",
        last_name="Candidate",
        id_number="123456789",
        email="test@test.com",
        job_type="dev",
        cv_pdf="cv.pdf"
    )

@pytest.mark.django_db
def test_anonymous_access_denied(client):
    url = reverse("staff_dashboard")
    response = client.get(url)
    assert response.status_code == 302
    assert "/admin/login/" in response.url

@pytest.mark.django_db
def test_regular_user_access_denied(client, regular_user):
    client.force_login(regular_user)
    url = reverse("staff_dashboard")
    response = client.get(url)
    assert response.status_code == 302
    assert "/admin/login/" in response.url

@pytest.mark.django_db
def test_staff_access_allowed(client, staff_user):
    client.force_login(staff_user)
    url = reverse("staff_dashboard")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_staff_can_delete_applicant(client, staff_user, applicant):
    client.force_login(staff_user)
    delete_url = reverse("applicant_delete", args=[applicant.pk])
    
    # Verify exists before
    assert Applicant.objects.count() == 1
    
    # Post to delete
    response = client.post(delete_url)
    
    # Verify redirect and deletion
    assert response.status_code == 302
    assert Applicant.objects.count() == 0

