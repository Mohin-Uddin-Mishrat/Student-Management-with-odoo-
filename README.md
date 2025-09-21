# Overview
A custom Odoo module for managing students, courses, and their relationships. This module allows educational institutions to track student information, course details  records.

# Features
Student management (name, email, roll number, department)

Course management (name, code, credits)

Organized menu structure: Student Management → Students/Courses

# Installation Steps
Prerequisites
Odoo 19.0 installed and running

Access to Odoo addons directory

# Installation
Place the management_of_student folder in your Odoo addons directory

Restart the Odoo server completely

Log in to your Odoo instance

Go to Apps → Update Apps List

Search for "Management Student"

Click Activate

# Testing the Module
Create Students:

Go to Student Management → Students → Create

Fill in: Name, Email, Roll Number, Department

Save the record

Create Courses:

Go to Student Management → Courses → Create

Fill in: Course Name, Course Code, Credits

Save the record

# Challenges Faced and Solutions
1. XML View Syntax Error
Problem: Odoo 19 uses <list> instead of <tree> for list views, but I initially used the old syntax.

Solution: Changed all <tree> tags to <list> in XML view files.

2. Module Caching Issues
Problem: Odoo cached old module files even after making corrections.

Solution:

Completely restarted Odoo service

Cleared browser cache multiple times

Created a new database for testing
