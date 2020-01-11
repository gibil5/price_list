# -*- coding: utf-8 -*-
{
	'name': "Price List 2019 - OBJECT ORIENTED - ODOO 9 MODULE",

	'summary': 
		"""
		Business Logic Encapsulator for the Openhealth System
		""",

	'description':
		"""

		11 Jan 2020

		(Since 22 April, in Prod)

		For Open Health. Service oriented way of adding BUSINESS LOGIC. 

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

		# Data - Gynecology - Dep ?
		#'data/data_users.xml',
		#'data/data_physicians.xml',



		# Product - 2019
		'views/product/pricelist_container.xml',
		'views/product/product_pricelist.xml',

		'views/product/product_template_actions.xml',
		'views/product/product_template.xml',
		'views/product/product_template_tree.xml',
		'views/product/product_template_search.xml',

		'views/product/product_product.xml',
		'views/product/product_product_actions.xml',




		# Order
		'views/order/product_selector.xml',               

		'views/order/payment_method_line.xml',             # Min
		'views/order/order_line.xml',                      # Min
		'views/order/order_line_actions.xml',              # MIn
		#'views/order/order.xml',                           # Min


		'views/order/closing_form.xml',                         # Min

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

		'views/service/service_actions.xml',



		# Treatment
		'views/treatment/cart_line.xml',
		'views/treatment/treatment_cart.xml',          	# Min
		'views/treatment/treatment_services.xml',      	# Min
		'views/treatment/treatment.xml',               	# Min

		#'views/treatment/procedure_actions.xml',  		# Dep
		#'views/treatment/procedure.xml',               # Dep

		#'views/treatment/session_config_1.xml',
		#'views/treatment/session_config_2.xml',



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

		'views/marketing/marketing_tree_others.xml',
		'views/marketing/marketing_actions.xml',

		'views/marketing/marketing_other_actions.xml',


		'views/marketing/histo.xml',
		'views/marketing/place.xml',
		'views/marketing/marketing_counters.xml',
		'views/marketing/origin_line.xml',


		'views/marketing/marketing.xml',






		# Management

		'views/management/mgt_patient_line.xml',

		'views/management/management_order_line.xml',
		'views/management/management_doctor_line.xml',
		
		'views/management/management_productivity_day.xml',
		'views/management/management_doctor_daily.xml',	

		'views/management/management_trees.xml',
		'views/management/management_actions.xml',
		'views/management/management.xml',





		# RSP
		#'views/report_sale_product.xml',  					# Dep



		# Electronic
		'views/electronic/account_line.xml',               # Min
		'views/electronic/account_contasis_actions.xml',   # Min
		'views/electronic/account_contasis.xml',           # Min
		'views/electronic/electronic_order.xml',           # Min


		'views/electronic/texto.xml', 
		'views/electronic/electronic_actions.xml', 

		'views/electronic/txt_line.xml', 

		'views/electronic/electronic_container.xml',       # Min



		# Appointment
		#'views/appointment/wizard.xml',            # Dep 
		#'views/appointment/matrix.xml',            # Dep
		#'views/appointment/appointment.xml',       # Dep




		# Menus - BL
		'views/menus/menus.xml',
		'views/menus/menus_marketing.xml',
		'views/menus/menus_account.xml',
		'views/menus/menus_management.xml',


		#'views/menus/menus_dev.xml',               # Dep
		#'views/menus/menus_rsp.xml',               # Dep
		#'views/menus/menus_products_2018.xml',     # Dep


		# Security
		'security/ir.model.access.csv',
	],




	# only loaded in demonstration mode
	'demo': [
		'demo/demo.xml',
	],
}