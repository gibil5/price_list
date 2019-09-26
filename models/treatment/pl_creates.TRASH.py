# 24 Sep 2019


# Continues

	# Search - Product Product
	product_product = self.env['product.product'].search([
																('id', '=', product.id),
													])
	print(product_product)

	# Search - Product Template
	product_template = self.env['product.template'].search([
																('x_name_short', '=', product_product.x_name_short),
																('x_origin', '=', False),
														])



	# Init
	#consultation_id = False
	#procedure_id = False
	#session_id = False
	#control_id = False
	#ret = 0










# Dup !


#------------------------------------------------ Create Procedure --------------------------------
# Create procedure
def create_procedure_go(self, app_date_str, subtype, product_id):
	"""
	high level support for doing this and that.
	"""
	#print()
	#print 'Create Procedure - Go'

	# Init
	treatment_id = self.id
	patient = self.patient.id


	chief_complaint = self.chief_complaint


	# Doctor
	doctor = pl_user.get_actual_doctor(self)

	doctor_id = doctor.id
	if doctor_id == False:
		doctor_id = self.physician.id




	# Create App - Dep !
	if False:
		# Search - Appointment
		appointment = self.env['oeh.medical.appointment'].search([
																	('patient', '=', self.patient.name),
																	('doctor', '=', self.physician.name),
																	('x_type', '=', 'procedure'),
																	('x_subtype', '=', subtype),
															],
																order='appointment_date desc', limit=1)
		#print appointment


		# Delta - Check if existing App is in the Future
		if appointment.name != False:
			future = appointment.appointment_date
			delta, delta_sec = lib.get_delta_now(self, future)


		if appointment.name == False or delta_sec < 0: 		# If no appointment or appointment in the past

			# Is the hour before 21:00
			app_date_ok = lib.doctor_available(self, app_date_str)

			if app_date_ok:

				# Create App
				appointment = self.env['oeh.medical.appointment'].create({
																			'appointment_date': app_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,
																			'state': 			'pre_scheduled',
																			'x_type': 			'procedure',
																			'x_subtype': 		subtype,

																			'treatment':		self.id,
																	})
		appointment_id = appointment.id
		#print appointment





	appointment_id = False

	# Search - Product Product
	product_product = self.env['product.product'].search([
																('id', '=', product_id),
													])
	



	# Search - Product Template
	product_template = self.env['product.template'].search([
																#('x_name_short', '=', product_product.x_name_short),
																#('x_origin', '=', False),

																('name', '=', product_product.name),
																('sale_ok', '=', True),
																('pl_price_list', '=', '2019'),
														])
	print(product_template)
	print(product_template.name)




	# Create Proc

	# Init
	consultation_id = False
	procedure_id = False
	session_id = False
	control_id = False
	ret = 0


	# If Dr available
	#app_date_ok = lib.doctor_available(self, app_date_str)


	#if app_date_ok:
	if True:

		# Create Procedure
		procedure = self.procedure_ids.create({
												#'evaluation_start_date':app_date_str,

												'appointment': appointment_id,
												'patient':patient,
												'doctor':doctor_id,
												'product':product_template.id,
												'chief_complaint':chief_complaint,

												'treatment':treatment_id,
											})
		procedure_id = procedure.id





		# Create Controls
		procedure.create_controls()  			# Here !

		# Create Sessions
		procedure.create_sessions()  			# Here !





		# Create Session - Dep !
		#session = self.env['openhealth.session.med'].create({
																#'evaluation_start_date':app_date_str,

		#														'appointment': appointment_id,
		#														'patient': patient,
		#														'doctor': doctor_id,
		#														'product': product_template.id,
		#														'chief_complaint': chief_complaint,

		#														'procedure': procedure_id,
		#														'treatment': treatment_id,
		#												})
		#session_id = session.id



	# Update Appointment
	if False:
		if procedure_id != False:
			ret = user.update_appointment_handlers(self, appointment_id, consultation_id, procedure_id, session_id, control_id)


	return ret
# create_procedure_go


