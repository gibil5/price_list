# 30 Dec 2019


# ----------------------------------------------------------- Set Proof - Dep ---------------------------
#def get_gen_totals(self):
def get_gen_totals_dep(self):
	"""
	Abstract, General purpose.
	Gives service to other methods.
	Provider of services.
	"""
	#print()
	#print('Get Generic Totals')

	# Get
	orders, count = get_orders(self, self.date, self.x_type)

	# Init
	total = 0




	# Loop
	for order in orders:
		# Filter Block
		#if not order.x_block_flow:	
		total = total + order.amount_untaxed



	# Assign
	gen_tot = total

	if count != 0:
		serial_nr_first = orders[0].x_serial_nr
		serial_nr_last = orders[-1].x_serial_nr
	else:
		serial_nr_first = ''
		serial_nr_last = ''

	return gen_tot, serial_nr_first, serial_nr_last


	# get_gen_totals

