# AI Context — Resume-Sivakorn Portfolio
> **ภาษาไทย** อยู่ด้านล่าง | **English** version is first

---

# 🇬🇧 ENGLISH

## About This Project

This is a personal portfolio and resume website for **Sivakorn Tanyupak (Book)**, a Full Stack Developer from Thailand.
The site serves as an online CV, showcasing skills, work experience, and contact information.

- **Live URL:** https://bookdev-vite-react.vercel.app/
- **Repository:** Private (local dev at `d:/BookDev/Resume-Sivakorn`)
- **Deployed on:** Vercel
- **Git branch:** `main`

---

## Owner — Personal Information

| Field         | Value                                              |
|---------------|----------------------------------------------------|
| Full Name     | Sivakorn Tanyupak                                  |
| Nickname      | Book (บุ๊ค)                                        |
| Date of Birth | March 17, 2001 (24 years old)                      |
| Address       | Ko Yao, Phang Nga 83000, Thailand                  |
| Email         | sivakorn.987@gmail.com                             |
| Phone         | 065-840-6400                                       |
| GitHub        | https://github.com/Sivakorn63110548                |
| Instagram     | @bookkkk_7 — https://www.instagram.com/bookkkk_7/ |
| Facebook      | https://www.facebook.com/sivakorn.tanyupak.7/      |
| LinkedIn      | https://www.linkedin.com/                          |

---

## Education

- **Degree:** Bachelor of Engineering (Computer Engineering & Intelligent Systems)
- **University:** Walailak University (มหาวิทยาลัยวลัยลักษณ์)
- **Bio:** Studied modern computing disciplines with a strong foundation in mathematics and electronics, focusing on building intelligent, connected systems.

### Subjects Covered

| Area               | Topics                                                          |
|--------------------|-----------------------------------------------------------------|
| Core               | Algorithms, Data Structures, Computer Architecture             |
| AI & ML            | Machine Learning, Deep Learning, Model Evaluation              |
| IoT Systems        | Sensors, Edge Computing, Networking                            |
| Electrical Circuits| Analog/Digital Circuits, Signal Basics                         |
| Embedded Systems   | Microcontrollers, PCB basics, Real-time I/O                    |
| Projects           | AI-driven prototypes, IoT dashboards, automation systems       |

---

## Technical Skills

### Languages
JavaScript, TypeScript, Python, PHP, HTML, CSS, Bash

### Frameworks & Platforms
React, Next.js, NestJS, Node.js, Elysia, Laravel, Angular, CodeIgniter 3, FastAPI

### Databases
MySQL, PostgreSQL, MongoDB, Redis

### DevOps & Infrastructure
Docker, Linux, Git, Nginx, AWS / Cloud

### Tools
Postman, VS Code, Figma

---

## Work Experience

### 1. Hospitality Technology Platform (2023 – 2024)
**Role:** Full-Stack Developer

**Description:**
Developed and maintained technology platforms for hotels and restaurant operations, focusing on building reliable systems that support real hospitality workflows.

**Responsibilities:**
- Hotel Property Management Systems (PMS)
- OTA integrations for booking synchronization
- Restaurant order and transaction systems
- Payment processing and transaction handling
- Backend API and database architecture
- Reporting dashboards for hotel operations

**Tech Stack:** React, Node.js, MySQL, REST API, OTA

---

### 2. Real Estate & Villa Rental Platform (2024 – Present) ← CURRENT JOB
**Role:** Full-Stack Developer & System Architect

**Description:**
Designing and building scalable platforms for a real estate company specialising in villa sales and rental management. Systems cover property listings, reservation management, OTA integrations, payment processing, and financial tracking.

**Location (main company):** Bookengine.com, Bangkok (coordinates: 13.8058462, 100.5020719)
**Working onsite at:** Santhiya Koh Yao Yai Resort & Spa, Phang Nga (coordinates: 7.9873156, 98.5667578)

**Responsibilities:**
- Villa rental and property management systems
- OTA integrations for booking channels
- Booking and reservation platforms
- Payment processing and transaction management
- Accounting and financial reporting systems
- Internal management dashboards
- Backend architecture and database design

**Tech Stack:** React, NestJS, MongoDB, TypeScript, OTA, Finance systems

---

## Tech Stack (Project)