# App Dep !
def create_procedure_go(self, product):



	# Create App - Dep !
	if False:
		# Search - Appointment
		appointment = self.env['oeh.medical.appointment'].search([
																	('patient', '=', self.patient.name),
																	('doctor', '=', self.physician.name),
																	('x_type', '=', 'procedure'),
																	('x_subtype', '=', subtype),
															],
																order='appointment_date desc', limit=1)
		#print appointment


		# Delta - Check if existing App is in the Future
		if appointment.name != False:
			future = appointment.appointment_date
			delta, delta_sec = lib.get_delta_now(self, future)


		if appointment.name == False or delta_sec < 0: 		# If no appointment or appointment in the past

			# Is the hour before 21:00
			app_date_ok = lib.doctor_available(self, app_date_str)

			if app_date_ok:

				# Create App
				appointment = self.env['oeh.medical.appointment'].create({
																			'appointment_date': app_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,
																			'state': 			'pre_scheduled',
																			'x_type': 			'procedure',
																			'x_subtype': 		subtype,

																			'treatment':		self.id,
																	})
		appointment_id = appointment.id
		#print appointment

		# Create Session - Dep !
		#session = self.env['openhealth.session.med'].create({
																#'evaluation_start_date':app_date_str,

		#														'appointment': appointment_id,
		#														'patient': patient,
		#														'doctor': doctor_id,
		#														'product': product_template.id,
		#														'chief_complaint': chief_complaint,

		#														'procedure': procedure_id,
		#														'treatment': treatment_id,
		#												})
		#session_id = session.id
	# If Dr available
	#app_date_ok = lib.doctor_available(self, app_date_str)


	# Update Appointment
	if False:
		if procedure_id != False:
			ret = user.update_appointment_handlers(self, appointment_id, consultation_id, procedure_id, session_id, control_id)



	#if app_date_ok:
	#if True:









# Aug 2019

	#name_list = [
	#				'CONSULTA MEDICA',
					#'CONSULTA GINECOLOGICA',
					#'CONSULTA MEDICA DR. CHAVARRI',
	#	]
	# Create Order Lines
	#for name in name_list:





# ----------------------------------------------------------- Create Order Target -----------------
# Create Order - By Line
def create_order(self, target):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Pl - Create Order')
	print(target)
	#print 'x_vip_inprog: ', self.x_vip_inprog


	# Init

	# Doctor
	doctor = pl_user.get_actual_doctor(self)
	
	doctor_id = doctor.id
	if doctor_id == False:
		doctor_id = self.physician.id




	# Pricelist
	# Vip in Prog
	if self.x_vip_inprog:
		#print 'Vip in prog'
		pl = self.env['product.pricelist'].search([
															('name', '=', 'VIP'),
													],
														#order='write_date desc',
														limit=1,
													)
	else:
		pl = self.pricelist_id

	#print(pl)
	#print('pricelist: ', pl.name)
	#print(pl.id)


		

	# Update Patient
	if self.patient.x_id_doc in [False, '']:
		if self.patient.x_dni not in [False, '']:
			self.patient.x_id_doc_type = 'dni'
			self.patient.x_id_doc = self.patient.x_dni






	# Create Order
	order = self.env['sale.order'].create({
													'partner_id': self.partner_id.id,
													'patient': self.patient.id,
													'state':'draft',
													'x_doctor': doctor_id,
													'x_family': target,
													'x_ruc': self.partner_id.x_ruc,
													'pricelist_id': pl.id,
													'x_dni': self.partner_id.x_dni,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,

													'treatment': self.id,
												})


# Create order lines

# Consultations
	if target == 'consultation':
		if self.chief_complaint in ['monalisa_touch']:
			target_line = 'con_gyn'
		else:
			target_line = 'con_med'

		# Init
		price_manual = -1
		price_applied = 0
		reco_id = False

		# Create
		ret = create_order_lines_micro(order, target_line, price_manual, price_applied, reco_id)



# Procedures
	else:  	
		order_id = order.id

		ret = create_order_lines(self, 'quick', order_id)
		ret = create_order_lines(self, 'co2', order_id)
		ret = create_order_lines(self, 'excilite', order_id)
		ret = create_order_lines(self, 'ipl', order_id)
		ret = create_order_lines(self, 'ndyag', order_id)
		ret = create_order_lines(self, 'medical', order_id)
		ret = create_order_lines(self, 'cosmetology', order_id)
		ret = create_order_lines(self, 'product', order_id)

		#ret = user.create_order_lines(self, 'vip', order_id)

	return order

# create_order



#------------------------------------------------ Create Order Lines ------------------------------

