from django import forms
from core.models import Service,CaseStudy,Industry , Technology

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'slug', 'short_description', 'icon', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none rounded-none',
                'placeholder': 'e.g. Custom Software Development'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none rounded-none',
                'placeholder': 'custom-software-development'
            }),
            'short_description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none rounded-none',
                'placeholder': 'Service ke brief details...'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none rounded-none',
                'placeholder': '</> ya [API]'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2 text-xs text-ink2 file:mr-4 file:py-2 file:px-4 file:border-0 file:text-xs file:bg-[#00ff88] file:text-black file:font-mono file:cursor-pointer'
            }),
        }

class CaseStudyForm(forms.ModelForm):
    class Meta:
        model = CaseStudy
        fields = [
            'title',
            'slug',
            'client_name',
            'industry',
            'category',
            'short_description',
            'challenge',
            'solution',
            'architecture',
            'results',
            'technologies',
            'featured_image',
            'featured',
            'is_sample_data',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'e.g. AI Healthcare Platform'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'ai-healthcare-platform'
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'e.g. MedTech Inc / Confidential'
            }),
            'industry': forms.Select(attrs={
                'class': 'w-full bg-black border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full bg-black border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none'
            }),
            'short_description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Summary of project...'
            }),
            'challenge': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Problem statement...'
            }),
            'solution': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Solution implementation...'
            }),
            'architecture': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Architectural breakdown...'
            }),
            'results': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Measurable impact...'
            }),
            'technologies': forms.SelectMultiple(attrs={
                'class': 'w-full bg-black border border-white/15 px-4 py-2.5 text-xs text-white font-mono focus:border-[#00ff88] focus:outline-none h-32'
            }),
            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2 text-xs text-gray-400 file:mr-4 file:py-2 file:px-4 file:border-0 file:text-xs file:bg-[#00ff88] file:text-black file:font-mono file:cursor-pointer'
            }),
            'featured': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 bg-black border-white/20 text-[#00ff88] focus:ring-0 rounded-none cursor-pointer'
            }),
            'is_sample_data': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 bg-black border-white/20 text-[#00ff88] focus:ring-0 rounded-none cursor-pointer'
            }),
        }


class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['name', 'slug', 'description', 'challenge', 'solution']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'e.g. Healthcare, E-Commerce, FinTech'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'e.g. healthcare, e-commerce'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Industry overview and market scope...'
            }),
            'challenge': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Industry pain points and technical hurdles...'
            }),
            'solution': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'How CODEMATRIX builds dedicated solutions...'
            }),
        }


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'category', 'description', 'icon', 'website_url', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'e.g. Django, React, PyTorch, Docker'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full bg-black border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none'
            }),
            'description': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'Short tech description...'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'e.g. SVG path, lucide icon name, or symbol'
            }),
            'website_url': forms.URLInput(attrs={
                'class': 'w-full bg-black/60 border border-white/15 px-4 py-2.5 text-sm text-white font-mono focus:border-[#00ff88] focus:outline-none',
                'placeholder': 'https://djangoproject.com'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 bg-black border-white/20 text-[#00ff88] focus:ring-0 rounded-none cursor-pointer'
            }),
        }