| Layer         | Technology                                                       |
|---------------|------------------------------------------------------------------|
| Frontend      | React 18, TypeScript, Vite 6                                     |
| UI Library    | MUI (Material UI v6) + MUI Icons                                 |
| Animation     | Framer Motion 11                                                 |
| Routing       | React Router DOM v7                                              |
| Styling       | CSS (per-component) + Tailwind CSS 3                             |
| i18n          | Custom React Context (English / Thai)                            |
| Theme         | Custom React Context (Dark / Light, persisted in localStorage)   |
| Email         | EmailJS (`emailjs-com`)                                          |
| Map           | React-Leaflet + Leaflet (OpenStreetMap)                          |
| Build Tool    | Vite 6                                                           |
| Linting       | ESLint 9 + typescript-eslint                                     |
| Deployment    | Vercel                                                           |

---

## Project File Structure

```
d:/BookDev/Resume-Sivakorn/
├── index.html
├── package.json
├── vite.config.ts
├── tailwind.config.js
├── tsconfig.json / tsconfig.app.json / tsconfig.node.json
├── eslint.config.js
├── vercel.json
│
├── public/
│   └── BookDev_logo.png
│
└── src/
    ├── main.tsx                    # App entry point
    ├── App.tsx                     # Root component — providers + router
    ├── index.css                   # Global base styles
    ├── App.css
    │
    ├── page/
    │   └── Home.tsx                # Single page: Hero → About → Skill → Experience → Contact
    │
    ├── component/
    │   ├── about_me.tsx            # About section: profile photo, bio, birth date, address, education
    │   ├── Skill.tsx               # Skills: 5 tab categories, icon grid with external doc links
    │   ├── Experience.tsx          # Work experience: 2 cards with tags + responsibilities
    │   ├── contact.tsx             # Contact: copy email/phone, open social links
    │   ├── Loading.tsx             # Full-screen animated robot loading screen
    │   ├── Language.tsx            # Language switcher component
    │   ├── Job_future.tsx          # (future) job preference component
    │   ├── SentMail.tsx            # Class component — send resume via EmailJS, download PDF
    │   └── map.tsx                 # Leaflet map: home pin, Santhiya resort pin, Bookengine pin
    │
    ├── topbar/
    │   ├── Topbar.tsx              # Fixed AppBar: logo, nav, scroll-spy, dark/light, lang, PDF modal
    │   └── Topbar.css
    │
    ├── i18n/
    │   └── LangContext.tsx         # LangProvider + useLang() — en/th, persisted in localStorage
    │
    ├── locales/
    │   ├── en.json                 # All English UI text
    │   └── th.json                 # All Thai UI text
    │
    ├── theme/
    │   └── ThemeContext.tsx        # ThemeProvider + useTheme() — dark/light, persisted in localStorage
    │
    ├── css/
    │   ├── Home.css
    │   └── component/
    │       ├── About_me.css
    │       ├── Contact.css
    │       ├── Experience.css
    │       └── Skill.css
    │
    ├── utils/
    │   └── motion.ts               # Framer Motion variants: fadeUp, fadeIn, slideLeft, slideRight,
    │                               #   cardPop, iconPop, stagger, headerContainer, eyebrowVariant,
    │                               #   titleVariant, subVariant
    │
    ├── vite-env.d.ts
    │
    └── assets/
        ├── Profile.png             # Owner's profile photo
        ├── Book.png                # Hero section avatar
        ├── Book2.png
        ├── BookDev_logo.png        # Topbar logo
        ├── wu_logo.png             # Walailak University logo
        ├── Background.jpg          # Background for SentMail section
        ├── logo.png
        ├── react.svg
        ├── backgrond_card.png
        ├── file/
        │   └── Resume_Sivakorn.pdf # Downloadable resume PDF
        └── icon/                   # Tech stack logos (PNG)
            ├── JavaScript-logo.png
            ├── typescript.png
            ├── python.png
            ├── php.png
            ├── html.png / css-3.png / bash.png
            ├── react.png / nextjs.png / nestjs.png
            ├── nodejs.png / elysia.png / laravel.png
            ├── angular.png / ci3.png / fastapi.png
            ├── mysql.png / postgresql.png / mongodbpng.png / redis.png
            ├── docker.png / linux.png / git.png / nginx.png / aws.png
            ├── postman.png / vscode.png / figma.png
            ├── home.png / sty.png / beg.png  ← map marker icons
            ├── th.png / th.svg / us.png / us.svg  ← language flag icons
            └── eng.png / beg.png
```

