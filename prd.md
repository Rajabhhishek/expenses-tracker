Product Requirements Document (PRD)
Wisdom School Expense Tracker System
1. Product Overview
Product Name

Wisdom School Expense Tracker

Product Type

Web Application

Purpose

The system helps Wisdom School manage, monitor, and analyze all school expenses digitally instead of using manual registers or spreadsheets.

The application will allow authorized staff to:

Record expenses
Categorize spending
Upload receipts
Generate reports
Monitor monthly/yearly expenses
Track financial activity efficiently
2. Problem Statement

Currently, schools often manage expenses manually which causes:

Data loss
Calculation errors
Difficult report generation
Lack of transparency
Slow auditing process
Poor expense tracking

The system will solve these problems through centralized digital expense management.

3. Objectives
Primary Objectives
Digitize school expense tracking
Reduce manual accounting work
Improve financial transparency
Generate quick reports
Maintain historical records
Secondary Objectives
Improve accountability
Support future scalability
Enable analytics and insights
Simplify audit preparation
4. Target Users
User Role	Description
Admin	Full access to all features
Accountant	Manage expenses and reports
Staff	Limited expense entry access
5. Technology Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Flask (Python)
Database
SQLite (Initial Version)
PostgreSQL/MySQL (Future Scaling)
Libraries
Flask-Login
SQLAlchemy
Chart.js
Bootstrap (optional)
6. Core Features
6.1 Authentication System
Description

Secure login system for authorized users.

Functional Requirements
User login
User logout
Password hashing
Session management
Role-based access
User Roles
Role	Permissions
Admin	Full system control
Accountant	Expense management
Staff	Add/view limited records
6.2 Dashboard
Description

Main overview screen showing expense summaries.

Dashboard Components
Total monthly expenses
Total yearly expenses
Expense category breakdown
Recent transactions
Expense charts
Functional Requirements
Real-time calculations
Dynamic charts
Responsive layout
6.3 Expense Management
Description

Module for managing school expenses.

Features
Add expense
Edit expense
Delete expense
Search expenses
Filter expenses
Expense Fields
Field	Type	Required
Expense Title	Text	Yes
Description	Text	No
Category	Dropdown	Yes
Amount	Decimal	Yes
Date	Date	Yes
Payment Method	Dropdown	Yes
Receipt Upload	File	No
Added By	Auto	Yes
6.4 Expense Categories
Description

Manage predefined expense categories.

Default Categories
Electricity
Salaries
Transport
Stationery
Internet
Water Bills
Maintenance
Furniture
Events
Miscellaneous
Features
Add category
Edit category
Delete category
6.5 Reports Module
Description

Generate expense reports.

Report Types
Daily Report
Weekly Report
Monthly Report
Yearly Report
Category-wise Report
Export Options
PDF
Excel
Print
6.6 Receipt Upload
Description

Upload expense proof documents.

Supported Formats
JPG
PNG
PDF
Requirements
File validation
Secure upload handling
File size limitation
7. User Flow
Login Flow
User → Login Page → Authentication → Dashboard
Add Expense Flow
Dashboard → Add Expense → Fill Form → Save → Database → Dashboard Update
Report Generation Flow
Reports Page → Select Filters → Generate Report → Export/Print
8. Functional Requirements
Authentication Requirements
ID	Requirement
FR-1	User must log in securely
FR-2	Passwords must be encrypted
FR-3	Sessions must expire after logout
Expense Requirements
ID	Requirement
FR-4	User can add expenses
FR-5	User can edit expenses
FR-6	User can delete expenses
FR-7	System validates expense data
Reporting Requirements
ID	Requirement
FR-8	System generates monthly reports
FR-9	Reports can be exported
FR-10	Charts update dynamically
9. Non-Functional Requirements
Category	Requirement
Performance	Fast loading under 3 seconds
Security	Password hashing + validation
Scalability	Database upgrade support
Availability	99% uptime target
Usability	Simple interface for school staff
Responsiveness	Mobile-friendly UI
10. Database Design
Users Table
Column	Type
id	Integer
username	String
password_hash	String
role	String
Expenses Table
Column	Type
id	Integer
title	String
description	Text
amount	Float
category_id	Integer
payment_method	String
expense_date	Date
receipt_path	String
created_by	Integer
Categories Table
Column	Type
id	Integer
name	String
11. API Requirements (Optional Future)
Future REST APIs
API	Purpose
/api/expenses	Expense data
/api/reports	Reports
/api/categories	Categories
/api/dashboard	Dashboard analytics
12. UI/UX Requirements
Design Style
Professional
Minimal
School-friendly
Easy navigation
Layout
Sidebar navigation
Dashboard cards
Responsive tables
Chart sections
Color Recommendation
Blue
White
Light gray
13. Security Requirements
Password hashing
Session protection
CSRF protection
Input validation
Secure file uploads
SQL injection prevention
14. Error Handling

System must handle:

Invalid login
Empty fields
Invalid uploads
Database errors
Session timeout
15. Future Enhancements
Phase 2 Features
Multi-school support
SMS notifications
Email reporting
Budget management
AI expense prediction
Mobile app
Cloud backups
16. Deployment Requirements
Recommended Hosting

Backend:

Render
Railway

Database:

PostgreSQL for production
17. Success Metrics
Metric	Goal
Expense Entry Time	< 1 minute
Report Generation	< 5 seconds
User Error Reduction	80%
Manual Work Reduction	70%
18. MVP Scope
Included
Login system
Expense CRUD
Dashboard
Reports
Categories
Receipt uploads
Excluded
AI analytics
Mobile app
Multi-school support
Advanced accounting
19. Timeline
Phase	Duration
Planning	1 Day
Backend Setup	2 Days
Frontend Development	3 Days
Dashboard & Reports	2 Days
Testing	1 Day
Deployment	1 Day

Total Estimated:

7–10 Days
20. Final Deliverables
Frontend
Responsive UI
Dashboard
Forms
Reports
Backend
Flask APIs/routes
Authentication
Database integration
Database
Expense storage
User management
Reporting support
Deployment
Production-ready app
Hosting setup
Database configuration