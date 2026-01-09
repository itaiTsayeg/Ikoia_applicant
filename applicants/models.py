from django.db import models

class Applicant(models.Model):
    JOB_CHOICES = [
        ("dev", "Developer"),
        ("data", "Data Analyst"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True)
    id_number = models.CharField(max_length=9, unique=True)

    job_type = models.CharField(max_length=10, choices=JOB_CHOICES)
    cv_pdf = models.FileField(upload_to="cvs/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"