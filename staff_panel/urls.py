from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="staff_dashboard"),
    path("delete/<int:pk>/", views.applicant_delete_confirm, name="applicant_delete_confirm"),
    path("delete/<int:pk>/confirm/", views.applicant_delete, name="applicant_delete"),
]
