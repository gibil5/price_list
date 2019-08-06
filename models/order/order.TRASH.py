




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
