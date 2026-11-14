import json

# 1. Projects Data (12 projects)
projects_data = {
  "$schema": "./schemas/projects.schema.json",
  "projects": [
    {
      "id": "documind-ai",
      "title": "DocuMind AI",
      "tagline": "Full-Stack Enterprise RAG & Knowledge Assistant",
      "badge": "GitHub Featured · AI & Security",
      "badgeStyle": "background: rgba(14, 165, 233, 0.9);",
      "icon": "bx bx-bot",
      "description": "Document-grounded AI knowledge platform engineered with Python, FastAPI, React, ChromaDB semantic vector search, and Google Gemini AI. Features multi-tenant database isolation, JWT auth, and automated RBAC security test suites.",
      "technologies": [
        "FastAPI",
        "React",
        "ChromaDB",
        "Gemini AI",
        "RBAC Security",
        "PostgreSQL"
      ],
      "actions": [
        {
          "type": "link",
          "label": "View on GitHub",
          "url": "https://github.com/thevishwakumar/documind",
          "icon": "bx bxl-github",
          "buttonClass": "button--primary",
          "ariaLabel": "View DocuMind AI source code on GitHub"
        }
      ]
    },
    {
      "id": "tnt-platforms",
      "title": "TNT Commercial Platforms",
      "tagline": "Client Order Management & Digital Utilities",
      "badge": "Production Client System",
      "badgeStyle": "background: rgba(16, 185, 129, 0.9);",
      "icon": "bx bx-cart",
      "description": "Commercial ordering software with anti-enumeration security engineered for client Shree Taste N Taste Catering, alongside the lightweight TNT Tamil Calendar utility app. Built with vanilla ES modules and Supabase backend.",
      "technologies": [
        "JavaScript ES Modules",
        "Supabase",
        "PostgreSQL",
        "Security Controls",
        "Netlify Functions"
      ],
      "actions": [
        {
          "type": "link",
          "label": "View on GitHub",
          "url": "https://github.com/thevishwakumar/tntdiwaliordermanagement",
          "icon": "bx bxl-github",
          "buttonClass": "button--secondary",
          "ariaLabel": "View TNT Diwali Order Management source code on GitHub"
        }
      ]
    },
    {
      "id": "fashion-cnn",
      "title": "Fashion Item CNN Classifier",
      "tagline": "Interactive Deep Learning & Computer Vision",
      "badge": "GitHub Machine Learning",
      "badgeStyle": "background: rgba(139, 92, 246, 0.9);",
      "icon": "bx bx-brain",
      "description": "Deep learning convolutional neural network (CNN) trained on the Fashion-MNIST dataset. Features an interactive 28x28 HTML5 Canvas for real-time user sketching and instant softmax probability classifications via a Python Flask backend.",
      "technologies": [
        "TensorFlow",
        "Keras",
        "Python Flask",
        "HTML5 Canvas",
        "Computer Vision"
      ],
      "actions": [
        {
          "type": "link",
          "label": "View on GitHub",
          "url": "https://github.com/thevishwakumar/Fashion-Item-Classification-Convolutional-Neural-Networks",
          "icon": "bx bxl-github",
          "buttonClass": "button--secondary",
          "ariaLabel": "View Fashion Item CNN Classifier on GitHub"
        }
      ]
    },
    {
      "id": "mediguide-ai",
      "title": "MediGuide AI",
      "tagline": "Autonomous Healthcare AI Frontend",
      "badge": "GitHub TypeScript",
      "badgeStyle": "background: rgba(236, 72, 153, 0.9);",
      "icon": "bx bx-pulse",
      "description": "Autonomous healthcare frontend platform engineered with TypeScript, React, Vite, and Bun for rapid symptom analysis, clinical triage recommendations, and interactive patient guidance.",
      "technologies": [
        "TypeScript",
        "React",
        "Vite",
        "Bun",
        "Healthcare AI"
      ],
      "actions": [
        {
          "type": "link",
          "label": "View on GitHub",
          "url": "https://github.com/thevishwakumar/mediguideai",
          "icon": "bx bxl-github",
          "buttonClass": "button--secondary",
          "ariaLabel": "View MediGuide AI on GitHub"
        }
      ]
    },
    {
      "id": "zinoin-group",
      "title": "Zinoin Group",
      "tagline": "Founder & CEO Initiative & Digital Infrastructure",
      "badge": "Active Enterprise (Est. Aug 2025)",
      "badgeStyle": "background: rgba(14, 165, 233, 0.9);",
      "icon": "bx bx-globe",
      "description": "Founder & CEO-led business group and digital initiatives (established August 2025), orchestrating enterprise technology services, digital infrastructure, client solutions, and commercial web platforms.",
      "technologies": [
        "Venture Leadership",
        "Digital Infrastructure",
        "Enterprise Architecture",
        "Cloud Hosting"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Explore Venture",
          "url": "https://zinoingroup.in/",
          "icon": "bx bx-globe",
          "buttonClass": "button--primary",
          "ariaLabel": "Visit Zinoin Group corporate website"
        }
      ]
    },
    {
      "id": "performance-marketing",
      "title": "Performance Marketing & Acquisition Funnel",
      "tagline": "Paid Social, Search & Multi-Channel Growth",
      "badge": "Digital Marketing",
      "badgeStyle": "background: rgba(245, 158, 11, 0.9);",
      "icon": "bx bx-target-lock",
      "description": "Engineered high-converting digital advertising campaigns across Meta Ads Manager, Google Ads (Search & Display), and Campaign Manager 360, driving scalable commercial lead generation and ROAS.",
      "technologies": [
        "Meta Ads",
        "Google Ads",
        "Campaign Manager 360",
        "Conversion Tracking",
        "ROAS Optimization"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Discuss Marketing",
          "url": "https://founder.zinoingroup.in/#contact",
          "icon": "bx bx-envelope",
          "buttonClass": "button--secondary",
          "ariaLabel": "Contact Vishwa Kumar about marketing strategy"
        }
      ]
    },
    {
      "id": "enterprise-seo",
      "title": "Enterprise SEO & Growth Architecture",
      "tagline": "Technical SEO, Knowledge Graphs & Telemetry",
      "badge": "Growth & Analytics",
      "badgeStyle": "background: rgba(16, 185, 129, 0.9);",
      "icon": "bx bx-search-alt",
      "description": "Full-funnel search engine optimization, semantic Schema.org entity graph engineering, Google Search Console telemetry, and Core Web Vitals performance tuning to capture top search engine positions.",
      "technologies": [
        "Technical SEO",
        "Schema.org JSON-LD",
        "Google Analytics 4",
        "Core Web Vitals",
        "Entity SEO"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Inquire via Contact",
          "url": "https://founder.zinoingroup.in/#contact",
          "icon": "bx bx-search",
          "buttonClass": "button--secondary",
          "ariaLabel": "Inquire about SEO & Growth"
        }
      ]
    },
    {
      "id": "genai-prompting",
      "title": "GenAI & Applied Prompt Engineering Platform",
      "tagline": "LLM Workflows, Context Engineering & AI Automation",
      "badge": "AI Innovation",
      "badgeStyle": "background: rgba(99, 102, 241, 0.9);",
      "icon": "bx bx-chip",
      "description": "Practical generative AI pipelines and multi-turn prompt engineering platforms connecting large language models with enterprise document search, automated summaries, and conversational knowledge extraction.",
      "technologies": [
        "Generative AI",
        "Prompt Engineering",
        "LLM Pipelines",
        "Gemini API",
        "Knowledge Workflows"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Explore AI Workflows",
          "url": "https://founder.zinoingroup.in/#contact",
          "icon": "bx bx-bot",
          "buttonClass": "button--secondary",
          "ariaLabel": "Contact about GenAI and Prompt Engineering solutions"
        }
      ]
    },
    {
      "id": "financial-risk-analytics",
      "title": "Financial Risk & Corporate Valuation Systems",
      "tagline": "Collateral Governance, Market Analysis & Financial Strategy",
      "badge": "Financial Systems",
      "badgeStyle": "background: rgba(14, 165, 233, 0.9);",
      "icon": "bx bx-trending-up",
      "description": "Corporate action evaluation, banking collateral management workflows, and financial risk governance models structured according to SEBI standards, TCS iON frameworks, and MTF Institute business administration.",
      "technologies": [
        "Risk Governance",
        "Financial Analysis",
        "Collateral Management",
        "Business Analytics",
        "SEBI Compliance"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Consult on Strategy",
          "url": "https://founder.zinoingroup.in/#contact",
          "icon": "bx bx-bar-chart",
          "buttonClass": "button--secondary",
          "ariaLabel": "Consult on Financial Risk and Corporate Strategy"
        }
      ]
    },
    {
      "id": "wordpress-cms",
      "title": "WordPress & CMS Performance Engineering",
      "tagline": "Enterprise Security Hardening, Speed & Custom Architecture",
      "badge": "CMS Solutions",
      "badgeStyle": "background: rgba(59, 130, 246, 0.9);",
      "icon": "bx bxl-wordpress",
      "description": "Professional WordPress architecture and custom theme development featuring rigorous security hardening, database query optimization, Cloudflare edge caching, and mobile speed scores exceeding 95+.",
      "technologies": [
        "WordPress Core",
        "PHP & MySQL",
        "Security Hardening",
        "Edge Caching",
        "Speed Optimization"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Review CMS Services",
          "url": "https://founder.zinoingroup.in/#contact",
          "icon": "bx bx-layer",
          "buttonClass": "button--secondary",
          "ariaLabel": "Review WordPress and CMS services"
        }
      ]
    },
    {
      "id": "cybersecurity-defense",
      "title": "Defensive Cybersecurity & Security Audit Framework",
      "tagline": "Access Governance, RBAC Isolation & Threat Auditing",
      "badge": "Security Engineering",
      "badgeStyle": "background: rgba(220, 38, 38, 0.9);",
      "icon": "bx bx-shield-quarter",
      "description": "Defensive security utilities and security test automation frameworks embodying ISO/IEC 27001 principles, password hashing, JWT session security, and multi-tenant database isolation to defeat enumeration attacks.",
      "technologies": [
        "RBAC Verification",
        "JWT Security",
        "ISO/IEC 27001",
        "Network Defense",
        "Security Test Automation"
      ],
      "actions": [
        {
          "type": "link",
          "label": "Security Consultation",
          "url": "https://founder.zinoingroup.in/#contact",
          "icon": "bx bx-shield-alt",
          "buttonClass": "button--secondary",
          "ariaLabel": "Inquire about Cybersecurity Consultation"
        }
      ]
    },
    {
      "id": "campusbridge",
      "title": "CampusBridge / SkillTrack",
      "tagline": "Student Certificate Tracking & Verification Engine",
      "badge": "In Development",
      "badgeStyle": "background: rgba(100, 116, 139, 0.9);",
      "icon": "bx bx-certification",
      "description": "Secure digital proof platform engineered for students to store and verify symposium and workshop certificates with GPS event validation and administrative cryptographic verification.",
      "technologies": [
        "Verification Engine",
        "GPS Validation",
        "Digital Proof",
        "Access Controls"
      ],
      "actions": [
        {
          "type": "pill",
          "label": "In Development",
          "url": None,
          "icon": "bx bx-time",
          "buttonClass": "",
          "pillStyle": "background: rgba(100, 116, 139, 0.2); color: var(--text-muted); font-size: var(--smaller-font-size); font-weight: 600; padding: 6px 12px; border-radius: var(--radius-full); display: inline-flex; align-items: center;",
          "ariaLabel": "Project in active development"
        }
      ]
    }
  ]
}

with open('founder.zinoingroup.in/data/projects.json', 'w', encoding='utf-8') as f:
    json.dump(projects_data, f, indent=2)

print("Updated data/projects.json with 12 featured projects!")
