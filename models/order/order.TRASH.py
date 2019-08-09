


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
