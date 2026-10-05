import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from . import content
from .forms import ContactForm
from .models import CaseStudy, Industry, Service, Technology
from .models import ServiceQuickEnquiry
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render
from .models import TeamMember


logger = logging.getLogger(__name__)

PROJECT_FILTERS = [
    ("all", "All"),
    ("web", "Web"),
    ("saas", "SaaS"),
    ("ai", "AI"),
    ("healthcare", "Healthcare"),
    ("education", "Education"),
    ("enterprise", "Enterprise"),
]


def _projects():
    return CaseStudy.objects.select_related("industry").prefetch_related("technologies")


def home(request):
    return render(request, "home.html", {
        "services": Service.objects.filter(featured=True).prefetch_related("technologies")[:6],
        "projects": _projects().filter(featured=True)[:3],
        "industries": Industry.objects.filter(is_active=True)[:6],  # <-- Top 6 industries
        "architecture": content.ARCHITECTURE_NODES,
        "team_members": TeamMember.objects.filter(is_active=True).order_by("order", "id"),
    })

def services(request):
    return render(request, "services.html", {
        "services": Service.objects.prefetch_related("technologies"),
    })

def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    other_services = Service.objects.exclude(id=service.id)[:6]
    return render(request, 'service_detail.html', {
        'service': service,
        'other_services': other_services
    })

def ai_data(request):
    return render(request, "ai-data.html", {"capabilities": content.AI_CAPABILITIES})


def technologies(request):
    active = Technology.objects.filter(is_active=True)
    groups = [
        (label, [t for t in active if t.category == value])
        for value, label in Technology.Category.choices
    ]
    return render(request, "technologies.html", {"groups": [g for g in groups if g[1]]})


def industries(request):
    return render(request, "industries.html", {"industries": Industry.objects.filter(is_active=True)})


def our_work(request):
    return render(request, "our-work.html", {"projects": _projects(), "filters": PROJECT_FILTERS})


def case_study_detail(request, slug):
    project = get_object_or_404(_projects().prefetch_related("gallery"), slug=slug)
    related = _projects().filter(category=project.category).exclude(pk=project.pk)[:3]
    return render(request, "case-study-detail.html", {"project": project, "related": related})


def about(request):
    return render(request, "about.html", {
        "principles": content.PRINCIPLES,
        "steps": content.PROCESS_STEPS,
    })


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        inquiry = form.save()
        _notify_team(inquiry)
        messages.success(request, "Your project brief has been received.")
        return redirect("contact")
    return render(request, "contact.html", {"form": form})


def _notify_team(inquiry):
    """Email the team about a new inquiry. Failures are logged, never shown to the visitor."""
    if not settings.CONTACT_EMAIL:
        return
    body = (
        f"Name: {inquiry.name}\nCompany: {inquiry.company}\nEmail: {inquiry.email}\n"
        f"Phone: {inquiry.phone}\nType: {inquiry.get_project_type_display()}\n"
        f"Budget: {inquiry.get_budget_display()}\nTimeline: {inquiry.get_timeline_display()}\n\n"
        f"{inquiry.message}"
    )
    try:
        send_mail(f"New project brief from {inquiry.name}", body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
    except Exception:  # noqa: BLE001 - email must never break the form
        logger.exception("Could not send inquiry notification email")


def page_not_found(request, exception):
    return render(request, "404.html", status=404)

@require_POST
def submit_quick_enquiry(request):
    name = request.POST.get('name', '').strip()
    contact_info = request.POST.get('contact_info', '').strip()
    message = request.POST.get('message', '').strip()
    service_title = request.POST.get('service_title', '').strip()

    if not name or not contact_info or not message:
        return JsonResponse({
            'status': 'error',
            'msg': 'Sabhi required fields bharna anivarya hai.'
        }, status=400)

    # Nayi dedicated table me entry create karein
    enquiry = ServiceQuickEnquiry.objects.create(
        service_title=service_title,
        name=name,
        contact_info=contact_info,
        message=message
    )

    return JsonResponse({
        'status': 'success',
        'msg': 'Transmission confirmed. Telemetry logged into database.',
        'enquiry_id': enquiry.id
    })

def team_view(request):
    founders = TeamMember.objects.filter(is_active=True, is_founder=True).order_by('order')[:2]
    members = TeamMember.objects.filter(is_active=True, is_founder=False).order_by('order')
    
    return render(request, 'team.html', {
        'founders': founders,
        'members': members,
    })