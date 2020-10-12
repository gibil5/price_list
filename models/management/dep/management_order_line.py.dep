# 9 Dec 2019



# ----------------------------------------------------------- 2019 !!! ------------------------------------------------------
	
	# Update Fields
	@api.multi
	def pl_update_fields(self):
		#print()
		#print('Pl - Update Fields - Order - 2019')


		# If Service 
		if self.product_id.type in ['service']: 	# Service

			# Family 

			if self.product_id.pl_subfamily in ['consultation']:
				self.family = self.product_id.pl_subfamily
			else:
				self.family = self.product_id.pl_family



			# Sub family 
			# Cosmetology 
			#if self.product_id.x_family == 'cosmetology': 
			if self.product_id.pl_subfamily == 'cosmetology': 
				self.sub_family = 'cosmetology'

			# Medical, Other 
			else: 
				#self.sub_family = self.product_id.x_treatment 
				self.sub_family = self.product_id.pl_treatment 



		# If Product 
		#if self.product_id.type in ['product','consu']: 	# Products and Consumables 
		if self.product_id.type in ['product']: 	# Products and Consumables 

			# Family 
			self.family = self.product_id.pl_family
			
			# Sub family
			self.sub_family = self.product_id.pl_subfamily

	# pl_update_fields





# ----------------------------------------------------------- 2018 ------------------------------------------------------
	
	# Update Fields
	@api.multi
	def update_fields(self):
		#print()
		#print('Update Fields - Order - 2018')


		# If Product 
		if self.product_id.type in ['product','consu']: 	# Products and Consumables 
			# Family 
			if self.product_id.x_family in ['kit']: 	# Kits 
				self.family = 'topical'
			else: 										# Vip and Topical 
				self.family = self.product_id.x_family
			# Sub family
			self.sub_family = 'product'


		# If Service 
		else: 

			# Family 
			self.family = self.product_id.x_family

			# Correct 
			if (self.product_id.x_family  == 'consultation'): 
				if self.price_unit  == 100: 
					self.family = 'consultation_100'			
				elif self.price_unit  == 0: 
					self.family = 'consultation_0'

			# Sub family 
			# Cosmetology 
			if self.product_id.x_family == 'cosmetology': 
				self.sub_family = 'cosmetology'

			# Medical, Other 
			else: 
				self.sub_family = self.product_id.x_treatment 

	# update_fields


	