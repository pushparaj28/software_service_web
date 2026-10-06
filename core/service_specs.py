# core/service_specs.py

SERVICE_SPECS = {
    # 1. UI/UX Design (Aapke Screenshot 1 ke hisaab se)
    "ui-ux-design": {
        "tagline": "User-centric, high-conversion interfaces and design systems.",
        "deliver_desc": "We craft intuitive wireframes, responsive prototypes, and scalable design token systems that turn visitors into long-term users.",
        "phases": [
            {"num": "01", "name": "USER RESEARCH", "desc": "Persona mapping, user journeys, competitor analysis, and accessibility audits."},
            {"num": "02", "name": "WIREFRAMING", "desc": "Low-fidelity structural wireframes, information architecture, and core flow validation."},
            {"num": "03", "name": "VISUAL SYSTEM", "desc": "High-fidelity mockups, design tokens, typography, dark/cyber UI systems in Figma."},
            {"num": "04", "name": "USABILITY AUDIT", "desc": "Interactive prototyping, heuristic evaluation, and developer handoff specs."}
        ],
        "modules": [
            {"title": "Design Systems & Tokens", "desc": "Reusable UI libraries, cross-platform components, and brand guidelines."},
            {"title": "Interactive Prototypes", "desc": "Clickable high-fidelity prototypes ready for immediate stakeholder feedback."}
        ]
        
    },

    # 2. Web Development
    "web-development": {
        "tagline": "Fast, accessible, SEO-ready web platforms engineered with modern stacks.",
        "deliver_desc": "Full-stack web applications built with Next.js, Django, and Tailwind CSS engineered for sub-second speeds, zero bloat, and enterprise security.",
        "phases": [
            {"num": "01", "name": "STACK ARCHITECTURE", "desc": "SSR/SSG routing plan, REST API contract drafting, and state architecture."},
            {"num": "02", "name": "FRONTEND & UI DEV", "desc": "Pixel-perfect component engineering, mobile-first responsive layouts."},
            {"num": "03", "name": "BACKEND & ORM SYNC", "desc": "Secure database schemas, session handlers, and optimized query pipelines."},
            {"num": "04", "name": "SEO & EDGE CACHING", "desc": "Lighthouse 95+ score tuning, automated OpenGraph tags, and CDN delivery."}
        ],
        "modules": [
            {"title": "Custom Client Portals", "desc": "Role-based dashboards, authentication security, and live data telemetry."},
            {"title": "Payment & Checkout Engines", "desc": "PCI-compliant multi-gateway integrations with automated invoices."}
        ]
    },

    # 3. School / College Management Software
    "school-management-software": {
        "tagline": "Unified digital operations for campuses, students, teachers, and exams.",
        "deliver_desc": "Centralized institutional platform automating admissions, fee collections, biometric attendance, and parent-student portals.",
        "phases": [
            {"num": "01", "name": "CAMPUS WORKFLOW AUDIT", "desc": "Mapping academic sessions, grading standards, and fee structures."},
            {"num": "02", "name": "STUDENT & STAFF ENGINE", "desc": "Enrollment pipelines, attendance tracking, and timetable schedules."},
            {"num": "03", "name": "FINANCE & EXAM PORTAL", "desc": "Automated fee receipts, grade-sheet generation, and SMS/WhatsApp alerts."},
            {"num": "04", "name": "ROLE-BASED ROLLOUT", "desc": "Separate dashboards for Admins, Teachers, Students, and Parents."}
        ],
        "modules": [
            {"title": "Biometric & RFID Sync", "desc": "Real-time automated student and staff attendance monitoring."},
            {"title": "Online Fee Gateway", "desc": "Automated payment reconciliation and dues reminder alerts."}
        ]
    },

    # 4. Hostel Management Software
    "hostel-management-software": {
        "tagline": "Simplified hostel operations with digital room, mess, and fee tracking.",
        "deliver_desc": "End-to-end boarding software handling room allocations, student check-in/out telemetry, mess billing, and security records.",
        "phases": [
            {"num": "01", "name": "CAPACITY MAPPING", "desc": "Room inventory, floor layouts, bed allocation rules, and asset audits."},
            {"num": "02", "name": "INMATE LIFECYCLE", "desc": "Digital onboarding, KYC record vault, and digital gate-pass tracking."},
            {"num": "03", "name": "MESS & UTILITY BILLING", "desc": "Daily meal counter, utility expense distribution, and monthly invoices."},
            {"num": "04", "name": "SECURITY TELEMETRY", "desc": "Warden management alerts, curfew logs, and parent communication."}
        ],
        "modules": [
            {"title": "Smart Room Allocator", "desc": "Automated bed allotment and occupancy telemetry dashboards."},
            {"title": "Digital Gate Pass Vault", "desc": "Parent-authorized leave approval workflows with OTP verification."}
        ]
    },

    # 5. E-Commerce Development
    "e-commerce-development": {
        "tagline": "High-conversion, multi-currency storefronts and inventory backbones.",
        "deliver_desc": "Blazing-fast e-commerce platforms with automated inventory locks, webhook cart recovery, and lightning checkout flows.",
        "phases": [
            {"num": "01", "name": "CATALOG ARCHITECTURE", "desc": "SKU variations, search indexing, and warehouse schema modeling."},
            {"num": "02", "name": "CHECKOUT & PAYMENTS", "desc": "Single-page checkouts, multi-currency handling, and payment security."},
            {"num": "03", "name": "LOGISTICS & DISPATCH", "desc": "Shipping API sync, tracking numbers, and automated order routing."},
            {"num": "04", "name": "CONVERSION TUNING", "desc": "Cart abandonment triggers, coupon logic, and load-stress testing."}
        ],
        "modules": [
            {"title": "Real-Time Inventory Engine", "desc": "Zero-overselling stock locks with instant order sync."},
            {"title": "Multi-Vendor Marketplace", "desc": "Vendor commission splits, individual storefronts, and payout ledgers."}
        ]
    }
}

def get_service_spec(slug, service):
    """Fallback generator agar koi naya slug add ho jaye"""
    if slug in SERVICE_SPECS:
        return SERVICE_SPECS[slug]
    
    # Clean generic fallback har nayi service ke liye
    title = service.title
    return {
        "tagline": getattr(service, 'short_description', None) or f"Engineered solutions tailored for {title}.",
        "deliver_desc": getattr(service, 'description', None) or f"Production-grade engineering, strict code audits, and scalable cloud architecture designed specifically for {title}.",
        "phases": [
            {"num": "01", "name": f"{title.upper()} DISCOVERY", "desc": "Detailed technical feasibility, database schema requirements, and architecture scope."},
            {"num": "02", "name": "ENGINEERING SPRINT", "desc": f"Clean modular programming for {title} with automated unit and regression tests."},
            {"num": "03", "name": "SYSTEM INTEGRATION", "desc": "API gateway integration, database indexing, and role-based security layers."},
            {"num": "04", "name": "PRODUCTION ROLLOUT", "desc": "CI/CD deployment, telemetry monitoring, and continuous maintenance SLAs."}
        ],
        "modules": [
            {"title": f"{title} Control Dashboard", "desc": "Centralized telemetry console with real-time operational metrics."},
            {"title": "Automated Data Pipelines", "desc": "Low-latency database synchronization and automated audit trails."}
        ]
    }