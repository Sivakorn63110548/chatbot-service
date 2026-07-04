"""
Idempotent locale seeder — safe to run multiple times.
Usage: python -m app.seeds.seed_locales
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import text
from app.core.database import engine

# ── Flat string sections ────────────────────────────────────────────────────

STRINGS: list[tuple[str, str, str, str]] = [
    # (lang, section, key, value)

    # nav
    ("th", "nav", "home",       "หน้าแรก"),
    ("th", "nav", "about",      "เกี่ยวกับ"),
    ("th", "nav", "skill",      "ทักษะ"),
    ("th", "nav", "experience", "ประสบการณ์"),
    ("th", "nav", "project",    "โปรเจกต์"),
    ("th", "nav", "contact",    "ติดต่อ"),
    ("en", "nav", "home",       "Home"),
    ("en", "nav", "about",      "About"),
    ("en", "nav", "skill",      "Skill"),
    ("en", "nav", "experience", "Experience"),
    ("en", "nav", "project",    "Project"),
    ("en", "nav", "contact",    "Contact"),

    # topbar
    ("th", "topbar", "cta",         "ดูเรซูเม่"),
    ("th", "topbar", "viewResume",  "ดูเรซูเม่"),
    ("th", "topbar", "resumeTitle", "เรซูเม่"),
    ("th", "topbar", "resumeName",  "ศิวกร ทันยุภักดิ์"),
    ("th", "topbar", "openNewTab",  "เปิดในแท็บใหม่"),
    ("th", "topbar", "download",    "ดาวน์โหลด"),
    ("th", "topbar", "close",       "ปิด"),
    ("en", "topbar", "cta",         "CV / Resume"),
    ("en", "topbar", "viewResume",  "View Resume"),
    ("en", "topbar", "resumeTitle", "Resume"),
    ("en", "topbar", "resumeName",  "Sivakorn Tanyupak"),
    ("en", "topbar", "openNewTab",  "Open in new tab"),
    ("en", "topbar", "download",    "Download"),
    ("en", "topbar", "close",       "Close"),

    # home
    ("th", "home", "greeting",      "สวัสดี, ผม"),
    ("th", "home", "name",          "บุ๊ค"),
    ("th", "home", "role",          "นักพัฒนา Full Stack"),
    ("th", "home", "desc",          "ผมออกแบบและพัฒนาระบบที่ยืดหยุ่น เว็บแอปสมัยใหม่ และแพลตฟอร์มอัจฉริยะสำหรับธุรกิจ"),
    ("th", "home", "experience",    "2 ปี"),
    ("th", "home", "experienceSub", "ประสบการณ์"),
    ("en", "home", "greeting",      "Hi, I'm"),
    ("en", "home", "name",          "Book"),
    ("en", "home", "role",          "Full Stack Developer"),
    ("en", "home", "desc",          "I design and build scalable systems, modern web apps, and intelligent platforms for businesses."),
    ("en", "home", "experience",    "2 Years"),
    ("en", "home", "experienceSub", "Experience"),

    # about
    ("th", "about", "eyebrow",        "ผมเป็นใคร"),
    ("th", "about", "title",          "เกี่ยวกับผม"),
    ("th", "about", "sub",            "นักพัฒนาที่หลงใหลในการสร้างระบบที่ยืดหยุ่นและประสบการณ์ดิจิทัลสมัยใหม่"),
    ("th", "about", "name",           "ศิวกร ทันยุภักดิ์  ( บุ๊ค )"),
    ("th", "about", "jobTitle",       "⚙️ นักพัฒนา Full Stack"),
    ("th", "about", "bio",            "หลงใหลในการสร้างเว็บแอปพลิเคชันที่ยืดหยุ่นและสำรวจเทคโนโลยีใหม่ๆ ในปัจจุบัน ต้องการเรียนรู้เกี่ยวกับสายงานนี้ สะสมประสบการณ์ และอยากเห็นโลกในอนาคตที่เทคโนโลยีเข้ามามีส่วนร่วมในชีวิตประจำวันของผู้คน"),
    ("th", "about", "birthDateLabel", "วันเกิด"),
    ("th", "about", "birthDate",      "17 มีนาคม 2544 ( 24 ปี )"),
    ("th", "about", "addressLabel",   "ที่อยู่"),
    ("th", "about", "address",        "เกาะยาว พังงา 83000"),
    ("en", "about", "eyebrow",        "Who I am"),
    ("en", "about", "title",          "About Me"),
    ("en", "about", "sub",            "Passionate developer building scalable systems and modern digital experiences."),
    ("en", "about", "name",           "Sivakorn Tanyupak  ( Book )"),
    ("en", "about", "jobTitle",       "⚙️ Full Stack Developer"),
    ("en", "about", "bio",            "Passionate about building scalable web applications and exploring today's new technologies. Want to learn about this line of work, accumulate experience, and want to see a future world where technology takes part in people's daily lives."),
    ("en", "about", "birthDateLabel", "Birth Date"),
    ("en", "about", "birthDate",      "March 17, 2001 ( 24 years old )"),
    ("en", "about", "addressLabel",   "Address"),
    ("en", "about", "address",        "Ko Yao, Phang Nga 83000, Thailand"),

    # about.education
    ("th", "about.education", "title",      "การศึกษา"),
    ("th", "about.education", "degree",     "วิศวกรรมศาสตรบัณฑิต (วิศวกรรมคอมพิวเตอร์และระบบอัจฉริยะ)"),
    ("th", "about.education", "university", "มหาวิทยาลัยวลัยลักษณ์"),
    ("th", "about.education", "bio",        "ศึกษาวิชาการคอมพิวเตอร์สมัยใหม่บนพื้นฐานที่แข็งแกร่งด้านคณิตศาสตร์และอิเล็กทรอนิกส์ โดยเน้นการสร้างระบบอัจฉริยะที่เชื่อมต่อกัน"),
    ("en", "about.education", "title",      "Education"),
    ("en", "about.education", "degree",     "Bachelor of Engineering (Computer Engineering & Intelligent Systems)"),
    ("en", "about.education", "university", "Walailak University"),
    ("en", "about.education", "bio",        "I studied modern computing disciplines with a strong foundation in mathematics and electronics, focusing on building intelligent, connected systems."),

    # skill
    ("th", "skill", "eyebrow", "สิ่งที่ผมใช้งาน"),
    ("th", "skill", "title",   "ทักษะทางเทคนิค"),
    ("th", "skill", "sub",     "เทคโนโลยีและเครื่องมือที่ผมใช้สร้างแอปพลิเคชันสมัยใหม่และยืดหยุ่น"),
    ("en", "skill", "eyebrow", "What I work with"),
    ("en", "skill", "title",   "Technical Skills"),
    ("en", "skill", "sub",     "Technologies and tools I use to build modern, scalable applications."),

    # experience
    ("th", "experience", "eyebrow",      "ประสบการณ์การทำงาน"),
    ("th", "experience", "title",        "ที่ที่ผมเคยทำงาน"),
    ("th", "experience", "sub",          "ประสบการณ์มืออาชีพในการสร้างแพลตฟอร์ม full-stack สำหรับอุตสาหกรรมจริง"),
    ("th", "experience", "currentLabel", "ปัจจุบัน"),
    ("en", "experience", "eyebrow",      "Work experience"),
    ("en", "experience", "title",        "Where I've Worked"),
    ("en", "experience", "sub",          "Professional experience building full-stack platforms for real-world industries."),
    ("en", "experience", "currentLabel", "Current"),

    # project
    ("th", "project", "eyebrow",      "สิ่งที่ผมสร้าง"),
    ("th", "project", "title",        "โปรเจกต์"),
    ("th", "project", "sub",          "โปรเจกต์โอเพนซอร์สและการทดลองส่วนตัวบน GitHub"),
    ("th", "project", "privateLabel", "ส่วนตัว"),
    ("th", "project", "viewCode",     "ดูโค้ด"),
    ("en", "project", "eyebrow",      "What I've built"),
    ("en", "project", "title",        "Projects"),
    ("en", "project", "sub",          "Open source projects and personal experiments on GitHub."),
    ("en", "project", "privateLabel", "Private"),
    ("en", "project", "viewCode",     "View Code"),

    # contact
    ("th", "contact", "eyebrow", "ติดต่อผม"),
    ("th", "contact", "title",   "มาเชื่อมต่อกัน"),
    ("th", "contact", "sub",     "เปิดรับโอกาส, ความร่วมมือ และโปรเจกต์ที่น่าสนใจ"),
    ("th", "contact", "hint",    "คลิกอีเมลหรือโทรศัพท์เพื่อคัดลอก · ลิงก์โซเชียลเปิดในแท็บใหม่"),
    ("th", "contact", "copied",  "คัดลอกแล้ว!"),
    ("en", "contact", "eyebrow", "Get in touch"),
    ("en", "contact", "title",   "Let's Connect"),
    ("en", "contact", "sub",     "Open to opportunities, collabs, and interesting projects."),
    ("en", "contact", "hint",    "Click email or phone to copy · social links open in new tab"),
    ("en", "contact", "copied",  "Copied!"),

    # footer
    ("th", "footer", "text", "ศิวกร ทันยุภักดิ์ · สร้างด้วย React + TypeScript"),
    ("en", "footer", "text", "Sivakorn Tanyupak · Built with React + TypeScript"),
]

# ── Experience entries ──────────────────────────────────────────────────────

EXPERIENCES = [
    {"slug": "hospitality", "logo": "https://www.bookengine.com/public/img/home/logo-05.png", "period": "2023 – 2024", "is_current": False},
    {"slug": "realestate",  "logo": "https://inspiringgroup.sg/wp-content/uploads/2025/10/logo.webp", "period": "2024 – Present", "is_current": True},
]

EXPERIENCE_TRANSLATIONS = [
    {"slug": "hospitality", "lang": "th", "company": "bookengine.com", "role": "นักพัฒนา (Programmer)",
     "description": "พัฒนาและดูแลแพลตฟอร์มเทคโนโลยีสำหรับโรงแรมและร้านอาหาร มุ่งเน้นการสร้างระบบที่เชื่อถือได้สำหรับขั้นตอนงานด้านการบริการ งานรวมถึง Property Management System (PMS), การจัดการการจอง, ระบบธุรกรรมร้านอาหาร, การเชื่อมต่อ OTA และแดชบอร์ดการดำเนินงาน"},
    {"slug": "hospitality", "lang": "en", "company": "bookengine.com", "role": "Programmer",
     "description": "Developed and maintained technology platforms for hotels and restaurant operations, focusing on building reliable systems that support real hospitality workflows. Work included a Property Management System (PMS), reservation management, restaurant transaction systems, OTA integrations, and operational dashboards."},
    {"slug": "realestate",  "lang": "th", "company": "Inspiring Group", "role": "นักพัฒนา Full-Stack & สถาปนิกระบบ",
     "description": "ออกแบบและสร้างแพลตฟอร์มที่ยืดหยุ่นสำหรับบริษัทอสังหาริมทรัพย์ที่เชี่ยวชาญด้านการขายและบริหารวิลล่าให้เช่า ระบบครอบคลุมรายการทรัพย์สิน, การบริหารการจอง, การเชื่อมต่อ OTA, การประมวลผลการชำระเงิน และการติดตามทางการเงิน"},
    {"slug": "realestate",  "lang": "en", "company": "Inspiring Group Co., Ltd.", "role": "Full-Stack Developer & Programmer",
     "description": "Currently designing and building scalable platforms for a real estate company specialising in villa sales and rental management. Systems cover property listings, reservation management, OTA integrations, payment processing, and financial tracking across both backend and frontend."},
]

EXPERIENCE_RESPONSIBILITIES = [
    # hospitality TH
    {"slug": "hospitality", "lang": "th", "position": 0, "text": "ระบบบริหารจัดการโรงแรม (PMS)"},
    {"slug": "hospitality", "lang": "th", "position": 1, "text": "การเชื่อมต่อ OTA สำหรับซิงค์การจอง"},
    {"slug": "hospitality", "lang": "th", "position": 2, "text": "ระบบสั่งอาหารและธุรกรรมร้านอาหาร"},
    {"slug": "hospitality", "lang": "th", "position": 3, "text": "การประมวลผลการชำระเงิน"},
    {"slug": "hospitality", "lang": "th", "position": 4, "text": "สถาปัตยกรรม Backend API และฐานข้อมูล"},
    {"slug": "hospitality", "lang": "th", "position": 5, "text": "แดชบอร์ดรายงานการดำเนินงานโรงแรม"},
    # hospitality EN
    {"slug": "hospitality", "lang": "en", "position": 0, "text": "Hotel Property Management Systems (PMS)"},
    {"slug": "hospitality", "lang": "en", "position": 1, "text": "OTA integrations for booking synchronization"},
    {"slug": "hospitality", "lang": "en", "position": 2, "text": "Restaurant order and transaction systems"},
    {"slug": "hospitality", "lang": "en", "position": 3, "text": "Payment processing and transaction handling"},
    {"slug": "hospitality", "lang": "en", "position": 4, "text": "Backend API and database architecture"},
    {"slug": "hospitality", "lang": "en", "position": 5, "text": "Reporting dashboards for hotel operations"},
    # realestate TH
    {"slug": "realestate", "lang": "th", "position": 0, "text": "ระบบบริหารการเช่าวิลล่าและจัดการทรัพย์สิน"},
    {"slug": "realestate", "lang": "th", "position": 1, "text": "การเชื่อมต่อ OTA สำหรับช่องทางการจอง"},
    {"slug": "realestate", "lang": "th", "position": 2, "text": "แพลตฟอร์มการจองและการสำรอง"},
    {"slug": "realestate", "lang": "th", "position": 3, "text": "การประมวลผลการชำระเงินและการจัดการธุรกรรม"},
    {"slug": "realestate", "lang": "th", "position": 4, "text": "ระบบบัญชีและรายงานทางการเงิน"},
    {"slug": "realestate", "lang": "th", "position": 5, "text": "แดชบอร์ดการจัดการภายใน"},
    {"slug": "realestate", "lang": "th", "position": 6, "text": "สถาปัตยกรรม Backend และการออกแบบฐานข้อมูล"},
    # realestate EN
    {"slug": "realestate", "lang": "en", "position": 0, "text": "Villa rental and property management systems"},
    {"slug": "realestate", "lang": "en", "position": 1, "text": "OTA integrations for booking channels"},
    {"slug": "realestate", "lang": "en", "position": 2, "text": "Booking and reservation platforms"},
    {"slug": "realestate", "lang": "en", "position": 3, "text": "Payment processing and transaction management"},
    {"slug": "realestate", "lang": "en", "position": 4, "text": "Accounting and financial reporting systems"},
    {"slug": "realestate", "lang": "en", "position": 5, "text": "Internal management dashboards"},
    {"slug": "realestate", "lang": "en", "position": 6, "text": "Backend architecture and database design"},
]

# ── Projects ────────────────────────────────────────────────────────────────

PROJECTS = [
    {"slug": "possy-backend",     "lang_code": "TypeScript", "stars": 0, "is_private": True,  "url": "https://github.com/Sivakorn63110548/POSsy-backend"},
    {"slug": "resume-sivakorn",   "lang_code": "TypeScript", "stars": 1, "is_private": True,  "url": "https://github.com/Sivakorn63110548/Resume-Sivakorn"},
    {"slug": "face-scan",         "lang_code": "Python",     "stars": 1, "is_private": False, "url": "https://github.com/Sivakorn63110548/Face-Scan-Tensorflow-RTX5070Ti"},
    {"slug": "chatbot-service",   "lang_code": "Python",     "stars": 1, "is_private": False, "url": "https://github.com/Sivakorn63110548/chatbot-service"},
    {"slug": "bookdev-tecnology", "lang_code": "Python",     "stars": 1, "is_private": False, "url": "https://github.com/Sivakorn63110548/BookDev-Tecnology"},
    {"slug": "angular-app",       "lang_code": "TypeScript", "stars": 1, "is_private": False, "url": "https://github.com/Sivakorn63110548/angular-app"},
    {"slug": "fivem-bookdev",     "lang_code": "Lua",        "stars": 1, "is_private": False, "url": "https://github.com/Sivakorn63110548/FiveM-bookDev"},
    {"slug": "install-node22",    "lang_code": "Shell",      "stars": 1, "is_private": False, "url": "https://github.com/Sivakorn63110548/install-package-node22-ubuntu"},
]

PROJECT_TRANSLATIONS = [
    {"slug": "possy-backend",     "lang": "th", "name": "POSsy-backend",                       "description": "Backend API สำหรับระบบ Point of Sale จัดการสินค้า คำสั่งซื้อ การชำระเงิน และธุรกรรม"},
    {"slug": "possy-backend",     "lang": "en", "name": "POSsy-backend",                       "description": "Backend API for a Point of Sale system, handling products, orders, payments, and transaction management."},
    {"slug": "resume-sivakorn",   "lang": "th", "name": "Resume-Sivakorn",                     "description": "เว็บพอร์ตโฟลิโอและเรซูเม่ส่วนตัวที่สร้างด้วย React, TypeScript และ Vite"},
    {"slug": "resume-sivakorn",   "lang": "en", "name": "Resume-Sivakorn",                     "description": "This personal portfolio and resume website built with React, TypeScript, and Vite."},
    {"slug": "face-scan",         "lang": "th", "name": "Face-Scan-Tensorflow-RTX5070Ti",      "description": "ระบบจดจำใบหน้าแบบเรียลไทม์ด้วย TensorFlow เร่งความเร็วด้วย GPU บน RTX 5070Ti"},
    {"slug": "face-scan",         "lang": "en", "name": "Face-Scan-Tensorflow-RTX5070Ti",      "description": "Real-time face recognition system built with TensorFlow, GPU-accelerated on NVIDIA RTX 5070Ti."},
    {"slug": "chatbot-service",   "lang": "th", "name": "chatbot-service",                     "description": "บริการ Chatbot Backend ด้วย Python เชื่อมต่อ API และจัดการการตอบสนองอัตโนมัติ"},
    {"slug": "chatbot-service",   "lang": "en", "name": "chatbot-service",                     "description": "Python-based chatbot backend service with API integration and automated response handling."},
    {"slug": "bookdev-tecnology", "lang": "th", "name": "BookDev-Tecnology",                   "description": "โปรเจกต์สำรวจและทดลองด้านเทคโนโลยีที่สร้างด้วย Python"},
    {"slug": "bookdev-tecnology", "lang": "en", "name": "BookDev-Tecnology",                   "description": "Technology exploration and experimentation project built with Python."},
    {"slug": "angular-app",       "lang": "th", "name": "angular-app",                         "description": "เว็บแอปพลิเคชันที่สร้างด้วย Angular framework และ TypeScript"},
    {"slug": "angular-app",       "lang": "en", "name": "angular-app",                         "description": "Web application built with the Angular framework and TypeScript."},
    {"slug": "fivem-bookdev",     "lang": "th", "name": "FiveM-bookDev",                       "description": "สคริปต์และ resource สำหรับเซิร์ฟเวอร์เกม FiveM (แพลตฟอร์ม multiplayer GTA V)"},
    {"slug": "fivem-bookdev",     "lang": "en", "name": "FiveM-bookDev",                       "description": "Custom game server scripts and resource modifications for FiveM (GTA V multiplayer platform)."},
    {"slug": "install-node22",    "lang": "th", "name": "install-package-node22-ubuntu",       "description": "Shell script สำหรับติดตั้ง Node.js 22 และแพ็กเกจต่างๆ บน Ubuntu server อัตโนมัติ"},
    {"slug": "install-node22",    "lang": "en", "name": "install-package-node22-ubuntu",       "description": "Shell scripts to automate Node.js 22 installation and package setup on Ubuntu servers."},
]

PROJECT_TAGS: dict[str, list[str]] = {
    "possy-backend":     ["TypeScript", "Node.js", "REST API", "POS"],
    "resume-sivakorn":   ["React", "TypeScript", "Vite", "Portfolio"],
    "face-scan":         ["Python", "TensorFlow", "AI", "GPU"],
    "chatbot-service":   ["Python", "Chatbot", "API"],
    "bookdev-tecnology": ["Python"],
    "angular-app":       ["TypeScript", "Angular"],
    "fivem-bookdev":     ["Lua", "FiveM", "GTA V"],
    "install-node22":    ["Shell", "Ubuntu", "Node.js", "DevOps"],
}

# ── Education subjects ──────────────────────────────────────────────────────

EDUCATION_SUBJECTS = [
    {"lang": "th", "position": 0, "label": "แกนหลัก",    "value": "อัลกอริทึม, โครงสร้างข้อมูล, สถาปัตยกรรมคอมพิวเตอร์"},
    {"lang": "th", "position": 1, "label": "AI & ML",    "value": "การเรียนรู้ของเครื่อง, การเรียนรู้เชิงลึก, การประเมินโมเดล"},
    {"lang": "th", "position": 2, "label": "ระบบ IoT",   "value": "เซนเซอร์, Edge Computing, เครือข่าย"},
    {"lang": "th", "position": 3, "label": "วงจรไฟฟ้า",  "value": "วงจรอะนาล็อก/ดิจิทัล, พื้นฐานสัญญาณ"},
    {"lang": "th", "position": 4, "label": "ระบบฝังตัว", "value": "ไมโครคอนโทรลเลอร์, พื้นฐาน PCB, I/O แบบเรียลไทม์"},
    {"lang": "th", "position": 5, "label": "โปรเจกต์",   "value": "ต้นแบบ AI, แดชบอร์ด IoT, ระบบอัตโนมัติ"},
    {"lang": "en", "position": 0, "label": "Core",               "value": "Algorithms, Data Structures, Computer Architecture"},
    {"lang": "en", "position": 1, "label": "AI & ML",            "value": "Machine Learning, Deep Learning, Model Evaluation"},
    {"lang": "en", "position": 2, "label": "IoT Systems",        "value": "Sensors, Edge Computing, Networking"},
    {"lang": "en", "position": 3, "label": "Electrical Circuits", "value": "Analog/Digital Circuits, Signal Basics"},
    {"lang": "en", "position": 4, "label": "Embedded",           "value": "Microcontrollers, PCB basics, Real-time I/O"},
    {"lang": "en", "position": 5, "label": "Projects",           "value": "AI-driven prototypes, IoT dashboards, automation"},
]

# ── Skill categories ────────────────────────────────────────────────────────

SKILL_CATEGORIES = [
    {"lang": "th", "position": 0, "title": "ภาษาโปรแกรม",           "description": "ภาษาโปรแกรมมิ่งและสคริปต์ที่ผมใช้งาน"},
    {"lang": "th", "position": 1, "title": "เฟรมเวิร์ก",             "description": "เฟรมเวิร์กและแพลตฟอร์มที่ผมใช้สร้างระบบที่ยืดหยุ่น"},
    {"lang": "th", "position": 2, "title": "ฐานข้อมูล",              "description": "ฐานข้อมูลที่ผมออกแบบและปรับปรุงในระบบ production"},
    {"lang": "th", "position": 3, "title": "DevOps & Infrastructure", "description": "เครื่องมือที่ผมใช้ deploy, scale และดำเนินการระบบ"},
    {"lang": "th", "position": 4, "title": "เครื่องมือ",             "description": "เครื่องมือพัฒนาและดีบักที่ผมใช้ทุกวัน"},
    {"lang": "en", "position": 0, "title": "Languages",               "description": "Programming and scripting languages I work with."},
    {"lang": "en", "position": 1, "title": "Frameworks",              "description": "Frameworks and platforms I use to build scalable systems."},
    {"lang": "en", "position": 2, "title": "Databases",               "description": "Databases I design and optimize in production systems."},
    {"lang": "en", "position": 3, "title": "DevOps & Infrastructure", "description": "Tools I use to deploy, scale and operate systems."},
    {"lang": "en", "position": 4, "title": "Tools",                   "description": "Development and debugging tools I use every day."},
]

# ── Seed logic ──────────────────────────────────────────────────────────────

def seed():
    with engine.begin() as conn:

        # 1. locale_strings
        print("  → locale_strings ...")
        conn.execute(text("""
            INSERT INTO locale_strings (lang, section, key, value)
            VALUES (:lang, :section, :key, :value)
            ON CONFLICT (lang, section, key) DO UPDATE SET value = EXCLUDED.value
        """), [{"lang": l, "section": s, "key": k, "value": v} for l, s, k, v in STRINGS])

        # 2. experience_entries
        print("  → experience_entries ...")
        conn.execute(text("""
            INSERT INTO experience_entries (slug, logo, period, is_current)
            VALUES (:slug, :logo, :period, :is_current)
            ON CONFLICT (slug) DO UPDATE SET
                logo = EXCLUDED.logo,
                period = EXCLUDED.period,
                is_current = EXCLUDED.is_current
        """), EXPERIENCES)

        # 3. experience_translations
        print("  → experience_translations ...")
        rows = conn.execute(text("SELECT id, slug FROM experience_entries")).fetchall()
        exp_id = {r.slug: r.id for r in rows}
        conn.execute(text("""
            INSERT INTO experience_translations (experience_id, lang, company, role, description)
            VALUES (:experience_id, :lang, :company, :role, :description)
            ON CONFLICT (experience_id, lang) DO UPDATE SET
                company = EXCLUDED.company, role = EXCLUDED.role, description = EXCLUDED.description
        """), [{**t, "experience_id": exp_id[t["slug"]]} for t in EXPERIENCE_TRANSLATIONS])

        # 4. experience_responsibilities
        print("  → experience_responsibilities ...")
        conn.execute(text("""
            INSERT INTO experience_responsibilities (experience_id, lang, position, text)
            VALUES (:experience_id, :lang, :position, :text)
            ON CONFLICT (experience_id, lang, position) DO UPDATE SET text = EXCLUDED.text
        """), [{**r, "experience_id": exp_id[r["slug"]]} for r in EXPERIENCE_RESPONSIBILITIES])

        # 5. projects
        print("  → projects ...")
        conn.execute(text("""
            INSERT INTO projects (slug, lang_code, stars, is_private, url)
            VALUES (:slug, :lang_code, :stars, :is_private, :url)
            ON CONFLICT (slug) DO UPDATE SET
                lang_code = EXCLUDED.lang_code,
                stars = EXCLUDED.stars,
                is_private = EXCLUDED.is_private,
                url = EXCLUDED.url
        """), PROJECTS)

        # 6. project_translations
        print("  → project_translations ...")
        rows = conn.execute(text("SELECT id, slug FROM projects")).fetchall()
        proj_id = {r.slug: r.id for r in rows}
        conn.execute(text("""
            INSERT INTO project_translations (project_id, lang, name, description)
            VALUES (:project_id, :lang, :name, :description)
            ON CONFLICT (project_id, lang) DO UPDATE SET
                name = EXCLUDED.name, description = EXCLUDED.description
        """), [{**t, "project_id": proj_id[t["slug"]]} for t in PROJECT_TRANSLATIONS])

        # 7. project_tags
        print("  → project_tags ...")
        tag_rows = [
            {"project_id": proj_id[slug], "tag": tag}
            for slug, tags in PROJECT_TAGS.items()
            for tag in tags
        ]
        conn.execute(text("""
            INSERT INTO project_tags (project_id, tag)
            VALUES (:project_id, :tag)
            ON CONFLICT (project_id, tag) DO NOTHING
        """), tag_rows)

        # 8. education_subjects
        print("  → education_subjects ...")
        conn.execute(text("""
            INSERT INTO education_subjects (lang, position, label, value)
            VALUES (:lang, :position, :label, :value)
            ON CONFLICT (lang, position) DO UPDATE SET
                label = EXCLUDED.label, value = EXCLUDED.value
        """), EDUCATION_SUBJECTS)

        # 9. skill_categories
        print("  → skill_categories ...")
        conn.execute(text("""
            INSERT INTO skill_categories (lang, position, title, description)
            VALUES (:lang, :position, :title, :description)
            ON CONFLICT (lang, position) DO UPDATE SET
                title = EXCLUDED.title, description = EXCLUDED.description
        """), SKILL_CATEGORIES)

    print("Seed complete.")


if __name__ == "__main__":
    print("Seeding locale data ...")
    seed()
