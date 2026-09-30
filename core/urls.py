from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path('services/<slug:slug>/', views.service_detail_view, name='service_detail'),
    path("ai-data/", views.ai_data, name="ai_data"),
    path("technologies/", views.technologies, name="technologies"),
    path("industries/", views.industries, name="industries"),
    path("our-work/", views.our_work, name="our_work"),
    path("our-work/<slug:slug>/", views.case_study_detail, name="case_study_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
