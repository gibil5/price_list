# -*- coding: utf-8 -*-
"""
		*** Treatment

		Created: 			26 Aug 2016
		Last up: 	 		27 Sep 2019

	- A Class exposes abstract interfaces that allow its users to manipulate the Essence of the data, without having to know its Implementation. 
	- Respect the Law of Demeter. Avoid Train Wrecks.
	- Treat the Active Record as a data structure and create separate objects that contain the business rules and that hide their internal data. These Objects are just instances of the Active Record.	
	- Handle Exceptions.
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError
from . import reco_funcs

from . import pl_creates

from . import test_treatment
from . import exc_tre

from . import pl_user
from . import time_funcs

class Treatment(models.Model):
	"""
	Class Treatment
	Extends the Business Rules. Should not extend the Data Model.
	Should contain only functions and libraries.

	All Creation Buttons should be Here.
	"""
	_inherit = 'openhealth.treatment'




# ----------------------------------------------------- Create Procedures ---------------------------------------------


# ----------------------------------------------------------- Create Procedure  -------------------
	# Create Procedure
	#@api.multi
	#def create_procedure(self, product):
	def create_procedure_auto(self, product):
		"""
		Used by: Order
		Uses: Price List PL-Creates Library
		"""
		print()
		print('PL - Create Procedure Auto')
		print(self)
		print(product)

		pl_creates.create_procedure_go(self, product)

	# create_procedure



# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def create_procedure_man(self):
		"""
		Create Procedure Manual
		"""
		print()
		print('Pl - Create Procedure - Manual - 2')


		# Loop
		for order in self.order_pro_ids:

			#if order.state == 'sale':
			#if (order.state == 'sale')	and  (not order.x_procedure_created):
			if (order.state == 'sale')	and  (not order.is_procedure_created()):


				# Update Order
				order.set_procedure_created(True)


				# Loop
				for line in order.order_line:

					print(line.product_id)

					if line.product_id.is_procedure():

						product_product = line.product_id

						# Create
						pl_creates.create_procedure_go(self, product_product)

	# create_procedure_man





# ----------------------------------------------------- Create Orders ---------------------------------------------

# -----------------------------------------------------------  Create Order Procedure - 2019 -------------
	@api.multi
	def create_order_pro(self):
		"""
		Create Order Procedure - 2019
		From Recommendations
		"""
		print('PL - Create Order Pro')

		# Clear
		self.shopping_cart_ids.unlink()

		# Init
		price_list = '2019'

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

				if (service.service.name not in [False]) 	and 	(service.service.pl_price_list in [price_list]):

					#print(service.service.name)

					#print(service.service)
					#print(service.service.id)
					#print(service.price_applied)
					#print(service.qty)
					#print()

					# Product
					product = self.env['product.product'].search([
																	('name', '=', service.service.name),
																	('sale_ok', '=', True),

																	('pl_price_list', '=', '2019'),
													])
					#print(product)
					#print(product.name)
					#print()
					#print()

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
	# create_order_pro



# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	#def create_order_con_med(self):
	def create_order_con(self):
		"""
		Create Order Consultation Standard - Medical
		One mode
		"""
		print()
		print('PL - Create Order Con Med')

		# Init
		price_list = '2019'
		target = 'medical'

		#order = self.create_order_con_target(target)
		order = pl_creates.pl_create_order_con(self, target, price_list)

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





# ----------------------------------------------------- Create Consultations ---------------------------------------------

# ----------------------------------------------------- Create Consultation -----------------------
	# Create Consultation
	@api.multi
	def create_consultation(self):
		print()
		print('PL - Create Consultation')

		# Init vars
		patient_id = self.patient.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint

		# Doctor
		doctor = pl_user.get_actual_doctor(self)
		doctor_id = doctor.id
		if doctor_id == False:
			doctor_id = self.physician.id

		# Date
		GMT = time_funcs.Zone(0, False, 'GMT')
		evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		# Search
		consultation = self.env['openhealth.consultation'].search([
																		('treatment', '=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)

		# If Consultation not exist
		if consultation.name == False:
			# Create
			consultation = self.env['openhealth.consultation'].create({
																		'patient': patient_id,
																		'treatment': treatment_id,
																		'evaluation_start_date': evaluation_start_date,
																		'chief_complaint': chief_complaint,
																		'doctor': doctor_id,
													})

		return {

			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action

			'res_model': 'openhealth.consultation',
			#'res_id': consultation_id,
			'res_id': consultation.id,

			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#'view_id': 'oeh_medical_evaluation_view',
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
					},
			'context':   {
							'search_default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_treatment': treatment_id,
							'default_evaluation_start_date': evaluation_start_date,
							'default_chief_complaint': chief_complaint,
			}
		}

	# create_consultation




# ----------------------------------------------------- Create Services ---------------------------------------------

# ----------------------------------------------------------- Create Service ---------------------------

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




# ----------------------------------------------------------- Fields - Services ------------------------
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

# ----------------------------------------------------------- Actions - Serivces --------------------------
	# co2
	@api.multi
	def create_service_co2(self):
		"""
		Create Service Co2
		"""
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
		"""
		Create Service Excilite
		"""
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
		"""
		Create Service Ipl
		"""
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
		"""
		Create Service Ndyag
		"""
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
		"""
		Create Service Quick
		"""
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
		"""
		Create Service Medical
		"""
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
		"""
		Create Service Cosmetology
		"""
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
		"""
		Create Service Product
		"""
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
		"""
		Create Service Gynecology
		"""
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
		"""
		Create Service Echography
		"""
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
		"""
		Create Service Promotion
		"""
		# Init
		family = 'promotion'
		subfamily = 'promotion'
		treatment_id = self.id
		physician_id = self.physician.id

		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)

		return ret





# ----------------------------------------------------------- Computes - Serivces --------------------------
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




# ----------------------------------------------------------- Test ----------------------------------------------------



# ----------------------------------------------------------- Test All Cycle - Step by Step --------------------------
	@api.multi
	def test_create_budget_consultation(self):
		"""
		Test
		"""
		print()
		print('Test Create Budget Consultation')
		test_treatment.test_create_budget_consultation(self)


	@api.multi
	def test_create_sale_consultation(self):
		"""
		Test
		"""
		print()
		print('Test Create Sale Consultation')
		test_treatment.test_create_sale_consultation(self)


	@api.multi
	def test_create_consultation(self):
		"""
		Test
		"""
		print()
		print('Test Create Consultation')
		test_treatment.test_create_consultation(self)


	@api.multi
	def test_create_recommendations(self):
		"""
		Test
		"""
		print()
		print('Test Create Recommendations')
		test_treatment.test_create_recommendations(self)


	@api.multi
	def test_create_budget_procedure(self):
		"""
		Test
		"""
		print()
		print('Test Create Budget procedure')
		test_treatment.test_create_budget_procedure(self)


	@api.multi
	def test_create_sale_procedure(self):
		"""
		Test
		"""
		print()
		print('Test Create Sale procedure')
		test_treatment.test_create_sale_procedure(self)


	@api.multi
	def test_create_procedure(self):
		"""
		Test
		"""
		print()
		print('Test Create procedure')
		test_treatment.test_create_procedure(self)

	@api.multi
	def test_create_sessions(self):
		"""
		Test
		"""
		print()
		print('Test Create sessions')
		test_treatment.test_create_sessions(self)

	@api.multi
	def test_create_controls(self):
		"""
		Test
		"""
		print()
		print('Test Create controls')
		test_treatment.test_create_controls(self)



# ----------------------------------------------------------- Test Integration ---------------------------------------------

# ----------------------------------------------------------- Test All --------------------------------
	# Test
	@api.multi
	#def test(self):
	def test_all(self):
		"""
		Test All
		"""
		print()
		print('Treatment - Test')
		if self.patient.x_test:
			self.test_reset()
			self.test_integration()
			#self.test_create_recos()
			#self.test_computes()
			#self.test_libs()


# ----------------------------------------------------------- Test Integration --------------------
	@api.multi
	def test_integration(self):
		"""
		Integration Test
		"""
		print()
		print('PL - Test Integration Button')
		if self.patient.x_test:
			# Reset
			#test_treatment.reset_treatment(self)
			# Test Integration
			test_treatment.test_integration_treatment(self)
		print()
		print()
		print('SUCCESS !')


# ----------------------------------------------------------- Test Reset --------------------------
	@api.multi
	def test_reset(self):
		"""
		Reset Test
		"""
		print()
		print('Test Reset Button')
		if self.patient.x_test:
			test_treatment.test_reset_treatment(self)
		print()
		print()
		print('SUCCESS !')

# ----------------------------------------------------------- Test Report MGT -----------------------------------------
	@api.multi
	def test_report_management(self):
		"""
		Test Report Management
		"""
		print()
		print('Test Report Management - Button')
		test_treatment.test_report_management(self)
		print()
		print()
		print('SUCCESS !')

# ----------------------------------------------------------- Test Report MKT -----------------------------------------
	@api.multi
	def test_report_marketing(self):
		"""
		Test Report Marketing
		"""
		print()
		print('Test Report Marketing - Button')
		test_treatment.test_report_marketing(self)
		print()
		print()
		print('SUCCESS !')

# ----------------------------------------------------------- Test Report ACC -----------------------------------------
	@api.multi
	def test_report_account(self):
		"""
		Test Report Accounting
		"""
		print()
		print('Test Report account - Button')
		test_treatment.test_report_account(self)
		print()
		print()
		print('SUCCESS !')

# ----------------------------------------------------------- Test Report ACC -----------------------------------------
	@api.multi
	def test_report_contasis(self):
		"""
		Test Report Accounting Contasis
		"""
		print()
		print('Test Report Contasis - Button')
		test_treatment.test_report_contasis(self)
		print()
		print()
		print('SUCCESS !')

# ----------------------------------------------------------- Test Report PROD -----------------------------------------
	@api.multi
	def test_report_product(self):
		"""
		Test Report Products
		"""
		print()
		print('Test Report Product - Button')
		test_treatment.test_report_product(self)
		print()
		print()
		print('SUCCESS !')


