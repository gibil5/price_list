# -*- coding: utf-8 -*-
"""
 	Test - Treatment
 	Integration Tests for the Treatment Class.

 	test_treatment.py

	Created: 			14 Aug 2018
	Last up: 	 		19 Apr 2019
"""
from __future__ import print_function


# ----------------------------------------------- Integration -------------------------------------
def test_integration_treatment(self, date_order_begin=False, date_order_end=False):
	"""
	Test - Integration - For Treatment
	"""
	print()
	print('Test Integration Treatment')


	# Sale - Consultation
	#print('Create Order - Consultation')
	self.create_order_con()			# Actual Button
	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()

	# Consultation
	#print('Create Consultation')
	self.create_consultation()
	for consultation in self.consultation_ids:
		consultation.autofill()

	# Create Recommendations
	if True:
		#print('Create Recommendations')
		create_recommendations(self)
		self.create_order_pro()			# Actual Button
	else:
		create_order_pro_lines(self)

	# Pay Order Procedure
	print('Create Order - Procedure')
	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()

	# Sessions
	#if False:
	if True:
		#print('Create Sessions')
		for procedure in self.procedure_ids:
			#for _ in range(2):
			for _ in range(1):
				procedure.create_sessions()

	# Controls
	#if False:
	if True:
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
	print()
	print('Pl - Create Recommendations')


	tst_list = [
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

					'prod',
	]

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

					'prod':		'ACNETOPIC 200ml',
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

					'prod': 	'price_list.service_product',
		}




	for tst in tst_list:

		name = name_dic[tst]
		model = model_dic[tst]

		product = self.env['product.template'].search([
															('name', '=', name),
											],
												#order='date_order desc',
												limit=1,
									)
		product_id = product.id

		print()
		print(product)
		print(product.name)
		if False:
			print(product.pl_family)
			print(product.pl_subfamily)
			print(product.pl_treatment)
			print(product.pl_zone)
			print(product.pl_pathology)
			print(product.pl_sessions)
			print(product.pl_level)
			print(product.pl_time)


		service = self.env[model].create({
														'service': 			product_id,

														'family': 			product.pl_family,
														'subfamily': 		product.pl_subfamily,
														'pl_treatment': 	product.pl_treatment,

														'zone': 			product.pl_zone,
														'pathology': 		product.pl_pathology,
														'sessions': 		product.pl_sessions,
														'level': 			product.pl_level,
														'time': 			product.pl_time,

														'price_applied': 	product.list_price,

														'sel_zone': 		product.pl_zone,

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