---

## Page Sections & Routing

```
/        → redirect to /home
/home    → Full single-page with anchor sections:
           #home       — Hero: greeting, name, role, description, experience stat
           #about      — About Me: photo, bio, birth date, address + Education card
           #skill      — Technical Skills: tabbed categories
           #experience — Work Experience: 2 cards
           #contact    — Contact: icon buttons + social links
```

---

## Key Features

| Feature                | Details                                                                           |
|------------------------|-----------------------------------------------------------------------------------|
| Scroll-spy nav         | IntersectionObserver highlights active nav item as user scrolls                  |
| Smooth scroll          | Scroll to section with topbar offset on nav click                                |
| Scroll progress bar    | LinearProgress in topbar shows reading progress (0–100%)                         |
| Dark / Light theme     | Toggle button in topbar, uses `data-theme` on `<html>`, persisted in localStorage|
| Language switch EN/TH  | Custom flag SVG dropdown, persisted in localStorage                              |
| Resume PDF modal       | Dialog with iframe preview, open-in-new-tab, and download buttons                |
| Framer Motion anims    | scroll-triggered entry animations on all sections                                |
| Mobile responsive      | Burger menu on <900px, collapses to slide-down panel                             |
| Skills tabs            | 5 categories: Languages / Frameworks / Databases / DevOps / Tools                |
| Contact copy           | Click email or phone icon to copy to clipboard                                   |
| Leaflet map            | 3 markers: home, current work site, main company HQ                              |
| EmailJS integration    | SentMail component sends resume PDF link to entered email                        |

---

## Framer Motion Variants (src/utils/motion.ts)

| Variant          | Behavior                              |
|------------------|---------------------------------------|
| `fadeUp`         | opacity 0→1, y +36→0                  |
| `fadeIn`         | opacity 0→1                           |
| `slideLeft`      | opacity 0→1, x -48→0                  |
| `slideRight`     | opacity 0→1, x +48→0                  |
| `cardPop`        | opacity 0→1, y +32→0, scale 0.96→1   |
| `iconPop`        | opacity 0→1, scale 0.6→1 (spring)    |
| `stagger(delay)` | staggerChildren container             |
| `headerContainer`| stagger 0.12s for section headers    |
| `eyebrowVariant` | y +16→0 fade                          |
| `titleVariant`   | y +24→0 fade                          |
| `subVariant`     | y +18→0 fade                          |

All scroll-triggered variants use `viewport: { once: true, margin: '-80px' }`.

---

## Coding Conventions

1. **All UI text** → always in `src/locales/en.json` and `th.json`, never hardcoded in components
2. **Framer Motion** → reuse variants from `src/utils/motion.ts`, do not inline new variants in components
3. **Theme** → applied via `data-theme` attribute on `<html>` element, not via class names
4. **CSS** → per-component files in `src/css/component/`, global in `src/index.css`
5. **Assets** → imported directly via ES module imports in components (not via `public/`)
6. **i18n hook** → `const { locale } = useLang()` — always destructure `locale` from context
7. **Theme hook** → `const { theme, toggleTheme } = useTheme()`
8. **Sections** → use `id="sectionName"` for scroll-spy anchors (`home`, `about`, `skill`, `experience`, `contact`)
9. **New components** → place in `src/component/`, add CSS in `src/css/component/`

---

---

# 🇹🇭 ภาษาไทย

## เกี่ยวกับโปรเจกต์นี้

เว็บไซต์พอร์ตโฟลิโอและเรซูเม่ส่วนตัวของ **ศิวกร ทันยุภักดิ์ (บุ๊ค)** นักพัฒนา Full Stack จากประเทศไทย
ใช้เป็น CV ออนไลน์ แสดงทักษะ ประสบการณ์ทำงาน และช่องทางติดต่อ

- **ลิงก์เว็บจริง:** https://bookdev-vite-react.vercel.app/
- **Deploy บน:** Vercel
- **Git branch:** `main`

---

## เจ้าของ — ข้อมูลส่วนตัว