# Create Order Lines
def create_order_lines(self, laser, order_id):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Pl - Create Order Lines')
	#print(laser)

	order = self.env['sale.order'].search([(
												'id', '=', order_id),
											],
											#order='appointment_date desc',
											#limit=1,
										)
	_model = {
				'quick':		'openhealth.service.quick',
				'co2':			'openhealth.service.co2',
				'excilite':		'openhealth.service.excilite',
				'ipl':			'openhealth.service.ipl',
				'ndyag':		'openhealth.service.ndyag',
				'medical':		'openhealth.service.medical',
				'cosmetology':		'openhealth.service.cosmetology',
				#'vip':			'openhealth.service.vip',
				'product':		'openhealth.service.product',
	}


	# Recommendations
	rec_set = self.env[_model[laser]].search([
														('treatment', '=', self.id),
														('state', '=', 'draft'),
											],
											#order='appointment_date desc',
											#limit=1,
										)
	print(rec_set)


	# Recommendations
	for reco in rec_set:
		print('Gotcha !')
		print(reco)
		print(reco.name)
		print(reco.service)
		print(reco.service.name)
		print(reco.service.x_name_short)
		print('Gotcha !')



		# Init
		reco_id = reco.id

		name_short = reco.service.x_name_short
		
		price_manual = reco.price_manual
		price_applied = reco.price_applied


		# Create the Order Line
		ret = create_order_lines_micro(order, name_short, price_manual, price_applied, reco_id)


		# Update Recommendation State
		reco.state = 'budget'


	return 0	# Always returns the same value

# create_order_lines






# ----------------------------------------------------------- Create order lines ------------------
# Create Order Lines
def create_order_lines_micro(self, name_short, price_manual, price_applied, reco_id, qty=1):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Pl - Create Order Lines - Micro')
	#print('name_short: ', name_short)
	#print('price_manual: ', price_manual)
	#print('price_applied:', price_applied)
	#print('reco_id: ', reco_id)
	#print


	# Init
	_h_field = {
					'consultation' : 	'service_consultation_id',
					'laser_co2' : 		'service_co2_id',
					'laser_quick' : 	'service_quick_id',
					'laser_excilite' : 	'service_excilite_id',
					'laser_ipl' : 		'service_ipl_id',
					'laser_ndyag' : 	'service_ndyag_id',
					'medical' : 		'service_medical_id',
					'cosmetology' : 	'service_cosmetology_id',
					'product' : 		'service_product_id',
			}

	# Product
	product = self.env['product.product'].search([
													('x_name_short', '=', name_short),
													('x_origin', '=', False),
											])

	print(product)
	print(product.name)
	print(product.type)
	print(product.x_family)
	print(product.x_treatment)


	# Reco field
	if product.type == 'service':
		if product.x_family in ['laser', 'consultation', 'consultation_gyn']:
			categ = product.x_treatment
		else:
			categ = product.x_family
	else:
			categ = 'product'
	reco_field = _h_field[categ]


	# Print
	#print product
	#print product.name
	#print product.x_treatment
	#print categ
	#print



# Create Order Line


	# With the correct price
	order_id = self.id


	# Manual Price
	#if price_manual != 0:
	if price_manual != -1:

		#print 'Manual Price'

		ol = self.order_line.create({
										'name': 		product.name,
										'product_id': 	product.id,
										'order_id': 	order_id,
										'x_price_manual': price_manual,
										'price_unit': 	price_manual,
										reco_field: reco_id,

										'product_uom_qty': qty,
									})



	# Quick Laser - With Price Applied
	#elif product.x_treatment == 'laser_quick':
	elif product.x_treatment == 'laser_quick' and price_applied != -1:

		#print 'Quick Laser Price - W Price Applied'

		price_quick = price_applied

		ol = self.order_line.create({
										'name': 		product.name,
										'product_id': 	product.id,
										'order_id': 	order_id,
										'price_unit': 	price_quick,
										reco_field: 	reco_id,

										'product_uom_qty': qty,
									})




	# Normal case
	else:

		#print 'Normal Price'

		ol = self.order_line.create({
										'name': 		product.name,
										'product_id': 	product.id,
										'order_id': 	order_id,
										reco_field: 	reco_id,

										'product_uom_qty': qty,
								})

	# Update Order line
	#ol.update_fields(categ)

	return self.nr_lines

# create_order_lines_micro



