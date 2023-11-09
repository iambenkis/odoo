# -*- coding: utf-8 -*-
{
    'name': "Benjamin",

    'summary': """
        this is where benjamin is going to be working on his modules.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Benjamin kisenge",
    'website': "https://www.benjaminkisenge23.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list 
    'version': '0.1',
    'application': True,
    'installable': True,
    'sequence': 2,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml', 
    ],
    'assets': {
        'web.assets_backend': [
            'people/static/style.css',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
