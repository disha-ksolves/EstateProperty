# -*- coding: utf-8 -*-
{
    'name': 'school',

    'depends': ['base_setup', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/SchoolStyle.xml',
        'views/clasStyle.xml',
        'views/subStyle.xml',
        'views/feeStyle.xml',
        'views/exam.xml',
        'wizards/wizards.xml',
        'report/report.xml',
        'report/marks.xml',


    ],

    'application': True
}