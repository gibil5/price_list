# -*- coding: utf-8 -*-
"""
		*** Treatment - DEP !!!

		Created: 			26 Aug 2016
		Last up: 	 		27 Jul 2020
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

# ----------------------------------------------------- Create Orders ---------------------------------------------

# ----------------------------------------------------- Create Services ---------------------------------------------


# ----------------------------------------------------------- Actions - Serivces --------------------------
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

