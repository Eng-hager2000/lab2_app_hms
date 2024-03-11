{
    'name': "HMS App2",
    'description': " Health management system ",
    'author': "Hagar Serag",
    'category': 'Health',
    'version': '17.0.0.1.0',
    'depends': ['base',
                ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient.xml',
    ]
}
