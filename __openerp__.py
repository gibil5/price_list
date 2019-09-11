# -*- coding: utf-8 -*-
{
    'name': "Price List - 2019 - SERVICE ORIENTED",

    'summary': 
        """
        Price List Loader for the Openhealth System
        """,

    'description': 
        """

        11 Sep 2019

        (Since 22 April, in Prod)

        For Open Health. Service oriented way of adding Price List Management. 

        Remember Robert C. Martin:
            - In software, 80 percent of what we do is called "Maintenance": the act of Repair. 
            - A Class exposes an abstract interface that allows users to manipulate the Essence of the data, without having to know its Implementation. 
            - Respect the Law of Demeter. Avoid Train Wreckages.
            - Handle Exceptions.


        Remember OO Concepts:
            - Confine change to interfaces, that capture all business logic. The Getters. 
            - Do not access class variables directly. 

        Remember Instrumentation:
            - Real Data is like White Noise. That will capture your system's actual Transfer Function. Coverage.

        Remember, Hunter and Westerman:
            - Step 1: New Thinking: Avoid the 7 Value Traps.

        Remember John Keegan: 
            - Two forces always: one slow and the other fast. 
        """,


    'author': "DataMetrics",
    
    'website': "http://jrevilla.com/",
    
    'category': 'Object Oriented',
    
    'version': '0.1',


    # any module necessary for this one to work correctly
    #'depends': ['base'],
    #'depends': ['base', 'oehealth'],
    'depends': ['base', 'oehealth', 'openhealth'],



    # always loaded
    'data': [

        # 'security/ir.model.access.csv',


        # Product - 2019
        'views/product/pricelist_container.xml',
        'views/product/product_pricelist.xml',
        'views/product/product_template.xml',
        'views/product/product_template_search.xml',
        'views/product/product_template_actions.xml',
        'views/product/product_product.xml',
        'views/product/product_product_actions.xml',




        # Order
        'views/order/product_selector.xml',               

        'views/order/payment_method_line.xml',             # Min
        'views/order/order_line.xml',                      # Min
        'views/order/order_line_actions.xml',              # MIn
        #'views/order/order.xml',                           # Min
        'views/order/closing.xml',                         # Min
        'views/order/report_order_line.xml',               # Min



        # Service
        'views/service/service.xml',
        'views/service/service_co2.xml',
        'views/service/service_exc.xml',
        'views/service/service_ipl.xml',
        'views/service/service_ndyag.xml',
        'views/service/service_quick.xml',
        'views/service/service_medical.xml',
        'views/service/service_cosmetology.xml',
        'views/service/service_gyn.xml',
        'views/service/service_echo.xml',
        'views/service/service_promo.xml',
        'views/service/service_product.xml',


        # Treatment
        'views/treatment/cart_line.xml',
        'views/treatment/treatment_cart.xml',          # Min
        'views/treatment/treatment_services.xml',      # Min
        'views/treatment/treatment.xml',               # Min
        'views/treatment/procedure_actions.xml',
        'views/treatment/procedure.xml',


        # Configurator
        #'views/configurator_emr.xml',                  # Dep


        # Patient
        'views/patient/patient.xml',                   
        #'views/patient/patient_personal.xml',          # Dep


        # Marketing
        'views/marketing/media_line.xml',
        'views/marketing/patient_line_actions.xml',     # Dep - Already in Openhealth
        'views/marketing/patient_line.xml', 
        'views/marketing/patient_line_search.xml', 
        'views/marketing/marketing_order_line.xml',
        'views/marketing/marketing.xml',
        'views/marketing/marketing_actions.xml',


        # Management
        'views/management/management.xml',
        'views/management/management_order_line.xml',
        'views/management/management_actions.xml',
        'views/management/mgt_patient_line.xml',


        # RSP
        'views/report_sale_product.xml',


        # Electronic
        'views/electronic/account_line.xml',               # Min
        'views/electronic/account_contasis_actions.xml',   # Min
        'views/electronic/account_contasis.xml',           # Min
        'views/electronic/electronic_order.xml',           # Min
        'views/electronic/electronic_container.xml',       # Min



        # Appointment
        #'views/appointment/wizard.xml',            # Dep 
        #'views/appointment/matrix.xml',            # Dep
        #'views/appointment/appointment.xml',       # Dep



        # Menus
        'views/menus/menus.xml',
        'views/menus/menus_marketing.xml',
        'views/menus/menus_management.xml',

        #'views/menus/menus_dev.xml',               # Dep
        #'views/menus/menus_rsp.xml',               # Dep
        #'views/menus/menus_products_2018.xml',     # Dep


        # Security
        'security/data_users.xml',
        'security/data_physicians.xml',
        'security/ir.model.access.csv',
    ],




    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}