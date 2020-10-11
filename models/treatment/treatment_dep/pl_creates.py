# -*- coding: utf-8 -*-
"""
	Encapsulates actual Creation on Database - DEP - 11 aug 2020
	Created: 			16 Apr 2019
 	Last up: 	 		26 Sep 2019

	pl_create_order_con
	pl_create_order
	create_procedure_go
"""
from __future__ import print_function
from . import pl_user


# ----------------------------------------------------------- Create Order Target -----------------
def pl_create_order_con(self, target, price_list):
	"""
	Create Order Consultation
	"""
	print()
	print('Pl - pl_creates - pl_create_order_con')
	print(target)

	# Create Partner
	print('Create partner')
	partner = self.env['res.partner'].search([
													('name', '=', self.patient.name),
												],
												limit=1,)
	#partner_id = partner.id


	# Create Order
	print('Create order')
	order = self.env['sale.order'].create({
													'patient': self.patient.id,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,
													'x_doctor': self.physician.id,
													'state':'draft',
													'partner_id': partner.id,
													'x_family': 'consultation',
													'treatment': self.id,

													#'partner_id': self.partner_id.id,
													#'x_ruc': self.partner_id.x_ruc,
													#'x_dni': self.partner_id.x_dni,
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
	print('Search product')
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
	print('Create order line')
	ol = order.order_line.create({
									'name': 			product.name,
									'product_id': 		product.id,
									'order_id': 		order.id,
								})
	return order

	# pl_create_order_con



# ----------------------------------------------------------- Create Order Target -----------------
def pl_create_order(self):
	"""
	Create Order - By Line
	"""
	print()
	print('Pl - Create Order')


	partner = self.env['res.partner'].search([
													('name', '=', self.patient.name),
												],
												#order='appointment_date desc',
												limit=1,)


	# Create Order
	order = self.env['sale.order'].create({
													'state':'draft',
													'x_doctor': self.physician.id,

													#'partner_id': self.partner_id.id,
													'partner_id': partner.id,
													#'x_ruc': self.partner_id.x_ruc,
													#'x_dni': self.partner_id.x_dni,

													'patient': self.patient.id,
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

	# pl_create_order


#------------------------------------------------ Create Procedure Go --------------------------------

def create_procedure_go(self, product):
	"""
	Create Procedure - Core
	Used by: Treatment
	Input is a Product Product !!!
	"""
	print()
	print('PLC - Create Procedure Go')


# Init

	# Product Template
	product_template = product.get_product_template()
	#print(product_template)


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
# create_procedure_go
