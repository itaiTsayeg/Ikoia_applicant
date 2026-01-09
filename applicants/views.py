from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicantForm

def home(request):
    return render(request, "home.html")

def apply(request, job_type):
    if job_type not in ("dev", "data"):
        return HttpResponse("Unknown job type", status=404)

    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job_type = job_type  
            applicant.save()
            return redirect("home")
    else:
        form = ApplicantForm(initial={"job_type": job_type})

    return render(request, "apply.html", {"form": form, "job_type": job_type})
