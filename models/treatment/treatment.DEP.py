# 27 Sep 2019


# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	#def create_order_con_target(self, target):
	def create_order_con_target_dep(self, target):
		"""
		Create Order Consultation - Dep
		"""
		print()
		print('PL - Create Order Con Target')

		# Init
		price_list = '2019'

		# Create Order
		order = pl_creates.pl_create_order_con(self, target, price_list)
		#print(order)

		return order

	# create_order_con



# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_target_2018(self, target):
		"""
		Create Order Consultation 2018
		"""
		print()
		print('PL - Create Order Con 2018')

		price_list = '2018'

		# Create Order
		order = pl_creates.pl_create_order_con(self, target, price_list)

		return order

	# create_order_con


# ----------------------------------------------------------- Create Order Con - Dep -------------------
	@api.multi
	#def create_order_con(self):
	def create_order_con_dep(self):
		"""
		Create Order Consultation
		Three modes
		"""
		print()
		print('Pl - Create Order Con')

		# Init
		res_id = self.id
		res_model = 'openhealth.treatment'
		view_id = self.env.ref('openhealth.treatment_3_form_view').id

		# Open
		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',
			# Window action
			'priority': 1,
			'res_id': res_id,
			'res_model': res_model,
			#'view_id': view_id,
			# Views
			#"views": [[False, "form"]],

			"views": [[view_id, "form"]],

			'view_mode': 'form',
			'target': 'current',
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': False, }
					},
			'context': {
						#'default_treatment': treatment_id,
					}
		}
	# create_order_con


# -----------------------------------------------------------  Create Order Procedure - 2018 --------------
	@api.multi
	def create_order_pro_2018(self):
		"""
		Create Order Procedure - 2018
		From Recommendations
		"""
		print()
		print('Pl - Create Order Pro - 2018')

		# Clear
		self.shopping_cart_ids.unlink()

		# Init
		price_list = '2018'

		service_list = [
							self.service_product_ids,
							self.service_co2_ids,
							self.service_excilite_ids,
							self.service_ipl_ids,
							self.service_ndyag_ids,
							self.service_quick_ids,
							self.service_medical_ids,
							self.service_cosmetology_ids,
							self.service_gynecology_ids,
							self.service_echography_ids,
							self.service_promotion_ids,
		]

		# Create Cart
		for service_ids in service_list:
			for service in service_ids:

				if (service.service.name not in [False]) and (service.service.pl_price_list in [price_list]):

					#print()
					#print(service.service.name)

					# Product
					product = self.env['product.product'].search([
																	('name', '=', service.service.name),
																	('pl_price_list', '=', price_list),
													],
														order='create_date desc',
														limit=1,
													)
					#print(product)
					#print(product.name)
					#print()
					#print()


					# Manage Exception
					try:
						product.ensure_one()

					except:
						#print("An exception occurred")
						msg_name = "ERROR: Record Must be One Only."
						class_name = type(product).__name__
						obj_name = service.service.name
						msg =  msg_name + '\n' + class_name + '\n' + obj_name

						raise UserError(_(msg))

					# Create Cart
					if product.name not in [False]:
						cart_line = self.shopping_cart_ids.create({
																			'product': 		product.id,
																			'price': 		service.price_applied,
																			'qty': 			service.qty,
																			'treatment': 	self.id,
																})
		# Create Order
		order = pl_creates.pl_create_order(self)
		#print(order)

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
	# create_order_pro_2018
