



# ----------------------------------------------------------- PROD ------------------------------------------------------

# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':

			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily


			self.pl_manufacturer = self.service.pl_manufacturer
			self.pl_brand = self.service.pl_brand

			self.pl_price = self.service.list_price
			self.pl_price_company = self.service.pl_price_company







# ----------------------------------------------------------- COSMETO ------------------------------------------------------

# ----------------------------------------------------------- Natives ------------------------------
	pl_qty = fields.Integer(
			default=1,
		)

	pl_price_policy = fields.Selection(
			selection=pl_vars._price_policy_list,
			string='Tipo de Precio',
		)


# ----------------------------------------------------------- On changes --------------------------

	# Price policy
	@api.onchange('pl_price_policy')
	def _onchange_pl_price_policy(self):		
		
		if self.pl_price_policy in ['normal']:
			self.price_applied = self.service.list_price

		elif self.pl_price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip

		elif self.pl_price_policy in ['company']:
			self.price_applied = self.service.pl_price_company

		elif self.pl_price_policy in ['manual']:
			self.price_applied = self.price_manual



# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max











# ----------------------------------------------------------- MED ------------------------------------------------------

# ----------------------------------------------------------- Natives ------------------------------
	pl_qty = fields.Integer(
			default=1,
		)

	pl_price_policy = fields.Selection(
			selection=pl_vars._price_policy_list,
			string='Tipo de Precio',
		)


# ----------------------------------------------------------- On changes --------------------------

	# Price policy
	@api.onchange('pl_price_policy')
	def _onchange_pl_price_policy(self):		
		
		if self.pl_price_policy in ['normal']:
			self.price_applied = self.service.list_price

		elif self.pl_price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip

		elif self.pl_price_policy in ['company']:
			self.price_applied = self.service.pl_price_company

		elif self.pl_price_policy in ['manual']:
			self.price_applied = self.price_manual



# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max











# ----------------------------------------------------------- QUICK ------------------------------------------------------

# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max














# ----------------------------------------------------------- NDYAG ------------------------------------------------------

# ----------------------------------------------------------- Natives ------------------------------
	pl_qty = fields.Integer(
			default=1,
		)

	pl_price_policy = fields.Selection(
			selection=pl_vars._price_policy_list,
			string='Tipo de Precio',
		)

# ----------------------------------------------------------- On changes --------------------------

	# Price policy
	@api.onchange('pl_price_policy')
	def _onchange_pl_price_policy(self):		
		
		if self.pl_price_policy in ['normal']:
			self.price_applied = self.service.list_price

		elif self.pl_price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip

		elif self.pl_price_policy in ['company']:
			self.price_applied = self.service.pl_price_company

		elif self.pl_price_policy in ['manual']:
			self.price_applied = self.price_manual




# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max














# ----------------------------------------------------------- IPL ------------------------------------------------------

# ----------------------------------------------------------- Natives ------------------------------
	pl_qty = fields.Integer(
			default=1,
		)

	pl_price_policy = fields.Selection(
			selection=pl_vars._price_policy_list,
			string='Tipo de Precio',
		)

# ----------------------------------------------------------- On changes --------------------------

	# Price policy
	@api.onchange('pl_price_policy')
	def _onchange_pl_price_policy(self):		
		
		if self.pl_price_policy in ['normal']:
			self.price_applied = self.service.list_price

		elif self.pl_price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip

		elif self.pl_price_policy in ['company']:
			self.price_applied = self.service.pl_price_company

		elif self.pl_price_policy in ['manual']:
			self.price_applied = self.price_manual



# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max






# ----------------------------------------------------------- EXC ------------------------------------------------------



# ----------------------------------------------------------- Natives ------------------------------
	pl_qty = fields.Integer(
			default=1,
		)


	pl_price_policy = fields.Selection(
			selection=pl_vars._price_policy_list,
			string='Tipo de Precio',
		)




# ----------------------------------------------------------- On changes --------------------------

	# Price policy
	@api.onchange('pl_price_policy')
	def _onchange_pl_price_policy(self):		
		
		if self.pl_price_policy in ['normal']:
			self.price_applied = self.service.list_price

		elif self.pl_price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip

		elif self.pl_price_policy in ['company']:
			self.price_applied = self.service.pl_price_company

		elif self.pl_price_policy in ['manual']:
			self.price_applied = self.price_manual






# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max













# ----------------------------------------------------------- CO2 ------------------------------------------------------




# ----------------------------------------------------------- Natives ------------------------------
	pl_qty = fields.Integer(
			default=1,
		)


	pl_price_policy = fields.Selection(
			selection=pl_vars._price_policy_list,
			string='Tipo de Precio',
		)



# ----------------------------------------------------------- On changes --------------------------

	# Price policy
	@api.onchange('pl_price_policy')
	def _onchange_pl_price_policy(self):		
		
		if self.pl_price_policy in ['normal']:
			self.price_applied = self.service.list_price

		elif self.pl_price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip

		elif self.pl_price_policy in ['company']:
			self.price_applied = self.service.pl_price_company

		elif self.pl_price_policy in ['manual']:
			self.price_applied = self.price_manual




# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.pl_family = self.service.pl_family
			self.pl_subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.pl_zone = self.service.pl_zone
			self.pl_pathology = self.service.pl_pathology

			self.pl_level = self.service.pl_level
			self.pl_sessions = self.service.pl_sessions
			self.pl_time = self.service.pl_time


			self.pl_price = self.service.list_price
			self.pl_price_vip = self.service.pl_price_vip
			self.pl_price_company = self.service.pl_price_company

			self.pl_price_session = self.service.pl_price_session
			self.pl_price_session_next = self.service.pl_price_session_next
			self.pl_price_max = self.service.pl_price_max

