from django.contrib import admin
from .models import Applicant


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("id_number", "first_name", "last_name", "email", "phone", "job_type", "created_at")
    search_fields = ("id_number", "first_name", "last_name", "email", "phone")
    list_filter = ("job_type", "created_at")
