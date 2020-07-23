# -*- coding: utf-8 -*-
"""
		Order - Pricelist

		Created: 			26 Aug 2016
		Last mod: 			23 Jul 2020
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError
from . import exc_ord
from openerp.addons.openhealth.models.order import ord_funcs

class sale_order(models.Model):
	"""
	# Dep - Encapsulates Business Rules. Should not extend the Data Model.
	This should disappear. Order must be in Openhealth, not in Pricelist.
	Testing must be into TestOrder.
	Tools must into ToolsOrder.
	"""
	_inherit = 'sale.order'

# ----------------------------------------------------- Test --------------------------
	@api.multi
	def test(self):
		"""
		Unit Testing - All
		"""
		print()
		print('Test Order')

		tester = TestOrder(self)

		tester.test_raw_receipt(self)
		tester.test_raw_invoice(self)
		tester.test_raw_credit_note(self)
		tester.test_serial_number(self)

		#action0 = self.test_raw_receipt()
		#return action0
		#action1 = self.test_raw_invoice()
		#return action1
		#action2 = self.test_raw_credit_note()
		#return action2
		#self.test_serial_number()
		#return action0, action1, action2


# ----------------------------------------------------- Django Interface --------------------------

	@api.multi
	def get_name(self):
		"""
		Django interface
		"""
		print()
		print('Get name')
		return self.name

	@api.multi
	def get_date(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_order

	@api.multi
	def get_state(self):
		"""
		Django interface
		"""
		print()
		print('Get state')
		return self.state

	@api.multi
	def get_total(self):
		"""
		Django interface
		"""
		print()
		print('Get total')
		return self.amount_total

	@api.multi
	def get_patient(self):
		"""
		Django interface
		"""
		print()
		print('Get patient')
		return self.patient.name

	@api.multi
	def get_type(self):
		"""
		Django interface
		"""
		print()
		print('Get type')
		return self.x_type

	@api.multi
	def get_serial_number(self):
		"""
		Django interface
		"""
		print()
		print('Get serial_number')
		return self.x_serial_nr


# ----------------------------------------------------- Admin --------------------------
	@api.multi
	def correct_serial_number(self):
		"""
		Correct Serial Number
		"""
		print()
		print('Correct Serial Number')

		self.x_serial_nr = ord_funcs.get_serial_nr(self.x_type, self.x_counter_value, self.state)


# ----------------------------------------------------- Fixers --------------------------

	@api.multi
	def fix_treatment(self):
		"""
		Fix Treatment
		"""
		print()
		print('Fix Treatment')

		# Treatment
		self.treatment = self.env['openhealth.treatment'].search([
																	('patient', '=', self.patient.id),
																	('physician', '=', self.x_doctor.id),
											],
												order='start_date desc',
												limit=1,
											)
		#print(self.treatment.name)


	@api.multi
	def fix_treatment_month(self):
		"""
		Fix Treatment Month
		"""
		print()
		print('Fix Treatment Month')


	@api.multi
	def fix_treatment_all(self):
		"""
		Fix Treatment All
		"""
		print()
		print('Fix Treatment All')


# ----------------------------------------------------------- Setters ----------------------------

	def set_procedure_created(self, value):
		"""
		Set Procedure Created
		Used by: Treatment and Order
		"""
		self.x_procedure_created = value


	def is_procedure_created(self):
		"""
		Used by: Treatment
		"""
		return self.x_procedure_created



# ----------------------------------------------------------- Validate Patient ----------------------------
	#@api.multi
	def validate_patient_for_invoice(self):
		"""
		Validate Patient
		Used by Electronic Container (Txt Generation).
		"""
		print()
		print('Order Validate Patient For Invoice')
		#self.patient.validate()
		self.patient.validate_for_invoice()


# ----------------------------------------------------------- Validate Electronic ----------------------------
	@api.multi
	def validate_electronic(self):
		"""
		Validate Electronic
		Used by Electronic Container (Txt Generation).
		"""
		#print()
		#print('Order Validate Electronic')

		# Handle Exceptions
		exc_ord.handle_exceptions_electronic(self)

	# validate_electronic


# ----------------------------------------------------- Product Selector 2019 --------------------------

	@api.multi
	def pl_open_product_selector_product(self):
		"""
		Open Product Selector Product - 2019
		"""
		return self.pl_open_product_selector('product')


	@api.multi
	def pl_open_product_selector_service(self):
		"""
		Open Product Selector Service - 2019
		"""
		return self.pl_open_product_selector('service')


	# Buttons  - Agregar Producto Servicio
	@api.multi
	def pl_open_product_selector(self, x_type):
		"""
		high level support for doing this and that.
		"""

		# Init
		order_id = self.id
		res_id = False

		# Open
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Orderline Selector Current',
				'view_type': 'form',
				'view_mode': 'form',
				#'target': 'current',
				'target': 'new',
				'res_id': res_id,
				'res_model': 'price_list.product.selector',
				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
								'form':{'action_buttons': False, 'options': {'mode': 'edit'}}
							},
				'context': {
								'default_order_id': order_id,
								'default_x_type': x_type,
					}}

	# pl_open_product_selector


# ----------------------------------------------------------- Clean ----------------------------
	@api.multi
	def clean_order_lines(self):
		"""
		Clean Order Lines
		"""
		for line in self.order_line:
			if self.x_admin_mode:
				line.state = 'draft'
				line.unlink()