| ฟิลด์          | ข้อมูล                                              |
|----------------|-----------------------------------------------------|
| ชื่อ-นามสกุล   | ศิวกร ทันยุภักดิ์                                   |
| ชื่อเล่น       | บุ๊ค (Book)                                         |
| วันเกิด        | 17 มีนาคม 2544 (อายุ 24 ปี)                         |
| ที่อยู่         | เกาะยาว พังงา 83000                                 |
| อีเมล          | sivakorn.987@gmail.com                              |
| โทรศัพท์       | 065-840-6400                                        |
| GitHub         | https://github.com/Sivakorn63110548                 |
| Instagram      | @bookkkk_7 — https://www.instagram.com/bookkkk_7/  |
| Facebook       | https://www.facebook.com/sivakorn.tanyupak.7/       |
| LinkedIn       | https://www.linkedin.com/                           |

---

## การศึกษา

- **วุฒิการศึกษา:** วิศวกรรมศาสตรบัณฑิต สาขาวิศวกรรมคอมพิวเตอร์และระบบอัจฉริยะ
- **มหาวิทยาลัย:** มหาวิทยาลัยวลัยลักษณ์ (Walailak University)
- **ชีวประวัติการเรียน:** ศึกษาวิชาการคอมพิวเตอร์สมัยใหม่บนพื้นฐานที่แข็งแกร่งด้านคณิตศาสตร์และอิเล็กทรอนิกส์ โดยเน้นการสร้างระบบอัจฉริยะที่เชื่อมต่อกัน

### วิชาที่เรียน

| ด้าน                | เนื้อหา                                                           |
|---------------------|-------------------------------------------------------------------|
| แกนหลัก             | อัลกอริทึม, โครงสร้างข้อมูล, สถาปัตยกรรมคอมพิวเตอร์            |
| AI & ML             | การเรียนรู้ของเครื่อง, การเรียนรู้เชิงลึก, การประเมินโมเดล       |
| ระบบ IoT            | เซนเซอร์, Edge Computing, เครือข่าย                               |
| วงจรไฟฟ้า           | วงจรอะนาล็อก/ดิจิทัล, พื้นฐานสัญญาณ                             |
| ระบบฝังตัว          | ไมโครคอนโทรลเลอร์, พื้นฐาน PCB, I/O แบบเรียลไทม์               |
| โปรเจกต์            | ต้นแบบ AI, แดชบอร์ด IoT, ระบบอัตโนมัติ                          |

---

## ทักษะทางเทคนิค

### ภาษาโปรแกรม
JavaScript, TypeScript, Python, PHP, HTML, CSS, Bash

### เฟรมเวิร์กและแพลตฟอร์ม
React, Next.js, NestJS, Node.js, Elysia, Laravel, Angular, CodeIgniter 3, FastAPI

### ฐานข้อมูล
MySQL, PostgreSQL, MongoDB, Redis

### DevOps & Infrastructure
Docker, Linux, Git, Nginx, AWS / Cloud

### เครื่องมือ
Postman, VS Code, Figma

---

## ประสบการณ์ทำงาน

### 1. Hospitality Technology Platform (2566 – 2567)
**ตำแหน่ง:** นักพัฒนา Full-Stack

**รายละเอียด:**
พัฒนาและดูแลแพลตฟอร์มเทคโนโลยีสำหรับโรงแรมและร้านอาหาร มุ่งเน้นการสร้างระบบที่เชื่อถือได้สำหรับขั้นตอนงานด้านการบริการ
งานรวมถึง Property Management System (PMS), การจัดการการจอง, ระบบธุรกรรมร้านอาหาร, การเชื่อมต่อ OTA และแดชบอร์ดการดำเนินงาน

**ความรับผิดชอบ:**
- ระบบบริหารจัดการโรงแรม (PMS)
- การเชื่อมต่อ OTA สำหรับซิงค์การจอง
- ระบบสั่งอาหารและธุรกรรมร้านอาหาร
- การประมวลผลการชำระเงินและธุรกรรม
- สถาปัตยกรรม Backend API และฐานข้อมูล
- แดชบอร์ดรายงานการดำเนินงานโรงแรม

**Tech Stack:** React, Node.js, MySQL, REST API, OTA

---

### 2. Real Estate & Villa Rental Platform (2567 – ปัจจุบัน) ← งานปัจจุบัน
**ตำแหน่ง:** นักพัฒนา Full-Stack & สถาปนิกระบบ

