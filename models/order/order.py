# -*- coding: utf-8 -*-
"""
		*** Order

		order.py

		Created: 			26 Aug 2016
		Last updated: 		29 Aug 2019
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError
from . import exc_ord

class sale_order(models.Model):
	"""
	Inherits Sale Classe from Openhealth
	Encapsulates Business Rules. Should not extend the Data Model.
	Should only have functions.
	"""
	_inherit = 'sale.order'



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
