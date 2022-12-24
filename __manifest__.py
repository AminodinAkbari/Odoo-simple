# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SimpleTodoList',
    'version' : '1.0',
    'summary': 'daily',
    'sequence': -101,
    'author':'Aminodin',
    'description': """

    """,
    'category': 'Accounting/Edu',
    
    'website': 'https://www.Google.com',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/NewTaskWizard.xml',
        'views/main.xml',
        'views/users.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
