from django import forms
from django.core.validators import RegexValidator

from .models import ContactInquiry

INPUT_CLASS = "field"

phone_validator = RegexValidator(r"^[0-9+()\-\s]{7,20}$", "Enter a valid phone number.")


class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False, max_length=20, validators=[phone_validator])
    # Honeypot: real users never see or fill this field.
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = ContactInquiry
        fields = ["name", "company", "email", "phone", "project_type", "budget", "timeline", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Your full name",
            "company": "Company (optional)",
            "email": "you@company.com",
            "phone": "+91 00000 00000 (optional)",
            "message": "Tell us about your product, users and goals.",
        }
        for name, field in self.fields.items():
            if name == "website":
                continue
            field.widget.attrs["class"] = INPUT_CLASS
            field.widget.attrs["placeholder"] = placeholders.get(name, "")

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 20:
            raise forms.ValidationError("Please share a few more details (at least 20 characters).")
        return message
