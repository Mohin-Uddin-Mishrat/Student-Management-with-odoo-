from odoo import models, fields, api

class Course(models.Model):
    _name = 'management.course'
    _description = 'Course Information'
    
    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    credit = fields.Integer(string='Credits', required=True)
    student_ids = fields.Many2many(
        'management.student', 
        'management_student_course_rel',
        'course_id', 
        'student_id',
        string='Enrolled Students'
    )