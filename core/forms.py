from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))  # honeypot

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "service", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us about your space: size, rooms, pets, preferred dates."})}

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""

class StaffLoginForm(AuthenticationForm):
    """Only staff accounts may sign in to the portal."""
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise forms.ValidationError("This area is for administrators only.", code="no_access")
