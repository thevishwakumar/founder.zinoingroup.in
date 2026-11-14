import json

raw_certs = [
    # Top verified credentials with link
    {
        "id": "cappriciosec-cybersecurity",
        "title": "Cybersecurity & Ethical Hacking",
        "organization": "CappricioSec University",
        "orgIcon": "bx bx-shield-quarter",
        "footerLabel": None,
        "status": "Verified",
        "isVerified": True,
        "link": {
            "url": "https://university.cappriciosec.com/",
            "text": "ID: b093c0aab1b34503a711",
            "title": "Verify Certificate on CappricioSec University portal"
        }
    },
    {
        "id": "cisco-cybersecurity",
        "title": "Introduction to Cybersecurity",
        "organization": "Cisco Networking Academy",
        "orgIcon": "bx bx-award",
        "footerLabel": "Candidate Record",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "simplilearn-ethical-hacking",
        "title": "Ethical Hacking 101: Beginner's Guide",
        "organization": "Simplilearn SkillUp",
        "orgIcon": "bx bx-shield-alt",
        "footerLabel": "SkillUp Certification",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "skillfront-iso27001",
        "title": "ISO/IEC 27001 Information Security Associate",
        "organization": "SkillFront",
        "orgIcon": "bx bx-check-shield",
        "footerLabel": "Associate Credential",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    # TCS iON & SEBI Financial / Entrepreneurship tracks
    {
        "id": "tcs-corporate-actions",
        "title": "Corporate Actions & Entrepreneurship",
        "organization": "TCS iON",
        "orgIcon": "bx bx-briefcase",
        "footerLabel": "Enterprise Credential",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "sebi-investor-awareness",
        "title": "SEBI Investor Awareness Test",
        "organization": "Securities and Exchange Board of India",
        "orgIcon": "bx bxs-bank",
        "footerLabel": "Regulatory Compliance",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "hubspot-digital-marketing",
        "title": "Digital Marketing Certified",
        "organization": "HubSpot Academy",
        "orgIcon": "bx bx-line-chart",
        "footerLabel": "Inbound Marketing",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "webul-risk-management",
        "title": "Risk Management in Financial Sector",
        "organization": "Webul",
        "orgIcon": "bx bx-dollar-circle",
        "footerLabel": "Financial Risk",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "microsoft-excel-analytics",
        "title": "Business Analytics with Excel",
        "organization": "Microsoft",
        "orgIcon": "bx bx-stats",
        "footerLabel": "Business Intelligence",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "hp-leadership-entrepreneurship",
        "title": "Effective Leadership & Social Entrepreneurship",
        "organization": "HP LIFE Foundation",
        "orgIcon": "bx bx-group",
        "footerLabel": "Executive Leadership",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "accenture-digital-marketing",
        "title": "Digital Marketing & Social Media",
        "organization": "Accenture",
        "orgIcon": "bx bx-target-lock",
        "footerLabel": "Professional Marketing",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "google-ads-display",
        "title": "Google Ads Display Certification",
        "organization": "Google",
        "orgIcon": "bx bxl-google",
        "footerLabel": "Display Ad Operations",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "google-ads-search",
        "title": "Google Ads Search Certification",
        "organization": "Google",
        "orgIcon": "bx bxl-google",
        "footerLabel": "Search Network Advertising",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "semrush-marketing-analytics",
        "title": "Fundamentals of Marketing Analytics",
        "organization": "Semrush Academy",
        "orgIcon": "bx bx-analyse",
        "footerLabel": "Analytics & Attribution",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "study-badshah-marketing",
        "title": "Digital & Social Media Marketing",
        "organization": "Study Badshah (Accredited by ACTD)",
        "orgIcon": "bx bx-trending-up",
        "footerLabel": "Accredited Program",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "linkedin-entrepreneurship",
        "title": "Entrepreneurship Foundations",
        "organization": "LinkedIn Learning",
        "orgIcon": "bx bxl-linkedin-square",
        "footerLabel": "Business Foundations",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "google-campaign-manager",
        "title": "Campaign Manager 360 Certificate",
        "organization": "Google",
        "orgIcon": "bx bxl-google",
        "footerLabel": "Enterprise Ad Serving",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "mtf-business-administration",
        "title": "Business Administration",
        "organization": "MTF Institute of Management",
        "orgIcon": "bx bx-buildings",
        "footerLabel": "Executive Administration",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "udemy-financial-analysis",
        "title": "Advanced Financial Analysis and Management",
        "organization": "Udemy",
        "orgIcon": "bx bx-money",
        "footerLabel": "Valuation & Analysis",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "cmi-digital-marketing",
        "title": "Digital Marketing Professional Certificate",
        "organization": "Content Marketing Institute",
        "orgIcon": "bx bx-certification",
        "footerLabel": "Content & Campaigns",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "wscube-facebook-ads",
        "title": "Master Facebook Ads In 90 Minutes",
        "organization": "WsCube Tech",
        "orgIcon": "bx bxl-facebook-square",
        "footerLabel": "Performance Ads",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "letsupgrade-genai",
        "title": "Introduction to GenAI & Prompting",
        "organization": "Lets Upgrade",
        "orgIcon": "bx bx-bot",
        "footerLabel": "Generative AI",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "udemy-wordpress-pro",
        "title": "Advanced WordPress Course for Professionals",
        "organization": "Udemy",
        "orgIcon": "bx bxl-wordpress",
        "footerLabel": "CMS Architecture",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "futurelearn-digital-marketing",
        "title": "Digital Skills: Digital Marketing",
        "organization": "Future Learn (Accenture)",
        "orgIcon": "bx bx-globe",
        "footerLabel": "Omnichannel Strategy",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "futurelearn-social-media",
        "title": "Digital Skills: Social Media",
        "organization": "Future Learn (Accenture)",
        "orgIcon": "bx bx-share-alt",
        "footerLabel": "Audience Engagement",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "google-cm360-exam",
        "title": "Campaign Manager 360 Certification Exam",
        "organization": "Google Digital Academy",
        "orgIcon": "bx bxl-google",
        "footerLabel": "Enterprise Ad Tech",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "tcs-collateral-management",
        "title": "Understanding Collateral Management",
        "organization": "TCS iON",
        "orgIcon": "bx bx-shield-quarter",
        "footerLabel": "Banking Operations",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "tcs-corporate-actions-intro",
        "title": "Introduction to Corporate Actions",
        "organization": "TCS iON",
        "orgIcon": "bx bx-briefcase-alt",
        "footerLabel": "Capital Markets",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "simplilearn-excel-analytics",
        "title": "Business Analytics with Excel (Beginner to Pro)",
        "organization": "Simplilearn",
        "orgIcon": "bx bx-table",
        "footerLabel": "Data Analytics",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "hp-social-entrepreneurship",
        "title": "Social Entrepreneurship",
        "organization": "HP LIFE Foundation",
        "orgIcon": "bx bx-bulb",
        "footerLabel": "Social Impact",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "hp-effective-leadership",
        "title": "Effective Leadership Principles",
        "organization": "HP LIFE Foundation",
        "orgIcon": "bx bx-user-voice",
        "footerLabel": "People Management",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "semrush-social-impact",
        "title": "Maximizing Your Social Impact with Semrush Toolkit",
        "organization": "Semrush Academy",
        "orgIcon": "bx bx-chart",
        "footerLabel": "Competitive Intelligence",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "tcs-financial-risk",
        "title": "Understanding Risk Management in Financial Sector",
        "organization": "TCS iON",
        "orgIcon": "bx bx-check-shield",
        "footerLabel": "Institutional Risk",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "letsupgrade-marketing-ai",
        "title": "Digital Marketing with AI",
        "organization": "Lets Upgrade",
        "orgIcon": "bx bx-chip",
        "footerLabel": "AI Marketing",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "saylor-business-ethics",
        "title": "BUS200 – Business Ethics",
        "organization": "Saylor Academy",
        "orgIcon": "bx bx-book-bookmark",
        "footerLabel": "Corporate Governance",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "linkedin-marketing-pro",
        "title": "Digital Marketing Professional Certificate",
        "organization": "LinkedIn Learning",
        "orgIcon": "bx bxl-linkedin",
        "footerLabel": "Career Certification",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "nism-investor-awareness",
        "title": "National Institute of Securities Markets (NISM) Awareness",
        "organization": "NISM (SEBI)",
        "orgIcon": "bx bx-certification",
        "footerLabel": "Financial Literacy",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "cybersec-network-defense",
        "title": "Network Defense & Threat Hunting Fundamentals",
        "organization": "CyberSec Foundation",
        "orgIcon": "bx bx-shield",
        "footerLabel": "Threat Mitigation",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "codecraft-python-cybersec",
        "title": "Python for Defensive Cybersecurity & Automation",
        "organization": "CodeCraft Academy",
        "orgIcon": "bx bxl-python",
        "footerLabel": "Security Scripting",
        "status": "Verified",
        "isVerified": True,
        "link": None
    },
    {
        "id": "enterprise-linux-admin",
        "title": "Linux System Administration & Server Hardening",
        "organization": "Enterprise Linux",
        "orgIcon": "bx bxl-tux",
        "footerLabel": "Systems Security",
        "status": "Verified",
        "isVerified": True,
        "link": None
    }
]

cert_data = {
    "$schema": "./schemas/certifications.schema.json",
    "certifications": raw_certs
}

with open('founder.zinoingroup.in/data/certifications.json', 'w', encoding='utf-8') as f:
    json.dump(cert_data, f, indent=2)

print(f"Updated data/certifications.json with {len(raw_certs)} verified certificates!")

