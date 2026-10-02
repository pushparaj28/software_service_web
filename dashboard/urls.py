from django.urls import path
from . import views

urlpatterns = [
   
    # Auth
    path('login/', views.panel_login, name='dashboard_login'),
    path('logout/', views.panel_logout, name='dashboard_logout'),

    path('', views.dashboard_overview, name='dashboard_home'),

    # Services
    path('services/', views.service_list, name='dashboard_services'),
    path('services/add/', views.service_create, name='dashboard_service_add'),
    path('services/<int:pk>/edit/', views.service_update, name='dashboard_service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='dashboard_service_delete'),

    # Case Studies
    path('case-studies/', views.case_study_list, name='dashboard_case_studies'),
    path('case-studies/add/', views.case_study_create, name='dashboard_case_study_add'),
    path('case-studies/<int:pk>/edit/', views.case_study_update, name='dashboard_case_study_edit'),
    path('case-studies/<int:pk>/delete/', views.case_study_delete, name='dashboard_case_study_delete'),

    # Industries
    path('industries/', views.industry_list, name='dashboard_industries'),
    path('industries/add/', views.industry_create, name='dashboard_industry_add'),
    path('industries/<int:pk>/edit/', views.industry_update, name='dashboard_industry_edit'),
    path('industries/<int:pk>/delete/', views.industry_delete, name='dashboard_industry_delete'),

    # Technologies
    path('technologies/', views.technology_list, name='dashboard_technologies'),
    path('technologies/add/', views.technology_create, name='dashboard_technology_add'),
    path('technologies/<int:pk>/edit/', views.technology_update, name='dashboard_technology_edit'),
    path('technologies/<int:pk>/delete/', views.technology_delete, name='dashboard_technology_delete'),

    # Contact Leads (Inhe verify/add karein)
    path('leads/', views.lead_list, name='dashboard_leads'),
    path('leads/<int:pk>/status/', views.lead_status_update, name='dashboard_lead_status'),
    path('leads/<int:pk>/delete/', views.lead_delete, name='dashboard_lead_delete'),

    # existing paths...
    path('quick-enquiries/', views.dashboard_quick_enquiries, name='dashboard_quick_enquiries'),
    path('quick-enquiries/<int:pk>/status/', views.update_quick_enquiry_status, name='update_quick_enquiry_status'),
    path('quick-enquiries/<int:pk>/delete/', views.delete_quick_enquiry, name='delete_quick_enquiry'),
]