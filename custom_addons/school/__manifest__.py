{
    'name': "School Management System",
    'version': '1.0',
    'depends': ['base'],
    'author': "Benjamin Kisenge",
    'category': 'Education',
    'description': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
    """,
    # data files always loaded at installation
    'installable': True,
    'application': True,
    "sequence": -100,
    'data': [
        'views/school_view.xml',
        'views/department_view.xml',
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'school/static/styles.css',
        ],
    },
    # data files containing optionally loaded demonstration data
    'demo': [],
}