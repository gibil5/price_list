# -*- coding: utf-8 -*-
"""
 	Test - Treatment - Integration Tests for the Treatment Class.

	Created: 			14 Aug 2018
	Last up: 	 		10 Jul 2019
"""
from __future__ import print_function




# ----------------------------------------------- Integration -------------------------------------
def test_integration_treatment(self, date_order_begin=False, date_order_end=False):
	"""
	Test - Integration - For Treatment
	"""
	print()
	print('Test Integration Treatment')

	# Create Sale - Consultation
	#print('Create Order - Consultation')
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
		#print('Create Recommendations')

		# Here !
		create_recommendations(self)


		self.create_order_pro()			# Actual Button
	#else:
	#	create_order_pro_lines(self)





	# Pay Order Procedure
	#if False:
	if True:
		print('Create Order - Procedure')
		for order in self.order_ids:
			if order.state in ['draft']:
				order.pay_myself()

	# Create Sessions
	if False:
	#if True:
		#print('Create Sessions')
		for procedure in self.procedure_ids:
			#for _ in range(2):
			for _ in range(1):
				procedure.create_sessions()

	# Create Controls
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


	# New Price List 2019
	create_recommendations_2019(self)


	# Price List 2018
	#create_recommendations_2018(self)





# ----------------------------------------------------------- Create Recommendations --------------
def create_recommendations_2019(self):
	"""
	Create Recommendations 2019
	Test Cases
	Be sure to cover:
		- All Families. 
		- All Sub Families. 
		- All Sub sub Families.
	"""
	print()
	print('Pl - Create Recommendations 2019')

	# Init

	#price_list = '2019'

	name_dic = {
					# Products
					'prod_0':		'ACNETOPIC 200ML',				# Topic
					'prod_1':		'KIT POST LASER CO2 COOPER',	# Kit
					'prod_2':		'TARJETA VIP',					# Card
					'prod_3':		'OTROS',						# Other
					'prod_4':		'COMISION DE ENVIO',			# Comission


					# Lasers
					'co2': 		'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',	# Co2
					'exc':		'LASER EXCILITE - Abdomen - Alopecias - 1 sesion - 15 min',					# Excilite
					'ipl':		'LASER M22 IPL - Abdomen - Depilacion - 1 sesion - 15 min',					# Ipl
					'ndy':		'LASER M22 ND YAG - Localizado Cuerpo - Hemangiomas - 1 sesion - 15 min',	# Ndyag
					'qui':		'QUICKLASER - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',				# Quick


					# Cosmetology
					'cos_0':		'CARBOXITERAPIA - Cuerpo - Rejuvenecimiento - 1 sesion - 30 min',				# Carboxitherapy
					'cos_1':		'PUNTA DE DIAMANTES - Rostro - Limpieza profunda - 1 sesion - 30 min',			# Diamond Tip
					'cos_2':		'LASER TRIACTIVE + CARBOXITERAPIA - Rostro + Papada + Cuello - Reafirmacion - 10 sesiones - 30 min',	# Laser Triactive + Carbo
					#'cos_1':		'',			# Carboxitherapy


					# Medical
					'med_0':		'ACIDO HIALURONICO - 1 Jeringa - Rejuvenecimiento Facial - 1 sesion - FILORGA UNIVERSAL',	# Hialuronic
					'med_1':		'PLASMA - Todo Rostro - Rejuvenecimiento Facial - 1 sesion',								# Plasma
					'med_2':		'BOTOX - 1 Zona - Rejuvenecimiento Zona - 1 sesion',										# Botox
					#'med_1':		'',			# Plasma


					# New Services
					'gyn':		'LASER CO2 FRACCIONAL - Monalisa Touch / Revitalizacion',
					'echo':		'ECOGRAFIAS ESPECIALES - Cadera Pediatrica (Bilateral) - 1 sesion',
					'prom':		'CARBOXITERAPIA - Localizado Cuerpo - Rejuvenecimiento Facial - 6 sesiones',
					#'gyn':		'ANALISIS - Vagina - Biopsias',
		}


	model_dic = {
					'prod_0': 	'price_list.service_product',
					'prod_1': 	'price_list.service_product',
					'prod_2': 	'price_list.service_product',
					'prod_3': 	'price_list.service_product',
					'prod_4': 	'price_list.service_product',


					'co2': 		'price_list.service_co2',
					'exc': 		'price_list.service_excilite',
					'ipl': 		'price_list.service_ipl',
					'ndy': 		'price_list.service_ndyag',
					'qui': 		'price_list.service_quick',

					'cos_0': 		'price_list.service_cosmetology',
					'cos_1': 		'price_list.service_cosmetology',
					'cos_2': 		'price_list.service_cosmetology',

					'med_0': 		'price_list.service_medical',
					'med_1': 		'price_list.service_medical',
					'med_2': 		'price_list.service_medical',

					'gyn': 		'price_list.service_gynecology',
					'echo': 	'price_list.service_echography',
					'prom': 	'price_list.service_promotion',
		}


	tst_list = [
					'prod_0',
					'prod_1',
					'prod_2',
					'prod_3',
					'prod_4',

					'co2',
					'exc',
					'ipl',
					'ndy',
					'qui',

					#'cos',
					'cos_0',
					'cos_1',
					'cos_2',

					'med_0',
					'med_1',
					'med_2',

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
															('pl_price_list', 'in', ['2019']),
															#('pl_price_list', 'in', [price_list]),
											],
												#order='date_order desc',
												limit=1,
									)
		product_id = product.id

		print()
		print(tst)
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
