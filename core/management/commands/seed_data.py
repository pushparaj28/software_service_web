"""Load SAMPLE development data. Nothing here represents a real client."""
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import CaseStudy, Industry, Service, Technology

T = Technology.Category
TECHNOLOGIES = [
    ("HTML", T.FRONTEND, "Semantic, accessible markup."),
    ("CSS", T.FRONTEND, "Modern layout and animation."),
    ("Tailwind CSS", T.FRONTEND, "Utility-first responsive styling."),
    ("JavaScript", T.FRONTEND, "Vanilla ES6+ interactivity."),
    ("Python", T.BACKEND, "Readable, versatile backend language."),
    ("Django", T.BACKEND, "Secure, batteries-included web framework."),
    ("Django REST Framework", T.BACKEND, "Clean, well-documented APIs."),
    ("MySQL", T.DATABASE, "Proven relational database."),
    ("PostgreSQL", T.DATABASE, "Advanced open-source SQL database."),
    ("Redis", T.DATABASE, "In-memory cache and queue."),
    ("Machine Learning", T.AI, "Models trained on your data."),
    ("LLM", T.AI, "Large language model integration."),
    ("RAG", T.AI, "Retrieval-augmented generation."),
    ("AI APIs", T.AI, "Managed model and vision APIs."),
    ("Git", T.DEVOPS, "Version control."),
    ("GitHub", T.DEVOPS, "Code hosting and review."),
    ("GitLab", T.DEVOPS, "Source control with built-in CI."),
    ("Docker", T.DEVOPS, "Reproducible containers."),
    ("AWS", T.DEVOPS, "Cloud infrastructure."),
]

SERVICES = [
    ("Custom Software Development", "</>", "Bespoke systems shaped around your workflows.", ["Python", "Django", "MySQL"]),
    ("Web Development", "{}", "Fast, accessible, SEO-ready web platforms.", ["HTML", "Tailwind CSS", "JavaScript"]),
    ("SaaS Development", "∞", "Multi-tenant products built to scale with subscriptions.", ["Django", "PostgreSQL", "Redis"]),
    ("Mobile Application Development", "[]", "Reliable mobile apps backed by secure APIs.", ["Django REST Framework", "AWS"]),
    ("Enterprise Software", "##", "Internal platforms, portals and ERP extensions.", ["Django", "MySQL", "Docker"]),
    ("API Development", "->", "Versioned, documented, well-tested interfaces.", ["Django REST Framework", "Python"]),
    ("UI/UX Engineering", "UI", "Interface systems that stay consistent as you grow.", ["CSS", "Tailwind CSS", "JavaScript"]),
    ("QA & Testing", "QA", "Automated and manual testing for confident releases.", ["Python", "Git"]),
    ("Cloud Engineering", "~", "Secure, cost-aware cloud architecture.", ["AWS", "Docker"]),
    ("DevOps", "Ops", "CI/CD, monitoring and repeatable deployments.", ["GitHub", "GitLab", "Docker"]),
    ("Legacy Modernization", "<>", "Move ageing systems to maintainable stacks safely.", ["Python", "Django", "PostgreSQL"]),
    ("Automation", "Au", "Workflow automation that removes repetitive work.", ["Python", "AI APIs"]),
]

