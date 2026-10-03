from django.contrib.staticfiles import finders
from django.db import models
from django.templatetags.static import static
from django.urls import reverse


def static_fallback(path):
    """Return the static URL for `path` if that file exists, else an empty string."""
    return static(path) if finders.find(path) else ""


class Technology(models.Model):
    class Category(models.TextChoices):
        FRONTEND = "frontend", "Frontend"
        BACKEND = "backend", "Backend"
        DATABASE = "database", "Database"
        AI = "ai", "AI & Data"
        DEVOPS = "devops", "DevOps & Cloud"

    name = models.CharField(max_length=80, unique=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.CharField(max_length=255, blank=True)
    icon = models.CharField(max_length=8, blank=True, help_text="Short glyph or initials shown on the card.")
    website_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "name"]
        verbose_name_plural = "technologies"

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=8, blank=True, help_text="Short glyph such as </> or {}.")
    image = models.ImageField(upload_to="services/", blank=True, help_text="Optional. A default illustration is used if empty.")
    technologies = models.ManyToManyField(Technology, blank=True, related_name="services")
    featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0, help_text="Lower numbers appear first.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return static_fallback(f"images/services/{self.slug}.svg") or static_fallback("images/services/default.svg")


class Industry(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    challenge = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    image = models.ImageField(upload_to="industries/", blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "industries"

    def __str__(self):
        return self.name


class CaseStudy(models.Model):
    class Category(models.TextChoices):
        WEB = "web", "Web"
        SAAS = "saas", "SaaS"
        AI = "ai", "AI"
        MOBILE = "mobile", "Mobile"
        ENTERPRISE = "enterprise", "Enterprise"

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    client_name = models.CharField(max_length=120, blank=True)
    industry = models.ForeignKey(Industry, null=True, blank=True, on_delete=models.SET_NULL, related_name="case_studies")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.WEB)
    short_description = models.CharField(max_length=255)
    challenge = models.TextField()
    solution = models.TextField()
    architecture = models.TextField(blank=True)
    results = models.TextField(blank=True)
    technologies = models.ManyToManyField(Technology, blank=True, related_name="case_studies")
    featured_image = models.ImageField(upload_to="case_studies/", blank=True)
    featured = models.BooleanField(default=False)
    is_sample_data = models.BooleanField(default=False, help_text="Tick for demo content that is not a real client project.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]
        verbose_name_plural = "case studies"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("case_study_detail", kwargs={"slug": self.slug})

    def get_image_url(self):
        """Uploaded image, else a project-specific illustration, else a generic one for its category."""
        if self.featured_image:
            return self.featured_image.url
        return (static_fallback(f"images/projects/{self.slug}.svg")
                or static_fallback(f"images/projects/category-{self.category}.svg"))

    @property
    def filter_tags(self):
        """Space-separated tokens used by the client-side filter on the Our Work page."""
        return " ".join(filter(None, [self.category, self.industry.slug if self.industry else ""]))


class CaseStudyImage(models.Model):
    case_study = models.ForeignKey(CaseStudy, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="case_studies/gallery/")
    caption = models.CharField(max_length=160, blank=True)

    def __str__(self):
        return self.caption or f"Image for {self.case_study}"


class ContactInquiry(models.Model):
    class ProjectType(models.TextChoices):
        WEB = "web", "Web application"
        MOBILE = "mobile", "Mobile app"
        SAAS = "saas", "SaaS product"
        AI = "ai", "AI / Data"
        ENTERPRISE = "enterprise", "Enterprise software"
        AUTOMATION = "automation", "Automation"
        OTHER = "other", "Something else"

    class Budget(models.TextChoices):
        LOW = "lt5k", "Under $5k"
        MID = "5k-15k", "$5k – $15k"
        HIGH = "15k-50k", "$15k – $50k"
        XL = "50k+", "$50k+"
        UNSURE = "unsure", "Not sure yet"

    class Timeline(models.TextChoices):
        ASAP = "asap", "As soon as possible"
        SHORT = "1-3m", "1–3 months"
        LONG = "3-6m", "3–6 months"
        FLEX = "flexible", "Flexible"

    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        CLOSED = "closed", "Closed"

    name = models.CharField(max_length=120)
    company = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    project_type = models.CharField(max_length=20, choices=ProjectType.choices)
    budget = models.CharField(max_length=20, choices=Budget.choices)
    timeline = models.CharField(max_length=20, choices=Timeline.choices)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "contact inquiries"

    def __str__(self):
        return f"{self.name} – {self.get_project_type_display()}"


class ServiceQuickEnquiry(models.Model):
    service_title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=150)
    contact_info = models.CharField(max_length=150)  # Email ya Phone
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('closed', 'Closed'),
        ],
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Quick Service Enquiry"
        verbose_name_plural = "Quick Service Enquiries"

    def __str__(self):
        return f"{self.name} - {self.service_title or 'General'}"


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150, help_text="e.g. Co-Founder & CTO, Principal Systems Architect")
    bio = models.TextField(blank=True, help_text="Short engineering / leadership overview")
    avatar = models.ImageField(upload_to="team/", blank=True, null=True)
    is_founder = models.BooleanField(default=False, help_text="Check if member is one of the 2 Co-Founders")
    tech_stack = models.CharField(max_length=255, blank=True, help_text="Comma-separated e.g. Python, Rust, Cloud, AI")
    order = models.PositiveIntegerField(default=0, help_text="Display priority (lower numbers appear first)")
    
    # Social links
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-is_founder', 'id']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} ({self.role})"