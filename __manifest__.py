{
    'name': 'Management Student',
    'version': '1.0',
    'summary': 'Manage students, courses and enrollments',
    'category': 'Education',
    'author': 'Your Name',
    'website': 'https://www.nnsengg.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}