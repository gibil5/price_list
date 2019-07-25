# -*- coding: utf-8 -*-
{
	'name': "Price List - 2019 - SERVICE ORIENTED",

	'summary': 
		"""
		Price List Loader for the Openhealth System
		""",

	'description': 
		"""
		25 July 2019

		(Since 22 April, in Prod)

		For Open Health. Service oriented way of adding Price List Management. 

		Remember Uncle Bob:
			- Total Productive Maintenance (TPM) focuses on Maintenance, rather than on Production. 
			- The bulk of the work lies not in Manufactoring, but in Maintenance (or its avoidance).
			- In software, 80 percent of what we do is called "Maintenance": the act of Repair. 

		Remember OO Concepts:
			- Confine change to interfaces, that capture all business logic. The Getters. 
			- Do not access class variables directly. 

		Remember Instrumentation:
			- Real Data is like White Noise. That will capture your system's actual Transfer Function. Coverage.

		Remember, Hunter and Westerman:
			- Step 1 - New Thinking: Avoid the 7 Value Traps.

		Remember John Keegan: 
			- Two forces always: one slow and the other fast. 
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


		'views/product_pricelist.xml',

		'views/containers.xml',

		'views/product_template.xml',

		'views/product_template_search.xml',
		'views/product_template_actions.xml',


		'views/product_product.xml',
		'views/product_product_actions.xml',



		'views/order.xml',

		'views/order_line.xml',

		'views/closing.xml',



		'views/report_order_line.xml',





		'views/service.xml',
		
		'views/service_co2.xml',

		'views/service_exc.xml',
		'views/service_ipl.xml',
		'views/service_ndyag.xml',
		'views/service_quick.xml',

		'views/service_medical.xml',
		'views/service_cosmetology.xml',


		'views/service_gyn.xml',
		'views/service_echo.xml',
		'views/service_promo.xml',
		
		'views/service_product.xml',



		'views/treatment_cart.xml',
		'views/cart_line.xml',

		'views/treatment_services.xml',
		'views/treatment.xml',



		'views/product_selector.xml',


		'views/payment_method_line.xml',
		'views/account_line.xml',
		'views/account_contasis_actions.xml',
		'views/account_contasis.xml',


		'views/configurator_emr.xml',


		'views/procedure_actions.xml',
		'views/procedure.xml',



		'views/patient.xml',


		'views/media_line.xml',

		'views/patient_line_actions.xml', # Dep - Already in Openhealth

		'views/patient_line.xml', 
		'views/patient_line_search.xml', 
		'views/marketing_order_line.xml',
		'views/marketing.xml',
		'views/marketing_actions.xml',






		'views/management.xml',
		'views/management_order_line.xml',
		'views/management_actions.xml',

		'views/mgt_patient_line.xml',


		'views/report_sale_product.xml',



		'views/electronic_order.xml',

		
		'views/electronic_container.xml',



		'views/menus/menus.xml',
		'views/menus/menus_dev.xml',
		'views/menus/menus_marketing.xml',
		'views/menus/menus_management.xml',
		'views/menus/menus_rsp.xml',

		'views/menus/menus_products_2018.xml',




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