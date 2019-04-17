{
    'name': "journal_aacount",
    'summary': """ Customization of journal for integrate with analytics\
                   accounts.  """,
    'author': "SimpleIT",
    'website': "http://simpleit.com",
    'category': 'account_invoicing',
    'version': '12.0',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/model_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
