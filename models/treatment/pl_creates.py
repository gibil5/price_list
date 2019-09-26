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
#def create_procedure_go(self, app_date_str, subtype, product_id):
def create_procedure_go(self, product):

	"""
	Create Procedure 
	Core Lib
	Used by: Treatment
	"""
	print()
	print('PLC - Create Procedure Go')




# Create Procedure

	# Init

	# Product Template
	product_template = product.get_product_template()
	print(product_template)


	# Patient
	patient_id = self.patient.id


	# Doctor
	doctor = pl_user.get_actual_doctor(self)
	doctor_id = doctor.id
	if doctor_id == False:
		doctor_id = self.physician.id


	# Chief Complaint
	chief_complaint = self.chief_complaint


	# Treatment
	treatment_id = self.id



	# Create Procedure
	procedure = self.procedure_ids.create({
											'patient':patient_id,
											'doctor':doctor_id,
											'product':product_template.id,
											'chief_complaint':chief_complaint,

											'treatment':treatment_id,
										})
	print(procedure)
	print(procedure.name)
	#procedure_id = procedure.id


	# Create Sessions
	#procedure.create_sessions()  			# Here !


	# Create Controls
	#procedure.create_controls()  			# Here !


	#return ret

# create_procedure_go



# ----------------------------------------------------------- Create Order Target -----------------
# Create Order - By Line
#def pl_create_order_con(self):
#def pl_create_order_con(self, target):
def pl_create_order_con(self, target, price_list):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Pl - Create Order Con')
	print(target)


	# Create Order
	order = self.env['sale.order'].create({
													'state':'draft',
													'x_doctor': self.physician.id,
													'partner_id': self.partner_id.id,
													'patient': self.patient.id,
													'x_ruc': self.partner_id.x_ruc,
													'x_dni': self.partner_id.x_dni,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,

													'x_family': 'consultation',
													'treatment': self.id,

													#'pricelist_id': pl.id,
												})
	#print(order)


	# Init
	_dic_con = {
					'medical':		'CONSULTA MEDICA',
					'gynecology':	'CONSULTA GINECOLOGICA',
					'premium':		'CONSULTA MEDICA DR. CHAVARRI',
	}

	name = _dic_con[target]


	# Search
	product = self.env['product.product'].search([
														('name', 'in', [name]),
														#('pl_price_list', 'in', ['2019']),
														('pl_price_list', 'in', [price_list]),
													],
														#order='date_begin asc',
														#limit=1,
												)
	print(product)
	print(product.name)


	# Create Order Line
	ol = order.order_line.create({
									'name': 			product.name,
									'product_id': 		product.id,

									'order_id': 		order.id,
								})
	return order







# ----------------------------------------------------------- Create Order Target -----------------
# Create Order - By Line
def pl_create_order(self):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Pl - Create Order')


	# Create Order
	order = self.env['sale.order'].create({
													'state':'draft',
													'x_doctor': self.physician.id,
													'partner_id': self.partner_id.id,
													'patient': self.patient.id,
													'x_ruc': self.partner_id.x_ruc,
													'x_dni': self.partner_id.x_dni,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,
													'x_family': 'procedure',

													'treatment': self.id,
												})
	#print(order)



	# Create Order Lines
	for cart_line in self.shopping_cart_ids:

		product = cart_line.product

		#print(product)
		#print(product.name)

		# Create Order Line
		ol = order.order_line.create({
										'name': 		product.name,										
										'product_id': 	product.id,
										'price_unit': 	cart_line.price,
										'product_uom_qty': cart_line.qty,

										'order_id': 	order.id,
									})
	return order

