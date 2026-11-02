from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from . import content
from .forms import ContactForm, StaffLoginForm
from .models import ContactMessage, SERVICES as SERVICE_CHOICES

staff_only = user_passes_test(lambda u: u.is_active and u.is_staff, login_url="portal_login")

def home(request):
    return render(request, "core/home.html", {"services": content.SERVICES[:3], "promises": content.PROMISES,
                  "steps": content.STEPS, "testimonials": content.TESTIMONIALS})

def services(request):
    return render(request, "core/services.html", {"services": content.SERVICES, "faq": content.FAQ})

def about(request):
    return render(request, "core/about.html", {"promises": content.PROMISES})

def contact(request):
    form = ContactForm(request.POST or None, initial={"service": request.GET.get("service", "standard")})
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thank you. Your message is in and we will reply as soon as we can.")
        return redirect("contact")
    return render(request, "core/contact.html", {"form": form, "faq": content.FAQ[:3]})

class PortalLogin(LoginView):
    template_name = "portal/login.html"
    authentication_form = StaffLoginForm
    redirect_authenticated_user = True

@staff_only
def dashboard(request):
    qs = ContactMessage.objects.all()
    flt, q = request.GET.get("show", "all"), request.GET.get("q", "").strip()
    service = request.GET.get("service", "")
    if flt == "unread":
        qs = qs.filter(is_read=False)
    if service in dict(SERVICE_CHOICES):
        qs = qs.filter(service=service)
    else:
        service = ""
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(email__icontains=q) | Q(message__icontains=q))
    page = Paginator(qs, 15).get_page(request.GET.get("page"))
    stats = {"total": ContactMessage.objects.count(), "unread": ContactMessage.objects.filter(is_read=False).count()}
    return render(request, "portal/dashboard.html", {"page": page, "stats": stats, "flt": flt, "q": q,
                  "service_choices": SERVICE_CHOICES, "service": service})

@staff_only
def message_detail(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if not msg.is_read:
        msg.is_read = True
        msg.save(update_fields=["is_read"])
    return render(request, "portal/detail.html", {"m": msg})

@staff_only
@require_POST
def message_action(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.POST.get("action") == "delete":
        msg.delete()
        messages.success(request, "Message deleted.")
    else:
        msg.is_read = False
        msg.save(update_fields=["is_read"])
    return redirect("portal_dashboard")
