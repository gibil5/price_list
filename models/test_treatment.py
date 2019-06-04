# -*- coding: utf-8 -*-
"""
 	Test - Treatment
 	Integration Tests for the Treatment Class.
 	test_treatment.py
	Created: 			14 Aug 2018
	Last up: 	 		19 Apr 2019
"""
from __future__ import print_function


# ----------------------------------------------- Test -------------------------------------
def test_two(self):
	"""
	Test - Two - 2018
	"""
	print()
	print('Test Treatment - Two')

	# Order - Consultation
	self.create_order_con_target_2018('medical')

	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()


	# Create Consultation
	self.create_consultation()
	for consultation in self.consultation_ids:
		consultation.autofill()


	# Create Recommendations
	if True:

		create_recommendations_2018(self)

		
		#self.create_order_pro()			# Actual Button
		self.create_order_pro_2018()			# Actual Button

	else:
		create_order_pro_lines(self)


	# Pay Order Procedure
	#if False:
	if True:
		print('Create Order - Procedure')
		for order in self.order_ids:
			if order.state in ['draft']:
				order.pay_myself()






# ----------------------------------------------- Test -------------------------------------
def test_one(self):
	"""
	Test - One - 2019
	"""
	print()
	print('Test Treatment - One')

	# Order - Consultation
	#print('Create Order - Consultation')
	
	#self.create_order_con()			# Actual Button
	self.create_order_con_med()			# Actual Button
	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()

	# Create Consultation
	#print('Create Consultation')
	self.create_consultation()
	for consultation in self.consultation_ids:
		consultation.autofill()

	# Create Recommendations
	if True:
		print('Create Recommendations')

		#create_recommendations(self)
		create_recommendations_2019(self)
		
		self.create_order_pro()			# Actual Button

	else:
		create_order_pro_lines(self)

	# Pay Order Procedure
	#if False:
	if True:
		print('Create Order - Procedure')
		for order in self.order_ids:
			if order.state in ['draft']:
				order.pay_myself()





# ----------------------------------------------- Integration -------------------------------------
def test_integration_treatment(self, date_order_begin=False, date_order_end=False):
	"""
	Test - Integration - For Treatment
	"""
	print()
	print('Test Integration Treatment')


	# Create Sale - Consultation
	#print('Create Order - Consultation')
	#self.create_order_con()			# Actual Button
	self.create_order_con_med()			# Actual Button
	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()


	# Create Consultation
	#print('Create Consultation')
	self.create_consultation()
	for consultation in self.consultation_ids:
		consultation.autofill()


	# Create Recommendations
	if True:
		print('Create Recommendations')
		create_recommendations(self)
		self.create_order_pro()			# Actual Button

	else:
		create_order_pro_lines(self)




	# Pay Order Procedure
	#if False:
	if True:
		print('Create Order - Procedure')
		for order in self.order_ids:
			if order.state in ['draft']:
				order.pay_myself()




	# Sessions
	if False:
	#if True:
		#print('Create Sessions')
		for procedure in self.procedure_ids:
			#for _ in range(2):
			for _ in range(1):
				procedure.create_sessions()

	# Controls
	if False:
	#if True:
		#print('Create Controls')
		for procedure in self.procedure_ids:
			#for _ in range(1):
			for _ in range(6):
				procedure.create_controls()

# test_integration_treatment



# ----------------------------------------------------------- Create Recommendations --------------
def create_recommendations(self):
	"""
	Create Recommendations
	"""
	#print()
	#print('Pl - Create Recommendations')

	#create_recommendations_2019(self)

	create_recommendations_2018(self)




