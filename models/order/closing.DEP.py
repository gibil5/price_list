# 30 Dec 2019

	def update_totals(self):
		#pl_clos_funcs.pl_set_form_totals(self)


# ----------------------------------------------------------- Set Form ----------------------------

def set_form_totals(self):
	"""
	Object oriented. 
	User of services.
	"""
	#print()
	#print('Set By Form')


	# Get Orders
	x_type = 'all'
	orders, count = get_orders(self, self.date, x_type)

	# Init
	cash_tot = 0
	ame_tot = 0
	din_tot = 0
	mac_tot = 0
	mad_tot = 0
	vic_tot = 0
	vid_tot = 0


	# Loop
	for order in orders:


		for pm_line in order.x_payment_method.pm_line_ids:

			if pm_line.method == 'cash':
				cash_tot = cash_tot + pm_line.subtotal

			elif pm_line.method == 'american_express':
				ame_tot = ame_tot + pm_line.subtotal

			elif pm_line.method == 'diners':
				din_tot = din_tot + pm_line.subtotal

			elif pm_line.method == 'credit_master':
				mac_tot = mac_tot + pm_line.subtotal

			elif pm_line.method == 'debit_master':
				mad_tot = mad_tot + pm_line.subtotal

			elif pm_line.method == 'credit_visa':
				vic_tot = vic_tot + pm_line.subtotal

			elif pm_line.method == 'debit_visa':
				vid_tot = vid_tot + pm_line.subtotal


	# Form
	#self.cash_tot = cash_tot
	self.cash_tot = cash_tot - self.crn_tot
	self.ame_tot = ame_tot
	self.din_tot = din_tot
	self.mac_tot = mac_tot
	self.mad_tot = mad_tot
	self.vic_tot = vic_tot
	self.vid_tot = vid_tot

# set_form_totals




	# Update
	@api.multi
	def update(self):
		#self.update_month()  	# Dep !
