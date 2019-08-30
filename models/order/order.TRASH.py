# 29 Aug - Fields - Dep



# ----------------------------------------------------------- Price List - Computes ----------------------

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



	x_amount_flow = fields.Float(
			'Pl - Total F',

			compute='_compute_x_amount_flow',
		)

	@api.multi
	def _compute_x_amount_flow(self):
		for record in self:
			if record.x_block_flow:
				record.x_amount_flow = 0
			elif record.state in ['credit_note']  and  record.x_credit_note_amount not in [0, False]:
				record.x_amount_flow = - record.x_credit_note_amount
			else:
				record.x_amount_flow = record.amount_total




	# Descriptor - Family
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



	# Descriptor - Product
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





# ---------------------------------------------- Price List - Fields ------------------------------------------

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


	# Receptor
	pl_receptor = fields.Char(
			string='Receptor',
		)


	# Transfer Free
	pl_transfer_free = fields.Boolean(
			'TRANSFERENCIA GRATUITA',
		
			default=False,
		)











# 29 Aug - Validate - Dep

# ----------------------------------------------------------- Validate ----------------------------


	@api.multi
	#def validate(self):
	def validate_dep(self):
		"""
		Deprecated
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


		# Change Appointment State - To Invoiced - Dep !!!
		#self.update_appointment()


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
			#self.treatment.update_appointments()		# Dep !



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






# 29 Aug - Getters - Dep


# ----------------------------------------------------------- Ticket - Amount - Getters ----------------

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







# ----------------------------------------------------------- Ticket - Header - Getters ----------------

	# Patient Firm Address
	def get_firm_address(self):
		"""
		Used by Print Ticket
		"""
		return self.patient.x_firm_address


	# Company Address
	def get_company_name(self):
		"""
		Used by Print Ticket
		"""
		company_name = self.configurator.company_name
		return company_name


	# Company Address
	def get_company_address(self):
		"""
		Used by Print Ticket
		"""
		company_address = self.configurator.ticket_company_address
		return company_address


	# Company Address
	def get_company_phone(self):
		"""
		Used by Print Ticket
		"""
		company_phone = self.configurator.company_phone
		return company_phone


	# Company Address
	def get_company_ruc(self):
		"""
		Used by Print Ticket
		"""
		company_ruc = self.configurator.ticket_company_ruc
		return company_ruc



# ----------------------------------------------------------- Ticket - Footer - Getters ----------------

	# Description
	def get_description(self):
		"""
		Used by Print Ticket
		"""
		print()
		print('Get description')
		description = self.configurator.ticket_description
		return description


	# Warning
	def get_warning(self):
		"""
		Used by Print Ticket
		"""
		print()
		print('Get Warning')
		warning = self.configurator.ticket_warning
		return warning


	# Website
	def get_website(self):
		"""
		Used by Print Ticket
		"""
		website = self.configurator.website
		return website


	# Email
	def get_email(self):
		"""
		Used by Print Ticket
		"""
		email = self.configurator.email
		return email












# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	#configurator = fields.Many2one(
	#		'openhealth.configurator.emr',
	#		string="Configuracion",
	#	)


	def init_configurator(self):
		"""
		Init Configurator
		For past orders
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
			#print(self.configurator)
			#print(self.configurator.name)











	def validate_electronic(self):
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





# ----------------------------------------------------------- Fields ----------------------------
	#ORDER_LINE_READONLY_STATES = {
	#								'draft': 		[('readonly', False)],
	#								'sent': 		[('readonly', False)],
	#								'cancel': 		[('readonly', False)],
	#								'sale': 		[('readonly', False)],
	#								'credit_note': 		[('readonly', False)],
	#}

	# Order Line
	#order_line = fields.One2many(
	#		'sale.order.line',
	#		'order_id',
	#		string='Order Lines',
	#		states=ORDER_LINE_READONLY_STATES,
	#	)








	# Pay myself
	#def pay_myself(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
		#print
		#print 'Order - Pay myself - Interface'
	#	test_order.pay_myself(self)


# ----------------------------------------------------------- Natives ----------------------
	#ORDER_LINE_READONLY_STATES = {
	#								'draft': 		[('readonly', False)],
	#								'sent': 		[('readonly', False)],
	#								'sale': 		[('readonly', False)],
	#								'cancel': 		[('readonly', False)],
	#}

	# Order Line
	#order_line = fields.One2many(
	#		'sale.order.line',
	#		'order_id',
	#		string='Order Lines',
			#states=READONLY_STATES, 			# By XML
	#		states=ORDER_LINE_READONLY_STATES,
	#	)

	#price_list = fields.Selection(
	#		selection=px_vars._price_list_list,
	#		string='Price list',
			#default='2019',
	#		required=True,
	#	)