# ----------------------------------------------------------- Create Recommendations --------------
def create_recommendations_2018(self):
	"""
	Create Recommendations 2018
	"""
	print()
	print('Pl - Create Recommendations 2018')

	# Init

	price_list = '2018'

	tst_list = [
					#'prod_0',
					#'prod_1',
					#'prod_2',

					'co2',
					#'exc',
					#'ipl',
					#'ndy',
					#'qui',
					#'cos',
					#'med',

					#'gyn',
					#'echo',
					#'prom',
	]

	name_dic = {
					#'co2': 	'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',
					'co2':		'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento Cuello Grado 3',

					#'exc':		'LASER EXCILITE - Abdomen - Alopecias - 1 sesion - 15 min',
					#'ipl':		'LASER M22 IPL - Abdomen - Depilacion - 1 sesion - 15 min',
					#'ndy':		'LASER M22 ND YAG - Localizado Cuerpo - Hemangiomas - 1 sesion - 15 min',
					#'qui':		'QUICKLASER - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',
					#'cos':		'CARBOXITERAPIA - Cuerpo - Rejuvenecimiento - 1 sesion - 30 min',
					#'med':		'ACIDO HIALURONICO - 1 Jeringa - Rejuvenecimiento Facial - 1 sesion - FILORGA UNIVERSAL',

					#'prod_0':		'ACNETOPIC 200ML',
					#'prod_1':		'KIT POST LASER CO2 COOPER',
					#'prod_2':		'TARJETA VIP',
		}


	model_dic = {
					'co2': 		'price_list.service_co2',
					#'co2': 			'openhealth.service.co2',

					#'exc': 		'price_list.service_excilite',
					#'ipl': 		'price_list.service_ipl',
					#'ndy': 		'price_list.service_ndyag',
					#'qui': 		'price_list.service_quick',

					#'cos': 		'price_list.service_cosmetology',
					#'med': 		'price_list.service_medical',

					#'prod_0': 	'price_list.service_product',
					#'prod_1': 	'price_list.service_product',
					#'prod_2': 	'price_list.service_product',
		}


	# Loop
	for tst in tst_list:

		# Init
		name = name_dic[tst]

		model = model_dic[tst]

		# Search
		product = self.env['product.template'].search([
															('name', '=', name),
															#('pl_price_list', 'in', ['2019']),
															('pl_price_list', 'in', [price_list]),
											],
												#order='date_order desc',
												limit=1,
									)
		product_id = product.id

		print()
		print(product)
		print(product_id)
		print(product.name)
		print(product.pl_price_list)
		print(product.pl_treatment)
		print()

		#if False:
		#	print(product.pl_family)
		#	print(product.pl_subfamily)
		#	print(product.pl_treatment)
		#	print(product.pl_zone)
		#	print(product.pl_pathology)
		#	print(product.pl_sessions)
		#	print(product.pl_level)
		#	print(product.pl_time)


		_dic = {
							'1':					'1 sesion',
							'rejuvenation_neck_3':	'Rejuvenecimiento Zona',
							'neck':					'Cuello',
							'laser_co2':			'LASER CO2 FRACCIONAL',
		}

		_dic_sub = {
							'laser_co2':			'co2',
		}

		# Create
		service = self.env[model].create({
														'service': 			product_id,

														#'family': 			product.pl_family,
														'family': 			product.x_family,

														#'subfamily': 		product.pl_subfamily,
														'subfamily': 		_dic_sub[product.x_treatment],

														#'zone': 			product.x_zone,
														'zone': 			_dic[product.x_zone],

														#'pathology': 		product.x_pathology,
														'pathology': 		_dic[product.x_pathology],

														#'sessions': 		product.x_sessions,
														'sessions': 		_dic[product.x_sessions],
														
														'level': 			'Grado 1',

														'time': 			product.x_time,

														'price_applied': 	product.list_price,

														#'sel_zone': 		product.x_zone,
														'sel_zone': 		_dic[product.x_zone],

														#'pl_treatment': 	product.x_treatment,
														'pl_treatment': 	_dic[product.x_treatment],

														'treatment': 		self.id,

											})
# create_recommendations



