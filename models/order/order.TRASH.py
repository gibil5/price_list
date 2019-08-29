# 29 Aug


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
