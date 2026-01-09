import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from applicants.forms import ApplicantForm
from applicants.models import Applicant

@pytest.fixture
def pdf_file():
    return SimpleUploadedFile(
        "test_cv.pdf", b"file_content", content_type="application/pdf"
    )

@pytest.fixture
def txt_file():
    return SimpleUploadedFile(
        "test_cv.txt", b"file_content", content_type="text/plain"
    )

@pytest.mark.django_db
def test_valid_form(pdf_file):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "id_number": "123456789",
        "phone": "0501234567",
        "email": "john@example.com",
        "job_type": "dev",
    }
    form = ApplicantForm(data=data, files={"cv_pdf": pdf_file})
    assert form.is_valid()

@pytest.mark.django_db
def test_invalid_id_number_length(pdf_file):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "id_number": "123",  # Too short
        "phone": "0501234567",
        "email": "john@example.com",
        "job_type": "dev",
    }
    form = ApplicantForm(data=data, files={"cv_pdf": pdf_file})
    assert not form.is_valid()
    assert "id_number" in form.errors

@pytest.mark.django_db
def test_invalid_file_extension(txt_file):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "id_number": "123456789",
        "phone": "0501234567",
        "email": "john@example.com",
        "job_type": "dev",
    }
    # Using .txt instead of .pdf
    form = ApplicantForm(data=data, files={"cv_pdf": txt_file})
    assert not form.is_valid()
    assert "cv_pdf" in form.errors

@pytest.mark.django_db
def test_home_page(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "home.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_apply_page_valid_job(client):
    url = reverse("apply", args=["dev"])
    response = client.get(url)
    assert response.status_code == 200
    assert "apply.html" in [t.name for t in response.templates]
    assert response.context["job_type"] == "dev"

@pytest.mark.django_db
def test_apply_page_invalid_job(client):
    url = reverse("apply", args=["pilot"])
    response = client.get(url)
    assert response.status_code == 404

@pytest.mark.django_db
def test_apply_submission_success(client, pdf_file):
    url = reverse("apply", args=["dev"])
    data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "id_number": "987654321",
        "phone": "0509876543",
        "email": "jane@example.com",
        "address": "Tel Aviv",
        "cv_pdf": pdf_file,
        "job_type": "dev"
    }
    
    # Verify count before
    assert Applicant.objects.count() == 0
    
    # We expect a direct render of the success page (200 OK), not a redirect (302)
    response = client.post(url, data)
    
    # Check if form has errors
    if "form" in response.context:
        print(response.context["form"].errors)

    # Check success page rendered
    assert response.status_code == 200
    assert "success.html" in [t.name for t in response.templates]
    
    # Verify DB creation
    assert Applicant.objects.count() == 1
    applicant = Applicant.objects.first()
    assert applicant.first_name == "Jane"
    assert applicant.job_type == "dev"

