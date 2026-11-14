import json

expertise_data = {
  "$schema": "./schemas/expertise.schema.json",
  "categories": [
    {
      "id": "tech-dev",
      "title": "Technology & Software Development",
      "icon": "bx bx-code-alt",
      "skills": [
        "Full-Stack Web Development",
        "Frontend Development (HTML5, CSS3, ES6+)",
        "Python & FastAPI Architecture",
        "React & Modern UI Frameworks",
        "WordPress & Custom CMS Development",
        "Generative AI & Prompt Engineering",
        "Vector Databases & Semantic RAG Search",
        "Data Analysis & Business Telemetry",
        "REST APIs & Cloudflare Serverless"
      ]
    },
    {
      "id": "cybersecurity",
      "title": "Cybersecurity & Systems Engineering",
      "icon": "bx bx-shield-quarter",
      "skills": [
        "Defensive Security & Threat Hunting",
        "Identity & Access Management (RBAC)",
        "Multi-Tenant Database Isolation",
        "Network Security & Packet Inspection",
        "Linux Server Administration & Hardening",
        "Ethical Hacking & Vulnerability Assessment",
        "Security Risk Management (ISO 27001)",
        "Automated Security Test Suites",
        "Anti-Enumeration Access Controls"
      ]
    },
    {
      "id": "marketing",
      "title": "Digital Marketing & Performance Ads",
      "icon": "bx bx-line-chart",
      "skills": [
        "Meta Ads Manager (Facebook & Instagram)",
        "Google Ads (Search & Display Networks)",
        "Campaign Manager 360 & Ad Operations",
        "Technical & Entity SEO Optimization",
        "Social Media Marketing & Brand Reach",
        "Google Analytics 4 & Tag Manager",
        "Automated Email Lead Nurturing",
        "PPC Advertising & Keyword Strategy",
        "Conversion Rate Optimization (CRO)"
      ]
    },
    {
      "id": "entrepreneurship",
      "title": "Entrepreneurship & Corporate Leadership",
      "icon": "bx bx-bulb",
      "skills": [
        "Founder & Executive Venture Leadership",
        "Commercial Client Software Delivery",
        "Business Administration & Operations",
        "Financial Planning & Risk Governance",
        "Strategic Market Research & Scoping",
        "Banking Processes & Collateral Evaluation",
        "Business Ideation & Innovation Thinking",
        "Agile Team & Project Management",
        "B2B Partnership & Ecosystem Strategy"
      ]
    }
  ]
}

with open('founder.zinoingroup.in/data/expertise.json', 'w', encoding='utf-8') as f:
    json.dump(expertise_data, f, indent=2)

print("Updated data/expertise.json with 36 categorized skills!")

