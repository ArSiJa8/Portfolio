# ArSiJa Portfolio

## Overview

A static portfolio website showcasing Blender animations and thumbnail creation work. Built with vanilla HTML, CSS, and JavaScript following a dark, modern glassmorphism design aesthetic inspired by Apple's liquid glass UI patterns.

The site consists of multiple pages (Home, About, Contact, Projects) with a consistent navigation structure, responsive layout, and smooth scroll-reveal animations.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack:**
- Pure HTML5, CSS3, and vanilla JavaScript
- No frontend frameworks or build tools required
- Single shared stylesheet (`styles.css`) across all pages
- Single shared script file (`script.js`) for interactivity

**Design System:**
- CSS custom properties (variables) for consistent theming in `:root`
- Glassmorphism effects using `backdrop-filter`, transparency, and blur
- Dark color palette with accent colors defined in variables
- Responsive design with mobile hamburger navigation

**Page Structure:**
- Root `index.html` serves as the main landing page with hero section
- Subdirectories (`About/`, `Contact/`, `Projects/`) each contain their own `index.html`
- All pages share the same header navigation and footer structure
- Relative paths (`../styles.css`) used for stylesheet references in subdirectories

**JavaScript Features:**
- Hamburger menu toggle for mobile navigation
- Intersection Observer-based scroll reveal animations
- Staggered animation delays for visual polish

### Development Server

**Local Development:**
- Python's built-in HTTP server (`server.py`) on port 5000
- Custom handler adds no-cache headers for development convenience
- Binds to `0.0.0.0` for external access (Replit compatibility)

### File Organization

```
/                    → Root directory (serves as public)
├── index.html       → Main landing page
├── styles.css       → Global stylesheet
├── script.js        → Shared JavaScript
├── server.py        → Development server
├── 404.html         → Custom error page
├── About/index.html → About page
├── Contact/index.html → Contact page
├── Projects/index.html → Projects page
└── css/css-test/    → CSS component testing page
```

## External Dependencies

### Third-Party Services

**Social Media Integration:**
- YouTube channel link (`youtube.com/@aArSiJa`)
- GitHub repository link (`github.com/ArSiJa8/Portfolio`)

### Static Assets

- Favicon files (`favicon.svg`, `favicon-96x96.png`) expected in root
- Background image (`wallpaper.jpg`) for hero section

### Deployment Compatibility

The project is designed as a fully static site compatible with:
- GitHub Pages
- Railway
- Replit static hosting
- Any static file server

No database, backend API, or build process required. The Python server is purely for local development convenience.