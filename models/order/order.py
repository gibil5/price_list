# -*- coding: utf-8 -*-
"""
		Order - Pricelist - DEP !
		Created: 			26 Aug 2016
		Last mod: 			27 Jul 2020
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