**รายละเอียด:**
ออกแบบและสร้างแพลตฟอร์มที่ยืดหยุ่นสำหรับบริษัทอสังหาริมทรัพย์ที่เชี่ยวชาญด้านการขายและบริหารวิลล่าให้เช่า
ระบบครอบคลุมรายการทรัพย์สิน, การบริหารการจอง, การเชื่อมต่อ OTA, การประมวลผลการชำระเงิน และการติดตามทางการเงิน

**ที่ตั้งบริษัทหลัก:** Bookengine.com กรุงเทพฯ (พิกัด: 13.8058462, 100.5020719)
**ทำงาน onsite ที่:** Santhiya Koh Yao Yai Resort & Spa พังงา (พิกัด: 7.9873156, 98.5667578)

**ความรับผิดชอบ:**
- ระบบบริหารการเช่าวิลล่าและจัดการทรัพย์สิน
- การเชื่อมต่อ OTA สำหรับช่องทางการจอง
- แพลตฟอร์มการจองและการสำรอง
- การประมวลผลการชำระเงินและการจัดการธุรกรรม
- ระบบบัญชีและรายงานทางการเงิน
- แดชบอร์ดการจัดการภายใน
- สถาปัตยกรรม Backend และการออกแบบฐานข้อมูล

**Tech Stack:** React, NestJS, MongoDB, TypeScript, OTA, ระบบการเงิน

---

## Tech Stack ของโปรเจกต์นี้

| Layer         | เทคโนโลยี                                                        |
|---------------|------------------------------------------------------------------|
| Frontend      | React 18, TypeScript, Vite 6                                     |
| UI Library    | MUI (Material UI v6) + MUI Icons                                 |
| Animation     | Framer Motion 11                                                 |
| Routing       | React Router DOM v7                                              |
| Styling       | CSS (แยกต่อ component) + Tailwind CSS 3                          |
| i18n          | Custom React Context (ไทย / อังกฤษ)                             |
| Theme         | Custom React Context (Dark / Light, เก็บใน localStorage)         |
| Email         | EmailJS (`emailjs-com`)                                          |
| Map           | React-Leaflet + Leaflet (OpenStreetMap)                          |
| Build Tool    | Vite 6                                                           |
| Deployment    | Vercel                                                           |

---

## โครงสร้างไฟล์

```
src/
├── main.tsx                    # Entry point ของแอป
├── App.tsx                     # Root component — providers + router setup
├── index.css / App.css         # Global styles
│
├── page/
│   └── Home.tsx                # หน้าเดียว: Hero → About → Skill → Experience → Contact
│
├── component/
│   ├── about_me.tsx            # ส่วน About: รูปโปรไฟล์, ชีวประวัติ, วันเกิด, ที่อยู่, การศึกษา
│   ├── Skill.tsx               # ส่วน Skills: 5 หมวด tab, กริดไอคอนพร้อมลิงก์เอกสารทางการ
│   ├── Experience.tsx          # ส่วน Experience: 2 การ์ดงาน + tag เทคโนโลยี + ความรับผิดชอบ
│   ├── contact.tsx             # ส่วน Contact: คัดลอกอีเมล/เบอร์, เปิด social links
│   ├── Loading.tsx             # หน้า loading เต็มจอ — หุ่นยนต์เดินแบบ CSS animation
│   ├── Language.tsx            # Component เปลี่ยนภาษา
│   ├── Job_future.tsx          # (อนาคต) component แสดงความต้องการงาน
│   ├── SentMail.tsx            # Class component — ส่งลิงก์ resume ผ่าน EmailJS, ดาวน์โหลด PDF
│   └── map.tsx                 # แผนที่ Leaflet: หมุดบ้าน, หมุด Santhiya Resort, หมุด Bookengine
│
├── topbar/
│   ├── Topbar.tsx              # AppBar ตรึงบน: โลโก้, nav, scroll-spy, dark/light,
│   │                           #   dropdown ภาษา (ธงชาติ EN/TH), modal PDF resume
│   └── Topbar.css
│
├── i18n/
│   └── LangContext.tsx         # LangProvider + useLang() — en/th, บันทึกใน localStorage
│
├── locales/
│   ├── en.json                 # ข้อความ UI ภาษาอังกฤษทั้งหมด
│   └── th.json                 # ข้อความ UI ภาษาไทยทั้งหมด
│
├── theme/
│   └── ThemeContext.tsx        # ThemeProvider + useTheme() — dark/light, บันทึกใน localStorage
│
├── css/
│   ├── Home.css
│   └── component/
│       ├── About_me.css
│       ├── Contact.css
│       ├── Experience.css
│       └── Skill.css
│
├── utils/
│   └── motion.ts               # Framer Motion variants รวมศูนย์
│
└── assets/
    ├── Profile.png             # รูปโปรไฟล์ของเจ้าของ
    ├── Book.png / Book2.png    # Avatar ส่วน Hero
    ├── BookDev_logo.png        # โลโก้ใน Topbar
    ├── wu_logo.png             # โลโก้มหาวิทยาลัยวลัยลักษณ์
    ├── Background.jpg          # พื้นหลัง SentMail
    ├── file/
    │   └── Resume_Sivakorn.pdf # PDF resume ดาวน์โหลดได้
    └── icon/                   # โลโก้เทคโนโลยีทั้งหมด (PNG)
```

