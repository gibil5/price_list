# -*- coding: utf-8 -*-
"""
		*** Treatment

		treatment.py

		Created: 			26 Aug 2016
		Last up: 	 		19 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import reco_funcs
from . import pl_creates
from . import test_treatment

class Treatment(models.Model):

	_inherit = 'openhealth.treatment'




# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def create_procedure_man(self):
		print()
		print('Pl - Create Procedure - Manual')


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







# ----------------------------------------------------------- Opens a new Form - Service ------------------------------

	@api.multi
	def create_order_con(self):
		"""
		Create Service
		Opens a new form. For Reco choice. 
		"""
		print()
		print('Pl - Create Order Con')

		# Init
		res_id = self.id
		res_model = 'openhealth.treatment'
		#view_id = self.env.ref('openhealth.treatment_2_form_view').id
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





# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_chav(self):
		print()
		print('Create Order Con Chav')
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

# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_gyn(self):
		print()
		print('Create Order Con Gyn')
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


# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_med(self):
		print()
		print('Create Order Con Med')
		target = 'medical'

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



# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	#def create_order_con(self):
	def create_order_con_target(self, target):
		print()
		print('Create Order Con Med')

		# Init
		#target = 'consultation'


		#order = cre.create_order(self, target)
		#order = pl_creates.pl_create_order_con(self)


		# Create Cart


		# Create Order
		#order = pl_creates.pl_create_order_con(self)
		order = pl_creates.pl_create_order_con(self, target)

		#print(order)

		return order

	# create_order_con





# ----------------------------------------------------------- Opens a new Form - Service ------------------------------

	@api.multi
	def create_service(self):
		"""
		Create Service
		Opens a new form. For Reco choice. 
		"""
		print()
		print('Pl - Create Service')

		# Init
		res_id = self.id
		res_model = 'openhealth.treatment'
		view_id = self.env.ref('openhealth.treatment_2_form_view').id

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
	# create_service









# -----------------------------------------------------------  Create Order Pro  ------------------
	@api.multi
	def create_order_pro(self):
		print('Create Order Pro')

		# Clear
		self.shopping_cart_ids.unlink()

		service_list = [
							self.service_co2_ids,
							self.service_excilite_ids,
							self.service_ipl_ids,
							self.service_ndyag_ids,
							self.service_quick_ids,
							self.service_medical_ids,
							self.service_cosmetology_ids,
							self.service_product_ids,
							self.service_gynecology_ids,
							self.service_echography_ids,
							self.service_promotion_ids,
		]


		# Create Cart
		for service in service_list:
			print(service.service)
			print(service.service.name)
			print(service.service.id)
			print(service.price_applied)
			print(service.qty)


			# Product
			product = self.env['product.product'].search([
															('name', '=', service.service.name),
															('sale_ok', '=', True),
															('pl_price_list', '=', '2019'),
											])
			print(product)
			print(product.name)


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

		print(order)


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
	# create_order_pro






# ----------------------------------------------------------- Fields --------------------------

	# co2
	service_co2_ids = fields.One2many(			
			'price_list.service_co2',
			'treatment',
			string="Servicios Co2"
			)

	# excilite
	service_excilite_ids = fields.One2many(			
			'price_list.service_excilite',
			'treatment',
			string="Servicios excilite"
			)

	# ipl
	service_ipl_ids = fields.One2many(			
			'price_list.service_ipl',
			'treatment',
			string="Servicios ipl"
			)

	# ndyag
	service_ndyag_ids = fields.One2many(			
			'price_list.service_ndyag',
			'treatment',
			string="Servicios ndyag"
			)

	# medical
	service_medical_ids = fields.One2many(			
			'price_list.service_medical',
			'treatment',
			string="Servicios medical"
			)

	# cosmetology
	service_cosmetology_ids = fields.One2many(			
			'price_list.service_cosmetology',
			'treatment',
			string="Servicios cosmetology"
			)

	# quick
	service_quick_ids = fields.One2many(			
			'price_list.service_quick',
			'treatment',
			string="Servicios quick"
			)

	# product
	service_product_ids = fields.One2many(			
			'price_list.service_product',
			'treatment',
			string="Servicios product"
			)

	# gynecology
	service_gynecology_ids = fields.One2many(			
			'price_list.service_gynecology',
			'treatment',
			string="Servicios Ginecologia"
			)

	# echography
	service_echography_ids = fields.One2many(
			'price_list.service_echography',
			'treatment',
			string="Servicios Ecografia"
			)
	
	# promotion
	service_promotion_ids = fields.One2many(			
			'price_list.service_promotion',
			'treatment',
			string="Servicios Promocion"
			)



	# Shopping cart
	shopping_cart_ids = fields.One2many(
			'price_list.cart_line',
			'treatment',
			string="Shopping Cart"
		)

# ----------------------------------------------------------- Actions --------------------------
	# co2
	@api.multi
	def create_service_co2(self):
		# Init
		family = 'laser'
		subfamily = 'co2'
		treatment_id = self.id 
		physician_id = self.physician.id

		# Create
		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# excilite
	@api.multi
	def create_service_excilite(self):
		# Init
		family = 'laser'
		subfamily = 'excilite'
		treatment_id = self.id 
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)

		return ret


	# ipl
	@api.multi
	def create_service_ipl(self):
		# Init
		family = 'laser'
		subfamily = 'ipl'
		treatment_id = self.id 
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# ndyag
	@api.multi
	def create_service_ndyag(self):
		# Init
		family = 'laser'
		subfamily = 'ndyag'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# quick
	@api.multi
	def create_service_quick(self):
		# Init
		family = 'laser'
		subfamily = 'quick'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# medical
	@api.multi
	def create_service_medical(self):
		# Init
		family = 'medical'
		subfamily = 'medical'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# cosmetology
	@api.multi
	def create_service_cosmetology(self):
		# Init
		family = 'cosmetology'
		subfamily = 'cosmetology'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# product
	@api.multi
	def create_service_product(self):
		# Init
		family = 'topical'
		subfamily = 'product'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# gynecology
	@api.multi
	def create_service_gynecology(self):
		# Init
		family = 'gynecology'
		subfamily = 'gynecology'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# echography
	@api.multi
	def create_service_echography(self):
		# Init
		family = 'echography'
		subfamily = 'echography'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# promotion
	@api.multi
	def create_service_promotion(self):
		# Init
		family = 'promotion'
		subfamily = 'promotion'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret



# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def create_procedure_man(self):
		print()
		print('Pl - Create Procedure - Manual')

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

					# Search
					product_template = self.env['product.template'].search([
																				('name', '=', product_id.name),
																				('sale_ok', '=', True),
																				('pl_price_list', '=', '2019'),
												])
					print(product_template)
					print(product_template.name)

					subtype = product_template.x_treatment

					# Create
					ret = pl_creates.create_procedure_go(self, date_app, subtype, product_id.id)
	# create_procedure_man




# ----------------------------------------------------------- Computes --------------------------
	@api.multi
	def _compute_nr_services(self):
		for record in self:
			co2 = self.env['price_list.service_co2'].search_count([('treatment', '=', record.id),])
			exc = self.env['price_list.service_excilite'].search_count([('treatment', '=', record.id),])
			ipl = self.env['price_list.service_ipl'].search_count([('treatment', '=', record.id),])
			ndyag = self.env['price_list.service_ndyag'].search_count([('treatment', '=', record.id),])
			quick =	self.env['price_list.service_quick'].search_count([('treatment', '=', record.id),])
			medical = self.env['price_list.service_medical'].search_count([('treatment', '=', record.id),])			
			cosmetology = self.env['price_list.service_cosmetology'].search_count([('treatment', '=', record.id),])
			product = self.env['price_list.service_product'].search_count([('treatment', '=', record.id),])
			gynecology = self.env['price_list.service_gynecology'].search_count([('treatment', '=', record.id),])
			echography = self.env['price_list.service_echography'].search_count([('treatment', '=', record.id),])
			promotion = self.env['price_list.service_promotion'].search_count([('treatment', '=', record.id),])
			record.nr_services = quick + co2 + exc + ipl + ndyag + medical + cosmetology + product + gynecology + echography + promotion



# ----------------------------------------------------------- Test --------------------------------
	# Test
	@api.multi
	def test(self):
		print()
		print('Treatment - Test')
		if self.patient.x_test:
			self.test_reset()
			self.test_integration()
			#self.test_create_recos()
			#self.test_computes()
			#self.test_libs()

# ----------------------------------------------------------- Test Reset --------------------------
	@api.multi
	def test_reset(self):
		print()
		print('Test Case - Reset')
		if self.patient.x_test:
			test_treatment.reset_treatment(self)

# ----------------------------------------------------------- Test Integration --------------------
	@api.multi
	def test_integration(self):
		"""
		Integration Test of the Treatment Class.
		"""
		print()
		print('Test Integration')
		if self.patient.x_test:
			# Reset
			#test_treatment.reset_treatment(self)
			# Test Integration
			test_treatment.test_integration_treatment(self)

