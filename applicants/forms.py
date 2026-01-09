from django import forms
from .models import Applicant


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            "job_type",
            "first_name",
            "last_name",
            "id_number",
            "phone",
            "email",
            "address",
            "cv_pdf",
        ]

    def clean_cv_pdf(self):
        f = self.cleaned_data.get("cv_pdf")
        if not f:
            return f

        name = f.name.lower()
        if not name.endswith(".pdf"):
            raise forms.ValidationError("Please upload a PDF file.")

        return f

    def clean_id_number(self):
        idn = self.cleaned_data.get("id_number", "")
        if not idn.isdigit() or len(idn) != 9:
            raise forms.ValidationError("ID number must be 9 digits.")
        return idn

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        digits = phone.replace("+", "")
        if not digits.isdigit():
            raise forms.ValidationError("Phone number must contain digits only.")
        return phone


