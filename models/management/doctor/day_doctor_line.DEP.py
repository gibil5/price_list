# 7 Dec 2019





# ----------------------------------------------------------- Update ------------------------------
	@api.multi
	def update_macro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update - Macro')

		# Clean		
		self.reset_macro()

		for line in self.order_line:
			self.amount = self.amount + line.price_total

			if line.product_id.x_family in ['consultation']:
				self.nr_consultations = self.nr_consultations + line.product_uom_qty

			if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty


		if self.nr_consultations != 0:
			print('Gotcha !')
			self.ratio_pro_con = float(self.nr_procedures) / float(self.nr_consultations)

	# update_macro
