# -*- coding: utf-8 -*-
{
    'name': "CVC",
    'sequence': 1,
    'summary': """""",
    'description': """""",
    'author': "Youssef JABALLAH",
    'website': "",
    'category': '',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    # always loaded
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/cvc.xml',
        'views/menu.xml',
    ],
    'assets': {
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
