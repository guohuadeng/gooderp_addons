{
    'name': 'GoodErp 首页设置',
    'version': '11.11',
    'author':"开阖静静<gilbert@osbzr.com>(开阖出品)",
    'summary': '首页配置',
    'category': 'Tools',
    'description':
    '''
                            该模块实现了 GoodERP 可配置的首页系统。
    ''',
    'data': [
        'security/groups.xml',
        "home_page.xml",
        'security/ir.model.access.csv',
    ],
    'depends': ['base','web','mail'],
    'qweb': ['static/src/xml/*.xml'],
}
