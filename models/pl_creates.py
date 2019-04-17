# -*- coding: utf-8 -*-
"""
	Encapsulates actual Creation on Database.

	Created: 			16 Apr 2019
 	Last up: 	 		16 Apr 2019
"""

from __future__ import print_function

from . import pl_user




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





# ----------------------------------------------------------- Create Order Target -----------------
# Create Order - By Line
def pl_create_order(self):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Pl - Pl Create Order')



	# Create Order
	order = self.env['sale.order'].create({
													'state':'draft',
													#'pricelist_id': pl.id,
													
													'x_family': 'procedure',


													'x_doctor': self.physician.id,

													'partner_id': self.partner_id.id,
													'patient': self.patient.id,
													'x_ruc': self.partner_id.x_ruc,
													'x_dni': self.partner_id.x_dni,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,

													'treatment': self.id,
												})
	print(order)



	# Shopping cart
	for cart_line in self.shopping_cart_ids:


		product = cart_line.product


		print(product)
		print(product.name)


		# Create Order Line
		ol = order.order_line.create({
										'name': 		product.name,
										
										'product_id': 	product.id,
										
										'order_id': 	order.id,
										

										#'price_unit': 	price_manual,

										#'price_unit': 	product.list_price,
										'price_unit': 	cart_line.price,


										'product_uom_qty': cart_line.qty,
									})


	return order


