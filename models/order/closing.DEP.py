# 30 Dec 2019



	# Closing Proof
	#closing_proof = fields.Many2one(
	#		'openhealth.closing.proof', 
	#	)



# ----------------------------------------------------------- Set Totals ---------------------------

	def set_sub_totals(self):
		"""
		Set Sub Totals
		"""
		print()
		print('2019 - Set Sub totals')

		
		# Totals - Form
		self.total_form = self.cash_tot + self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot + \
							self.bbva_tot + self.interbank_tot + self.scotiabank_tot + self.bcp_tot

		self.total_form_wblack = self.total_proof_wblack
		self.cash_tot_wblack = self.cash_tot - (self.total_form - self.total_form_wblack)



		# Subtotals
		self.total_cash = self.cash_tot

		self.total_cards = self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot

		self.total_banks = self.bbva_tot + self.interbank_tot + self.scotiabank_tot + self.bcp_tot

	# set_sub_totals







		#if True:
		if False:

			# Create Closing Proof
			self.closing_proof = self.env["openhealth.closing.proof"].create({
																				'name': 'Closing Proof',
																				'date': self.date,
																		})
			# Analise
			self.closing_proof.analyse()



			# Get Totals
			self.rec_tot, self.serial_nr_first_rec, self.serial_nr_last__rec, \
				self.inv_tot, self.serial_nr_first_inv, self.serial_nr_last_inv, \
				self.tkr_tot, self.serial_nr_first_tkr, self.serial_nr_last_tkr, \
				self.tki_tot, self.serial_nr_first_tki, self.serial_nr_last_tki, \
				self.adv_tot, self.serial_nr_first_adv, self.serial_nr_last_adv, \
				self.san_tot, self.serial_nr_first_san, self.serial_nr_last_san, \
				self.crn_tot, self.serial_nr_first_crn, self.serial_nr_last_crn = self.closing_proof.get_totals()

			print('mark 4')
			print(self.serial_nr_first_crn)
			print(self.serial_nr_last_crn)



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
