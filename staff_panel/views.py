from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from applicants.models import Applicant

@staff_member_required
def dashboard(request):
    applicants = Applicant.objects.order_by("-created_at")
    return render(request, "staff_panel/dashboard.html", {"applicants": applicants})

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from applicants.models import Applicant


@staff_member_required
def dashboard(request):
    applicants = Applicant.objects.order_by("-created_at")
    return render(request, "staff_panel/dashboard.html", {"applicants": applicants})


@staff_member_required
def applicant_delete_confirm(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    return render(
        request,
        "staff_panel/applicant_confirm_delete.html",
        {"applicant": applicant},
    )


@staff_member_required
def applicant_delete(request, pk):
    if request.method != "POST":
        return redirect("staff_dashboard")

    applicant = get_object_or_404(Applicant, pk=pk)
    applicant.delete()  
    return redirect("staff_dashboard")
