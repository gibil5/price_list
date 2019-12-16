




# 10 Dec 2019

# ----------------------------------------------------------- Correct ----------------------------------------------------

	corr_medical = fields.Boolean(
		)

	corr_cosmetology = fields.Boolean(
		)

# ----------------------------------------------------------- Getters -------------------------

	# Get Treatment
	#@api.multi
	def get_treatment(self):
		"""
		Get Product Treatment
		Used by: Session, Control.
		"""

		# Init
		_dic = {
					'LASER CO2 FRACCIONAL': 	'laser_co2',
					'QUICKLASER': 				'laser_quick',
					'LASER EXCILITE':			'laser_excilite',
					'LASER M22 IPL':			'laser_ipl',
					'LASER M22 ND YAG':			'laser_ndyag',
		}

		treatment = False


		print(self.pl_treatment)


		if self.pl_price_list in ['2019']:
			if self.pl_treatment in _dic:
				treatment = _dic[self.pl_treatment]
			else:
				print('Error: 1')


		elif self.pl_price_list in ['2018']:
			treatment = self.x_treatment

		else:
			print('Error: 2')


		return treatment




# ----------------------------------------------------------- Correct ----------------------------------------------------
	@api.multi
	def correct_subfamilies(self):
		"""
		Update
		"""
		print()
		print('Correct Subfamilies')


		model = 'product.template'

		family = ''


		if self.corr_medical:
			family = 'medical'

		if self.corr_cosmetology:
			family = 'cosmetology'



		# Search
		products = self.env[model].search([
														#('name', '=', name),
														('pl_price_list', 'in', ['2019']),
				
														('pl_family', 'in', [family]),
											],
												#order='date_order desc',
												#limit=1,
									)
		print(products)



		_dic_med = {
					'VICTAMINA C ENDOVENOSA': 	'vitamin_c_intravenous',

					'INFILTRACIONES': 		'infiltrations',
					'CRIOCIRUGIA': 			'cryosurgery',
					'ESCLEROTERAPIA': 		'sclerotherapy',
					'PLASMA': 				'plasma',

					'BOTOX': 				'botox',
					'REDUX': 				'redux',
					'ACIDO HIALURONICO': 	'hyaluronic_acid',
					'MESOTERAPIA NCTF': 	'mesotherapy',
		}

		_dic_cos = {

					'CARBOXITERAPIA': 					'carboxytherapy',
					'PUNTA DE DIAMANTES': 				'diamond_tip',
					'LASER TRIACTIVE + CARBOXITERAPIA': 'laser_triactive_carboxytherapy',
		}


		for product in products:
			print(product.name)
			print(product.pl_family)
			print(product.pl_treatment)
			print(product.pl_subfamily)
			print()

			if product.pl_family in ['medical']:
				product.pl_subfamily = _dic_med[product.pl_treatment]

			elif product.pl_family in ['cosmetology']:
				product.pl_subfamily = _dic_cos[product.pl_treatment]










# ----------------------------------------------------------- Update ----------------------------------------------------
	#@api.multi
	#def update(self):
	#	"""
	#	Update
	#	"""
		#print()
		#print('Product Template - Update')
	#	self.pl_idx_int = int(self.pl_idx)
	#	self.purchase_ok = False



# ----------------------------------------------------------- Fix - Button -----------
	@api.multi
	def fix(self):
		"""
		Fix Product
		"""
		print()
		print('Product Fix')

		# Handle Exceptions
		#exc_prod.handle_exceptions(self)
		exc_prod.fix_exceptions(self)


# ----------------------------------------------------------- Validate - Button -----------
	@api.multi
	def validate(self):
		"""
		Validate Product
		"""
		print()
		print('Product Validate')

		# Handle Exceptions
		exc_prod.handle_exceptions(self)


	@api.multi
	def validate_all(self):
		"""
		Validate Product
		"""
		print()
		print('Product Validate All')


		# Search
		products = self.env['product.template'].search([
																	('pl_price_list', 'in', ['2019']),
															],
															#order='pl_prefix,pl_idx_int asc',
															#order='pl_idx_int,pl_prefix asc',
															order='pl_prefix asc',
															#limit=10,
															#limit=100,
															limit=600,
														)
		# Loop
		idx = 0
		for product in products:
			print()
			print(product.name)
	
			idx = idx + 1

			# Handle Exceptions
			exc_prod.handle_exceptions(product)

		print(idx)