INDUSTRIES = [
    ("Healthcare", "Software for clinics, labs and care teams.", "Fragmented records and manual scheduling.", "Unified, permission-aware patient and scheduling platforms."),
    ("Education", "Platforms for institutions and learners.", "Disconnected tools for content, testing and reporting.", "One portal for courses, assessments and analytics."),
    ("FinTech", "Secure financial products and back-office tooling.", "Strict compliance with slow release cycles.", "Audit-ready services with automated testing."),
    ("E-Commerce", "Storefronts and operations systems.", "Slow pages and inventory mismatches.", "Fast catalogues with real-time stock sync."),
    ("Real Estate", "Listing, CRM and property management systems.", "Leads scattered across spreadsheets and inboxes.", "Central pipeline with automated follow-up."),
    ("Logistics", "Tracking and fleet operations software.", "Poor visibility across shipments.", "Live dashboards fed by event pipelines."),
    ("Manufacturing", "Production, quality and inventory software.", "Paper-based shop-floor processes.", "Digital workflows with traceable records."),
    ("Retail", "Omnichannel retail systems.", "Inconsistent data between stores and online.", "One catalogue and order backbone."),
    ("Travel", "Booking and itinerary platforms.", "Complex pricing and availability rules.", "Rule-driven engines behind clean booking flows."),
    ("Automotive", "Dealer, service and fleet software.", "Service history spread across systems.", "Connected service and inventory platform."),
    ("Media", "Publishing and content operations tools.", "Slow editorial and asset workflows.", "Headless content pipelines with fast delivery."),
    ("Startups", "MVPs and product engineering.", "Limited time and budget to validate ideas.", "Lean architecture that grows without a rewrite."),
    ("Enterprise", "Large-scale internal and customer platforms.", "Legacy systems that block change.", "Incremental modernisation with clear ownership."),
]

CASE_STUDIES = [
    ("Clinic Scheduling Platform", "healthcare", "web", "Appointment and patient-flow system for multi-branch clinics.", ["Django", "MySQL", "Tailwind CSS"], True),
    ("Adaptive Learning Portal", "education", "saas", "Course delivery, assessments and analytics in one portal.", ["Django", "PostgreSQL", "Redis"], True),
    ("Support Copilot with RAG", "enterprise", "ai", "Knowledge assistant grounded in internal documents.", ["LLM", "RAG", "Python"], True),
    ("Inventory ERP Modernisation", "enterprise", "enterprise", "Legacy inventory system moved to a maintainable Django stack.", ["Django", "MySQL", "Docker"], False),
    ("Live Logistics Dashboard", "logistics", "web", "Real-time shipment tracking and exception alerts.", ["Python", "Redis", "JavaScript"], False),
    ("Subscription Billing SaaS", "fintech", "saas", "Plans, invoicing and usage metering for a B2B product.", ["Django", "PostgreSQL", "AWS"], False),
]


class Command(BaseCommand):
    help = "Create sample services, technologies, industries and case studies (idempotent)."

    def handle(self, *args, **options):
        techs = {}
        for name, category, description in TECHNOLOGIES:
            techs[name], _ = Technology.objects.update_or_create(
                name=name, defaults={"category": category, "description": description, "icon": name[:2]}
            )

        for order, (title, icon, short, tech_names) in enumerate(SERVICES, start=1):
            service, _ = Service.objects.update_or_create(
                slug=slugify(title),
                defaults={"title": title, "icon": icon, "short_description": short, "description": short,
                          "featured": order <= 6, "order": order},
            )
            service.technologies.set([techs[n] for n in tech_names])

        industries = {}
        for name, description, challenge, solution in INDUSTRIES:
            industries[slugify(name)], _ = Industry.objects.update_or_create(
                slug=slugify(name),
                defaults={"name": name, "description": description, "challenge": challenge, "solution": solution},
            )

        for order, (title, industry, category, short, tech_names, featured) in enumerate(CASE_STUDIES):
            study, _ = CaseStudy.objects.update_or_create(
                slug=slugify(title),
                defaults={
                    "title": title, "client_name": "Sample Client (demo data)", "industry": industries[industry],
                    "category": category, "short_description": short, "featured": featured, "is_sample_data": True,
                    "challenge": f"{short} The existing process was manual, slow and hard to measure.",
                    "solution": "We designed a modular architecture, shipped in short iterations and automated testing and deployment.",
                    "architecture": "Client apps → REST API → Django services → relational database → background workers → cloud hosting.",
                    "results": "Sample outcome text: faster workflows, clearer reporting and a maintainable codebase.",
                },
            )
            study.technologies.set([techs[n] for n in tech_names])

        self.stdout.write(self.style.SUCCESS("Sample data loaded. It is demo content, not real client work."))
