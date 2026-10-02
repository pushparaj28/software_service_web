from django.contrib import admin

from .models import CaseStudy, CaseStudyImage, ContactInquiry, Industry, Service, Technology
from .models import ServiceQuickEnquiry

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_active")
    list_filter = ("category", "is_active")
    list_editable = ("is_active",)
    search_fields = ("name", "description")
    ordering = ("category", "name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order", "updated_at")
    list_editable = ("featured", "order")
    list_filter = ("featured",)
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
    ordering = ("order", "title")


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


class CaseStudyImageInline(admin.TabularInline):
    model = CaseStudyImage
    extra = 1


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "industry", "featured", "is_sample_data", "created_at")
    list_editable = ("featured",)
    list_filter = ("category", "industry", "featured", "is_sample_data")
    search_fields = ("title", "client_name", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
    inlines = [CaseStudyImageInline]
    ordering = ("-created_at",)


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "project_type", "budget", "status", "created_at")
    list_editable = ("status",)
    list_filter = ("status", "project_type", "budget", "timeline")
    search_fields = ("name", "company", "email", "message")
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    def has_add_permission(self, request):
        return False


@admin.register(ServiceQuickEnquiry)
class ServiceQuickEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_title', 'contact_info', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'contact_info', 'message', 'service_title')