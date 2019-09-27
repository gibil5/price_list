# 27 sep 2019


# Dep
# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_chav(self):
		"""
		Create Order Consultation Dr. Chavarri
		"""
		print()
		print('PL - Create Order Con Chav')

		target = 'premium'

		order = self.create_order_con_target(target)

		# Open Order
		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
				# Views
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',
				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False,
				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						},
				'context': {}
			}


# Dep
# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_gyn(self):
		"""
		Create Order Consultation Gynecology
		"""
		print()
		print('PL - Create Order Con Gyn')

		target = 'gynecology'

		order = self.create_order_con_target(target)

		# Open Order
		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
				# Views
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',
				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False,
				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						},
				'context': {}
			}




# Dup
# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def create_procedure_man(self):
		"""
		Create Procedure Manual
		"""
		print()
		print('Pl - Create Procedure - Manual - 1')

		# Loop - Create Procedures
		ret = 0
		for order in self.order_pro_ids:

			if order.state == 'sale':

				# Update
				order.x_procedure_created = True

				# Loop
				for line in order.order_line:

					# Init
					date_app = order.date_order
					product_id = line.product_id
					product_template = self.env['product.template'].search([
																				('x_name_short', '=', product_id.x_name_short),
												])
					subtype = product_template.x_treatment

					# Create - This
					ret = cre.create_procedure_go(self, date_app, subtype, product_id.id)

	# create_procedure_man














# 26 sep 2019

# ----------------------------------------------------------- Price List Fields - Relational ----------------------------------------------

	#report_product = fields.Many2one(
	#		'price_list.container',
	#		string="PROD",
			#required=True,
	#	)






# 30 Aug


# ----------------------------------------------------------- Pricelist Fields - Test --------------------------------

	x_test_scenario = fields.Selection(
			[
				('all', 'All'),
				('product', 'product'),
				('laser', 'laser'),
				('cosmetology', 'cosmetology'),
				('medical', 'medical'),
				('new', 'new'),
			],
			string="Test Scenarios",
		)


	test_pricelist_2019 = fields.Boolean(
			#'Price List 2019',
			'PL 2019',
			default=False,
		)

	test_pricelist_2018 = fields.Boolean(
			#'Price List 2018',
			'PL 2018',
			default=False,
		)



# ----------------------------------------------------------- Price List Fields - Relational ----------------------------------------------
	# Management
	report_management = fields.Many2one(
			'openhealth.management',
			string="MGT",
		)

	# Marketing
	report_marketing = fields.Many2one(
			'openhealth.marketing',
			string="MKT",
		)

	# Contasis
	report_contasis = fields.Many2one(
			'openhealth.account.contasis',
			string="ACC",
		)

	# Txt
	report_account = fields.Many2one(
			'openhealth.container',
			string="TXT",
		)






# ----------------------------------------------------------- Test One --------------------------
	@api.multi
	def test_one(self):
		#print()
		#print('Test One')
		test_treatment.test_one(self)

# ----------------------------------------------------------- Test two --------------------------
	@api.multi
	def test_two(self):
		#print()
		#print('Test Two')
		test_treatment.test_two(self)




# ----------------------------------------------------------- Computes --------------------------
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:
			record.nr_invoices_pro = self.env['sale.order'].search_count([
																			('treatment', '=', record.id),
																			('x_family', '=', 'procedure'),
																			('state', '=', 'sale'),
																	])


	
	@api.multi
	#@api.depends('consultation_ids')
	def _compute_state(self):
		for record in self:

			# Init
			state = 'empty'


			if record.treatment_closed:
				state = 'done'

			elif record.nr_controls > 0:
				state = 'controls'

			elif record.nr_sessions > 0:
				state = 'sessions'

			elif record.nr_procedures > 0:
				state = 'procedure'

			elif record.nr_invoices_pro > 0:
				state = 'invoice_procedure'

			elif record.nr_budgets_pro > 0:
				state = 'budget_procedure'

			elif record.nr_services > 0:
				state = 'service'

			elif record.consultation_progress == 100:
				state = 'consultation'

			elif record.nr_invoices_cons > 0:
				state = 'invoice_consultation'

			elif record.nr_budgets_cons > 0:
				state = 'budget_consultation'

			elif record.nr_appointments > 0:
				state = 'appointment'


			# Assign
			record.state = state

	# _compute_state



