# -*- coding: utf-8 -*-
{
    'name': "Plant Nursery",
    'version': '0.1',
    'summary': """Plant and customer management""",
    'author': "Abdul Halim",
    'website': "http://abdulhalim.pythonanywhere.com",
    'category': 'Uncategorized',
    'depends': ['web'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}