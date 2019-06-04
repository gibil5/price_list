
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







# ----------------------------------------------------------- Reset Treatment ---------------------

def reset_treatment(self):



	# Vip Card
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