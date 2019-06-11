

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
