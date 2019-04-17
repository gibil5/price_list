# -*- coding: utf-8 -*-
"""
 	tst.py
  	
 	Test - Treatment
 	Integration Tests for the Treatment Class

	Created: 			14 Aug 2018
	Last up: 	 		22 Jan 20189
"""

from __future__ import print_function





# ----------------------------------------------------------- Integration -------------------------
def test_integration_treatment(self, date_order_begin=False, date_order_end=False):
	"""
	Test - Integration - For Treatment 
	"""
	print()
	print('Test Integration')



	# Sale - Consultation 
	print('Create Order - Consultation')
	self.create_order_con()			# Actual Button 
	for order in self.order_ids: 
		if order.state in ['draft']:
			order.pay_myself()

	# Consultation 
	print('Create Consultation')
	self.create_consultation()
	for consultation in self.consultation_ids: 
		consultation.autofill()


	# Recommendations 
	if True:
		print('Create Recommendations')
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
		print('Create Sessions')
		for procedure in self.procedure_ids: 
			#for _ in range(2): 
			for _ in range(1):
				procedure.create_sessions()



	# Controls 
	#if False:
	if True:
		print('Create Controls')
		for procedure in self.procedure_ids:
			#for _ in range(1):
			for _ in range(6):
				procedure.create_controls()

# test_integration_treatment





# ----------------------------------------------------------- Create Recommendations  ------------------------------------------------------

# Create Recommendations 
def create_recommendations(self):
	print
	print('Create Recommendations')


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

		#model = 'price_list.service_co2'
		model = model_dic[tst]




		product = self.env['product.template'].search([
															('name', '=', name),
											],
												#order='date_order desc',
												limit=1,
									)
		print(product)
		print(product.name)
		print(product.pl_level)

		product_id = product.id
		

		#service = self.service_co2_ids.create({
		service = self.env[model].create({
														'service': 			product_id, 
														
														'pl_family': 		product.pl_family, 
														'pl_subfamily': 	product.pl_subfamily, 
														'pl_sessions': 		product.pl_sessions, 

														'pl_level': 		product.pl_level, 
														'pl_time': 			product.pl_time, 
														'pl_zone': 			product.pl_zone, 
														
														'pl_pathology': 	product.pl_pathology, 
														'pl_treatment': 	product.pl_treatment, 



														'price_applied': 		product.list_price, 


														'treatment': 	self.id, 
											})

# create_recommendations







# ----------------------------------------------------------- Reset Treatment ------------------------------------------------------

# Reset 
def reset_treatment(self):
	print()
	print('Reset')


	# Card 
	card = self.env['openhealth.card'].search([
													('patient_name', '=', self.patient.name), 
												],
													#order='write_date desc',
													limit=1,
											)
	#print card
	#print card.patient_name
	#if card.name != False: 
		#card.unlink()



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


	self.procedure_ids.unlink()
	self.session_ids.unlink()
	self.control_ids.unlink()

	self.appointment_ids.unlink()

	# Alta 
	self.treatment_closed = False


	# Orders 
	for order in self.order_ids:
		#order.remove_myself()
		order.remove_myself_force()



	# Conter Decrease - Deprecated !!!
	#name_ctr = 'advertisement'
	#counter = self.env['openhealth.counter'].search([
	#														('name', '=', name_ctr), 
	#												],
														#order='write_date desc',
	#													limit=1,
	#												)
	#counter.decrease()
	#counter.decrease()

# reset