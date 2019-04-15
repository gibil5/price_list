# -*- coding: utf-8 -*-
{
    'name': "Price List - 2019",

    'summary': 
        """
        Price List Loader for the Openhealth System
        """,

    'description': 
        """
        15 April 2019 - 11:35 am

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
        'views/product_template.xml',

        'views/product_template_search.xml',
        'views/product_template_actions.xml',

        'views/menus.xml',


        'views/treatment_services.xml',
        'views/treatment.xml',
        'views/service_gyn.xml',


        'security/data_users.xml',
    ],




    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}