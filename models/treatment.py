# -*- coding: utf-8 -*-
"""
		*** Treatment

		Created: 			26 Aug 2016
		Last up: 	 		21 Jan 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import reco_funcs
from . import pl_creates
from . import pl_test_treatment

class Treatment(models.Model):

	_inherit = 'openhealth.treatment'


# ----------------------------------------------------------- Actions --------------------------
	# co2
	@api.multi
	def create_service_co2(self):

		family = 'laser'
		subfamily = 'co2'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# excilite
	@api.multi
	def create_service_excilite(self):

		family = 'laser'
		subfamily = 'excilite'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)

		return ret


	# ipl
	@api.multi
	def create_service_ipl(self):

		family = 'laser'
		subfamily = 'ipl'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret



	# ndyag
	@api.multi
	def create_service_ndyag(self):

		family = 'laser'
		subfamily = 'ndyag'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# quick
	@api.multi
	def create_service_quick(self):

		family = 'laser'
		subfamily = 'quick'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret





	# medical
	@api.multi
	def create_service_medical(self):

		family = 'medical'
		subfamily = 'medical'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# cosmetology
	@api.multi
	def create_service_cosmetology(self):

		family = 'cosmetology'
		subfamily = 'cosmetology'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret


	# product
	@api.multi
	def create_service_product(self):

		family = 'topical'
		subfamily = 'product'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret





	# gynecology
	@api.multi
	def create_service_gynecology(self):

		family = 'gynecology'
		subfamily = 'gynecology'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret

	# echography
	@api.multi
	def create_service_echography(self):

		family = 'echography'
		subfamily = 'echography'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret

	# promotion
	@api.multi
	def create_service_promotion(self):

		family = 'promotion'
		subfamily = 'promotion'
		treatment_id = self.id 

		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)
		
		return ret




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
			pl_test_treatment.reset_treatment(self)


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
			#pl_test_treatment.reset_treatment(self)

			# Test Integration
			pl_test_treatment.test_integration_treatment(self)







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
																				#('x_name_short', '=', product_id.x_name_short),
																				('name', '=', product_id.name),
																				('sale_ok', '=', True),
																				('pl_price_list', '=', '2019'),
												])

					print(product_template)
					print(product_template.name)


					subtype = product_template.x_treatment

					#ret = cre.create_procedure_go(self, date_app, subtype, product_id.id)
					ret = pl_creates.create_procedure_go(self, date_app, subtype, product_id.id)










# ----------------------------------------------------------- Computes --------------------------
	@api.multi
	def _compute_nr_services(self):
		for record in self:

			#co2 = self.env['openhealth.service.co2'].search_count([('treatment', '=', record.id),])
			#exc = self.env['openhealth.service.excilite'].search_count([('treatment', '=', record.id),])
			#ipl = self.env['openhealth.service.ipl'].search_count([('treatment', '=', record.id),])
			#ndyag = self.env['openhealth.service.ndyag'].search_count([('treatment', '=', record.id),])
			#quick =	self.env['openhealth.service.quick'].search_count([('treatment', '=', record.id),])
			#medical = self.env['openhealth.service.medical'].search_count([('treatment', '=', record.id),])
			#vip = self.env['openhealth.service.vip'].search_count([('treatment', '=', record.id),])
			#product = self.env['openhealth.service.product'].search_count([('treatment', '=', record.id),])

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




# ----------------------------------------------------------- Fields --------------------------
	# Shopping cart
	shopping_cart_ids = fields.One2many(
			
			'price_list.cart_line',
			
			'treatment',
			
			string="Shopping Cart"
		)





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


			#if service.service.name not in [False]:
			if product.name not in [False]:

				cart_line = self.shopping_cart_ids.create({
																	#'product': 	service.service.id,
																	'product': 		product.id,

																	'price': 		service.price_applied,

																	'qty': 			service.qty,

																	'treatment': 	self.id,
														})




		order = pl_creates.pl_create_order(self)

		print(order)


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




# ----------------------------------------------------------- Fields --------------------------
	# gynecology
	service_gynecology_ids = fields.One2many(			
			'price_list.service_gynecology',
			'treatment',
			string="Servicios Ginecologia"
			)

	# echography
	service_echography_ids = fields.One2many(

			#'openhealth.service.echography',
			'price_list.service_echography',

			'treatment',
			string="Servicios Ecografia"
			)
	
	# promotion
	service_promotion_ids = fields.One2many(
			
			#'openhealth.service.promotion',
			'price_list.service_promotion',
			
			'treatment',
			string="Servicios Promocion"
			)



