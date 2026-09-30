from django.conf import settings

NAV_ITEMS = [
    ("Home", "home", ("home",)),
    ("Services", "services", ("services",)),
    ("AI & Data", "ai_data", ("ai_data",)),
    ("Technologies", "technologies", ("technologies",)),
    ("Industries", "industries", ("industries",)),
    ("Our Work", "our_work", ("our_work", "case_study_detail")),
    ("About", "about", ("about",)),
]


def site(request):
    """Expose navigation and company details to every template."""
    current = getattr(getattr(request, "resolver_match", None), "url_name", "")
    return {
        "nav_items": [
            {"label": label, "url_name": url_name, "active": current in matches}
            for label, url_name, matches in NAV_ITEMS
        ],
        "company_email": settings.CONTACT_EMAIL,
    }
