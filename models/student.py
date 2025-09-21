from odoo import models, fields, api

class Student(models.Model):
    _name = 'management.student'
    _description = 'Student Information'
    
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    roll_no = fields.Char(string='Roll Number', required=True)
    department = fields.Char(string='Department', required=True)
    course_ids = fields.Many2many(
        'management.course', 
        'management_student_course_rel',
        'student_id', 
        'course_id',
        string='Enrolled Courses'
    )
    
    def action_show_courses(self):
        self.ensure_one()
        return {
            'name': 'Enrolled Courses',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'management.course',
            'domain': [('id', 'in', self.course_ids.ids)],
            'target': 'current',
        }