# ----------------------------------------------------------- Create Recommendations --------------
def create_recommendations_2019(self):
	"""
	Create Recommendations 2019
	"""
	print()
	print('Pl - Create Recommendations 2019')

	# Init

	price_list = '2019'

	name_dic = {
					'co2': 		'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',
					'exc':		'LASER EXCILITE - Abdomen - Alopecias - 1 sesion - 15 min',
					'ipl':		'LASER M22 IPL - Abdomen - Depilacion - 1 sesion - 15 min',
					'ndy':		'LASER M22 ND YAG - Localizado Cuerpo - Hemangiomas - 1 sesion - 15 min',
					'qui':		'QUICKLASER - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',
					'cos':		'CARBOXITERAPIA - Cuerpo - Rejuvenecimiento - 1 sesion - 30 min',
					'med':		'ACIDO HIALURONICO - 1 Jeringa - Rejuvenecimiento Facial - 1 sesion - FILORGA UNIVERSAL',

					'gyn':		'ANALISIS - Vagina - Biopsias',
					'echo':		'ECOGRAFIAS ESPECIALES - Cadera Pediatrica (Bilateral) - 1 sesion',
					'prom':		'CARBOXITERAPIA - Localizado Cuerpo - Rejuvenecimiento Facial - 6 sesiones',

					'prod_0':		'ACNETOPIC 200ML',
					'prod_1':		'KIT POST LASER CO2 COOPER',
					'prod_2':		'TARJETA VIP',
		}


	model_dic = {
					'co2': 		'price_list.service_co2',
					'exc': 		'price_list.service_excilite',
					'ipl': 		'price_list.service_ipl',
					'ndy': 		'price_list.service_ndyag',
					'qui': 		'price_list.service_quick',

					'cos': 		'price_list.service_cosmetology',
					'med': 		'price_list.service_medical',

					'gyn': 		'price_list.service_gynecology',
					'echo': 	'price_list.service_echography',
					'prom': 	'price_list.service_promotion',

					'prod_0': 	'price_list.service_product',
					'prod_1': 	'price_list.service_product',
					'prod_2': 	'price_list.service_product',
		}


	tst_list = [
					'prod_0',
					'prod_1',
					'prod_2',

					'co2',
					'exc',
					'ipl',
					'ndy',
					'qui',
					'cos',
					'med',

					'gyn',
					'echo',
					'prom',
	]


	# Loop
	for tst in tst_list:

		# Init
		name = name_dic[tst]

		model = model_dic[tst]

		# Search
		product = self.env['product.template'].search([
															('name', '=', name),
															#('pl_price_list', 'in', ['2019']),
															('pl_price_list', 'in', [price_list]),
											],
												#order='date_order desc',
												limit=1,
									)
		product_id = product.id

		print()
		print(product)
		print(product_id)
		print(product.name)

		print(product.pl_price_list)

		print(product.pl_treatment)

		#if False:
		#	print(product.pl_family)
		#	print(product.pl_subfamily)
		#	print(product.pl_treatment)
		#	print(product.pl_zone)
		#	print(product.pl_pathology)
		#	print(product.pl_sessions)
		#	print(product.pl_level)
		#	print(product.pl_time)


		# Create
		service = self.env[model].create({
														'service': 			product_id,

														'family': 			product.pl_family,
														'subfamily': 		product.pl_subfamily,

														'zone': 			product.pl_zone,
														'pathology': 		product.pl_pathology,
														'sessions': 		product.pl_sessions,
														'level': 			product.pl_level,
														'time': 			product.pl_time,

														'price_applied': 	product.list_price,

														'sel_zone': 		product.pl_zone,

														'pl_treatment': 	product.pl_treatment,
														'treatment': 		self.id,

											})
# create_recommendations



# ----------------------------------------------------------- Reset Treatment ---------------------

def reset_treatment(self):
	"""
	Reset Treatment
	"""
	print()
	print('Reset')


	# Consultation
	self.consultation_ids.unlink()

	# Recos
	self.service_co2_ids.unlink()


	# Recos
	self.service_co2_ids.unlink()
	self.service_excilite_ids.unlink()
	self.service_ipl_ids.unlink()
	self.service_ndyag_ids.unlink()
	self.service_quick_ids.unlink()
	self.service_product_ids.unlink()
	self.service_medical_ids.unlink()
	self.service_cosmetology_ids.unlink()
	self.service_gynecology_ids.unlink()
	self.service_echography_ids.unlink()
	self.service_promotion_ids.unlink()

	# Procedures
	self.procedure_ids.unlink()
	self.session_ids.unlink()
	self.control_ids.unlink()

	# App
	self.appointment_ids.unlink()

	# Alta
	self.treatment_closed = False

	# Orders
	for order in self.order_ids:
		#order.remove_myself()
		order.remove_myself_force()
# reset
