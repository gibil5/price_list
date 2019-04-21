# -*- coding: utf-8 -*-
{
	'name': "Price List - 2019",

	'summary': 
		"""
		Price List Loader for the Openhealth System
		""",

	'description': 
		"""
		21 April 2019

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

		'views/order_line.xml',

		'views/menus.xml',
		'views/menus_dev.xml',



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

		'security/data_users.xml',


		'security/ir.model.access.csv',
	],




	# only loaded in demonstration mode
	'demo': [
		'demo/demo.xml',
	],
}