# -*- coding: utf-8 -*-
{
    'name': "employee_docs",
    'summary': """This module will store employee documents""",
    'description': """This module will store employee documents""",
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_record.xml',
        'views/employee_view.xml',
        'data/corn_jobs.xml',
        'data/sequence.xml',
    ],
}
