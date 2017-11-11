# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Disable confirmation of sales orders without stock',
    'version': '9.0.0.1.0',
    'category': 'Sale',
    'summary': """This module does not allow confirm sale orders that has
    products without availability in stock.""",
    'author': 'Humanytek',
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'depends': ['sale', ],
    'data': [
    ],
    'installable': True,
    'auto_install': False
}
