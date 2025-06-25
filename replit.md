# Portfolio Website

## Overview

This is a modern, dark-themed portfolio website for a full-stack developer named Harsh. The application is built using Flask (Python) for the backend with a responsive frontend featuring smooth animations, contact form functionality, and email integration. The website showcases skills, projects, and provides a way for visitors to download a resume and contact the developer.

## System Architecture

The application follows a simple Flask web application architecture with the following key characteristics:

- **Backend Framework**: Flask (Python 3.11)
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap 5 framework
- **Email Service**: Flask-Mail for contact form submissions
- **Deployment**: Gunicorn WSGI server with autoscaling capability
- **Static Assets**: CSS, JavaScript, and PDF resume served through Flask's static file handling

## Key Components

### Backend Components

1. **Application Factory (`app.py`)**
   - Flask application initialization
   - Email configuration with environment variable support
   - Session management with secret key
   - ProxyFix middleware for proper header handling behind proxies

2. **Route Handlers (`routes.py`)**
   - Home page rendering
   - Contact form processing with email sending
   - Resume download endpoint (incomplete)
   - Flash message system for user feedback

3. **Entry Point (`main.py`)**
   - Application startup for both development and production

### Frontend Components

1. **Template System**
   - Single-page application with `index.html` template
   - Bootstrap 5 for responsive design
   - Google Fonts integration (Poppins)
   - Font Awesome icons

2. **Styling (`static/css/style.css`)**
   - CSS custom properties for theming
   - Dark theme with purple gradient accents
   - Responsive design principles
   - Modern animations and transitions

3. **Interactive Features (`static/js/main.js`)**
   - Loading spinner functionality
   - Scroll progress indicator
   - Smooth scrolling navigation
   - Typing effects for dynamic content
   - Contact form validation and submission

## Data Flow

### Contact Form Flow
1. User fills out contact form (name, email, message)
2. Form data is submitted via POST to `/contact` endpoint
3. Server validates required fields
4. Email is composed and sent via Flask-Mail
5. Success/error flash message is set
6. User is redirected back to home page with feedback

### Static Content Flow
1. CSS, JavaScript, and asset files are served through Flask's static file handler
2. Resume PDF is available for download at `/download-resume` endpoint
3. All static assets are cached by the browser for performance

## External Dependencies

### Python Packages
- **Flask**: Web framework and routing
- **Flask-Mail**: Email sending functionality
- **Flask-SQLAlchemy**: Database ORM (configured but not actively used)
- **Gunicorn**: Production WSGI server
- **psycopg2-binary**: PostgreSQL adapter (available but not used)
- **email-validator**: Email validation utilities
- **Werkzeug**: WSGI utilities and development server

### Frontend Dependencies (CDN)
- **Bootstrap 5**: CSS framework for responsive design
- **Font Awesome 6**: Icon library
- **Google Fonts**: Poppins font family

### Email Service
- Configured for Gmail SMTP by default
- Environment variables for email credentials
- Fallback to logging when email service is not configured

## Deployment Strategy

### Production Configuration
- **Server**: Gunicorn with autoscaling deployment target
- **Binding**: All interfaces (0.0.0.0) on port 5000
- **Process Management**: Gunicorn handles worker processes
- **Proxy Support**: ProxyFix middleware for proper header handling

### Environment Variables
- `SESSION_SECRET`: Session encryption key
- `MAIL_SERVER`: SMTP server (default: smtp.gmail.com)
- `MAIL_PORT`: SMTP port (default: 587)
- `MAIL_USERNAME`: Email username
- `MAIL_PASSWORD`: Email password
- `MAIL_DEFAULT_SENDER`: Default sender email

### Development vs Production
- Development uses Flask's built-in server with debug mode
- Production uses Gunicorn with reuse-port and reload options
- Environment-based configuration for email and session secrets

## Changelog

- June 25, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.