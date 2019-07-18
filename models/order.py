# -*- coding: utf-8 -*-
"""
		*** Order

		order.py

		Created: 			26 Aug 2016
		Last up: 	 		17 Jul 2019
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError

class sale_order(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'sale.order'




	# Pay myself
	#def pay_myself(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
		#print
		#print 'Order - Pay myself - Interface'
	#	test_order.pay_myself(self)





# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
		)


	def init_configurator(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Init Configurator')

		# Configurator
		if self.configurator.name in [False]:
			self.configurator = self.env['openhealth.configurator.emr'].search([
																					('x_type', 'in', ['emr']),
															],
															#order='date_begin,name asc',
															limit=1,
														)
			print(self.configurator)
			print(self.configurator.name)



# ----------------------------------------------------------- Ticket - Header - Getters ----------------
	def get_company_name(self):
		"""
		Used by Print Ticket.
		"""
		#company_name = 'SERVICIOS MÉDICOS ESTÉTICOS S.A.C'

		self.init_configurator()

		if self.configurator.name not in [False]:
			company_name = self.configurator.company_name
		else:
			company_name = ''
		return company_name




	def get_company_address(self):
		"""
		Used by Print Ticket.
		"""
		#company_address = 'Av. La Merced 161 Miraflores - Lima'

		self.init_configurator()

		if self.configurator.name not in [False]:
			#company_address = self.configurator.company_address
			company_address = self.configurator.ticket_company_address
		else:
			company_address = ''
		return company_address



	def get_company_phone(self):
		"""
		Used by Print Ticket.
		"""
		#company_phone = 'Teléfono: (051) 321 2394'

		self.init_configurator()

		if self.configurator.name not in [False]:
			company_phone = self.configurator.company_phone
		else:
			company_phone = ''
		return company_phone



	def get_company_ruc(self):
		"""
		Used by Print Ticket.
		"""
		#company_ruc = 'R.U.C.: 20523424221'

		self.init_configurator()

		if self.configurator.name not in [False]:
			#company_ruc = self.configurator.company_ruc
			company_ruc = self.configurator.ticket_company_ruc
		else:
			company_ruc = ''
		return company_ruc




# ----------------------------------------------------------- Ticket - Footer - Getters ----------------

	# description
	def get_description(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Get description')

		# With Configurator
		self.init_configurator()
		if self.configurator.name not in [False]:
			description = self.configurator.ticket_description
		else:
			description = ''

		return description


	# Warning
	def get_warning(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Get Warning')

		# With Configurator
		self.init_configurator()
		if self.configurator.name not in [False]:
			warning = self.configurator.ticket_warning
		else:
			warning = ''

		return warning


	# Website
	def get_website(self):
		"""
		high level support for doing this and that.
		"""
		#return self.x_my_company.website

		# Configurator
		self.init_configurator()

		if self.configurator.name not in [False]:
			website = self.configurator.website
		else:
			website = ''
		return website



	# Email
	def get_email(self):
		"""
		high level support for doing this and that.
		"""
		#return self.x_my_company.email

		# Configurator
		self.init_configurator()

		if self.configurator.name not in [False]:
			email = self.configurator.email
		else:
			email = ''
		return email







# ----------------------------------------------------------- Validate ----------------------------
	x_amount_flow = fields.Float(
			'Pl - Total F',

			compute='_compute_x_amount_flow',
		)

	@api.multi
	def _compute_x_amount_flow(self):
		#print('Pl - compute x_amount_flow')
		for record in self:

			if record.x_block_flow:
				record.x_amount_flow = 0

			#elif record.x_credit_note_amount not in [0, False]:
			elif record.state in ['credit_note']  and  record.x_credit_note_amount not in [0, False]:
				#record.x_amount_flow = record.amount_total - record.x_credit_note_amount
				record.x_amount_flow = - record.x_credit_note_amount

			else:
				record.x_amount_flow = record.amount_total




# ----------------------------------------------------------- Validate ----------------------------

	# Validate
	@api.multi
	def validate_electronic(self):
		"""
		Validate Order.
		Used by Electronic Container (Txt Generation). 
		"""
		#print()
		#print('Pl - Order Validate')

		#print(self.name)
		#print(self.patient.name)
		#print(self.x_type)
		#print(self.x_type_code)
		#print(self.x_serial_nr)
		#print(self.pl_receptor)

		error = 0
		msg = ''

		#if self.x_type in [False]		or 	self.x_type_code in [False]		or self.x_serial_nr in [False]:
		if self.x_type in [False]		or 	self.x_type_code in [False]		or self.x_serial_nr in [False]   	or self.pl_receptor in [False, '']:
			print('Gotcha !')

			msg = 'ERROR - Venta: La Venta esta incompleta. ' + self.patient.name
			error = 1

			#raise UserError(_(msg))
		else:
			#print('Validated !')
			print()
		return error, msg

	# validate_electronic



# ----------------------------------------------------------- Natives ----------------------


	# Price List
	pl_price_list = fields.Char(
			string="Pl - Price List",

			compute='_compute_pl_price_list',
		)

	@api.multi
	def _compute_pl_price_list(self):
		for record in self:
			price_list = ''
			for line in record.order_line:
				price_list =line.get_price_list()
			record.pl_price_list = price_list




# ----------------------------------------------------------- Natives ----------------------------
	pl_receptor = fields.Char(
			string='Receptor',
			#required=True,
		)



# ----------------------------------------------------------- Descriptors -------------------------------



	# Family
	pl_family = fields.Char(
			string="Pl - Familia",

			compute='_compute_pl_family',
		)

	@api.multi
	def _compute_pl_family(self):
		for record in self:
			families = ''
			for line in record.order_line:
				families = families + line.get_family() + ', '
			record.pl_family = families



	# Product
	pl_product = fields.Char(
			string="Pl - Producto",

			compute='_compute_pl_product',
		)

	@api.multi
	def _compute_pl_product(self):
		for record in self:
			products = ''
			for line in record.order_line:
				products = products + line.get_product() + ', '
			record.pl_product = products








# ----------------------------------------------------------- Print Ticket -------------------------------

	def get_total_net(self):
		"""
		Used by Print Ticket.
		"""
		if self.pl_transfer_free:
			value = 0
		else:
			value = self.x_total_net
		return value


	def get_total_tax(self):
		"""
		Used by Print Ticket.
		"""		
		if self.pl_transfer_free:
			value = 0
		else:
			value = self.x_total_tax
		return value


	def get_amount_total(self):
		"""
		Used by Print Ticket.
		"""
		if self.pl_transfer_free:
			value = 0
		else:
			value = self.amount_total
		return value




	def get_total_in_words(self):
		"""
		Used by Print Ticket.
		"""
		if self.pl_transfer_free:
			value = 'Cero'
		else:
			value = self.x_total_in_words
		return value


	def get_total_cents(self):
		"""
		Used by Print Ticket.
		"""
		if self.pl_transfer_free:
			value = 0
		else:
			value = self.x_total_cents
		return value




# ---------------------------------------------- Fields ------------------------------------------
	pl_transfer_free = fields.Boolean(

			#'Transferencia Gratuita',
			'TRANSFERENCIA GRATUITA',
		
			default=False,
		)



# ----------------------------------------------------------- Update Descriptors ------------------


	@api.multi
	def update_descriptors(self):
		"""
		For Order Validation.
		Update Family and Product.

		Used by: validate()
		"""
		#print()
		#print('Pl - Update Descriptors')


		out = False

		for line in self.order_line:

			#print(line.product_id.pl_subfamily)

			if not out:

				# Consultations
				if line.product_id.pl_subfamily in ['consultation']:
					self.x_family = 'consultation'
					out = True
					#print('mark 1')


				# Procedures
				elif line.product_id.pl_family in ['laser', 'medical', 'gynecology', 'echography']:
					self.x_family = 'procedure'
					out = True
					#print('mark 2')


				# Cosmetology
				elif line.product_id.pl_family in ['cosmetology']:
					self.x_family = 'cosmetology'
					out = True
					#print('mark 3')


				# Products
				else:
					if self.x_family != 'procedure':
						self.x_family = 'product'
					#print('mark 4')

	#update_descriptors


# ----------------------------------------------------------- Validate ----------------------------

	# Action confirm
	@api.multi
	def validate(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Validate')



		# Price list
		#print('Validate Price list')
		for line in self.order_line:
			#if line.pl_price_list not in ['2019']:
			if line.pl_price_list not in ['2019', '2018']:
				msg = "Error: Lista de Precios."
				raise UserError(_(msg))



		# Payment method validation
		self.check_payment_method()

		# Doctor User Name
		if self.x_doctor.name != False:
			uid = self.x_doctor.x_user_name.id
			self.x_doctor_uid = uid


		# Date - Must be that of the Sale, not the Budget.
		self.date_order = datetime.datetime.now()
		self.update_day_month()


		# Update Descriptors (family and product)
		self.update_descriptors()


		#print('mark 1')


		# Change Appointment State - To Invoiced
		self.update_appointment()


		#print('mark 2')


		# Vip Card - Detect and Create
		self.detect_create_card()


		#print('mark 3')


		# Type
		#print 'Type'
		if self.x_payment_method.saledoc != False:
			self.x_type = self.x_payment_method.saledoc
		#print self.x_type


		#print('mark 4')


		# Create Procedure 
		if self.treatment.name != False:
			for line in self.order_line:
				if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:
					# Create
					self.treatment.create_procedure(False, line.product_id.x_treatment, line.product_id.id)
				line.update_recos()
			# Update
			self.x_procedure_created = True
			self.treatment.update_appointments()



		#print('mark 5')



		# Id Doc and Ruc
		# Invoice
		if self.x_type in ['ticket_invoice', 'invoice']:
			if self.x_ruc in [False, '']:
				msg = "Error: RUC Ausente."
				#raise Warning(_(msg))
				raise UserError(_(msg))

		# Receipt
		elif self.x_type in ['ticket_receipt', 'receipt']:
			if self.x_id_doc_type in [False, '']  or self.x_id_doc in [False, '']:
				msg = "Error: Documento de Identidad Ausente."
				#raise Warning(_(msg))
				raise UserError(_(msg))

		# Update Patient
		if self.patient.x_id_doc in [False, '']:
			self.patient.x_id_doc_type = self.x_id_doc_type
			self.patient.x_id_doc = self.x_id_doc


		# Change Electronic
		self.x_electronic = True


		# Title
		if self.x_type in ['ticket_receipt', 'receipt']:
			self.x_title = 'Boleta de Venta Electrónica'
		elif self.x_type in ['ticket_invoice', 'invoice']:
			self.x_title = 'Factura de Venta Electrónica'
		else:
			self.x_title = 'Venta Electrónica'


		# Change State
		self.state = 'validated'


		print('mark 10')
	# validate







# ----------------------------------------------------- Product Selector --------------------------

	@api.multi
	#def open_product_selector_product(self):
	def pl_open_product_selector_product(self):
		"""
		high level support for doing this and that.
		"""
		#print('o ps p')
		return self.pl_open_product_selector('product')


	@api.multi
	#def open_product_selector_service(self):
	def pl_open_product_selector_service(self):
		"""
		high level support for doing this and that.
		"""
		#print('o ps s')
		return self.pl_open_product_selector('service')



	# Buttons  - Agregar Producto Servicio
	@api.multi
	#def open_product_selector(self, x_type):
	def pl_open_product_selector(self, x_type):
		"""
		high level support for doing this and that.
		"""
		#print('o ps')


		# Init Vars
		order_id = self.id
		res_id = False


		return {
				'type': 'ir.actions.act_window',
				'name': ' New Orderline Selector Current',
				'view_type': 'form',
				'view_mode': 'form',
				#'target': 'current',
				'target': 'new',
				'res_id': res_id,


				#'res_model': 'openhealth.product.selector',
				'res_model': 'price_list.product.selector',


				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
								'form':{'action_buttons': False, 'options': {'mode': 'edit'}}
							},
				'context': {
								'default_order_id': order_id,
								'default_x_type': x_type,
					}}
					
	# pl_open_product_selector



# ----------------------------------------------------------- Validate ----------------------------
	# States
	READONLY_STATES = {
		'draft': 		[('readonly', False)],
		'sent': 		[('readonly', False)],
		'sale': 		[('readonly', True)],
		'cancel': 		[('readonly', True)],
	}

	# Doctor
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			states=READONLY_STATES,
		)