---

## Sections และ Routing

```
/        → redirect ไปที่ /home
/home    → Single-page พร้อม anchor sections:
           #home       — Hero: ทักทาย, ชื่อ, ตำแหน่ง, คำอธิบาย, สถิติประสบการณ์
           #about      — About Me: รูป, ชีวประวัติ, วันเกิด, ที่อยู่ + การ์ดการศึกษา
           #skill      — Technical Skills: หมวด tab ทักษะ
           #experience — Work Experience: 2 การ์ดงาน
           #contact    — Contact: ไอคอน + social links
```

---

## ฟีเจอร์หลัก

| ฟีเจอร์                   | รายละเอียด                                                                         |
|---------------------------|------------------------------------------------------------------------------------|
| Scroll-spy navigation     | IntersectionObserver ไฮไลต์ nav ตาม section ที่กำลังดู                           |
| Smooth scroll             | เลื่อนไปยัง section พร้อม offset ของ topbar                                       |
| Scroll progress bar       | LinearProgress ใน topbar แสดงความคืบหน้าการอ่าน (0–100%)                          |
| Dark / Light theme        | ปุ่ม toggle ใน topbar, ใช้ `data-theme` บน `<html>`, บันทึกใน localStorage        |
| เปลี่ยนภาษา EN/TH         | dropdown ธงชาติ SVG สร้างเอง, บันทึกใน localStorage                              |
| Resume PDF modal          | Dialog พร้อม iframe preview, เปิดในแท็บใหม่, และปุ่มดาวน์โหลด                   |
| Framer Motion animations  | animation scroll-triggered บนทุก section                                           |
| Mobile responsive         | เมนู Burger <900px, พับลงเป็น panel แบบ slide-down                               |
| Skills tabs               | 5 หมวด: Languages / Frameworks / Databases / DevOps / Tools                       |
| Copy contact              | คลิกไอคอน email หรือ phone เพื่อ copy to clipboard                                |
| แผนที่ Leaflet             | 3 หมุด: บ้าน, ที่ทำงาน onsite, บริษัทหลัก                                       |
| EmailJS integration       | SentMail ส่งลิงก์ resume PDF ไปยัง email ที่กรอก                                 |

---

## Convention การเขียนโค้ด

1. **ข้อความ UI ทั้งหมด** → ต้องอยู่ใน `src/locales/en.json` และ `th.json` เท่านั้น ห้าม hardcode ใน component
2. **Framer Motion** → ใช้ variants จาก `src/utils/motion.ts` ห้าม inline variants ใหม่ใน component
3. **Theme** → apply ผ่าน `data-theme` attribute บน `<html>` ไม่ใช่ class name
4. **CSS** → แยกไฟล์ต่อ component ใน `src/css/component/`, global ใน `src/index.css`
5. **Assets** → import โดยตรงผ่าน ES module ใน component (ไม่ใช้ `public/`)
6. **i18n hook** → `const { locale } = useLang()` — destructure `locale` จาก context เสมอ
7. **Theme hook** → `const { theme, toggleTheme } = useTheme()`
8. **Anchor sections** → ใช้ `id="sectionName"` สำหรับ scroll-spy (`home`, `about`, `skill`, `experience`, `contact`)
9. **Component ใหม่** → วางใน `src/component/`, CSS ใน `src/css/component/`
