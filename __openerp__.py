# -*- coding: utf-8 -*-
{
    'name': "Price List - 2019",

    'summary': 
        """
        Price List Loader for the Openhealth System
        """,

    'description': 
        """
        9 April 2019 - 11:35 am

        For Open Health. Service oriented way of adding Price List Management. 
        """,


    'author': "DataMetrics",
    
    'website': "http://jrevilla.com/",
    
    'category': 'Object Oriented',
    
    'version': '0.1',


    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['base', 'oehealth'],



    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',


        'views/products.xml',
        'views/containers.xml',

        'views/product_templates.xml',

        'views/menus.xml',
    ],




    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}