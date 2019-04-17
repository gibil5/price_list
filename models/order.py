# -*- coding: utf-8 -*-
"""
	Order

	Created: 			26 Aug 2016
	Last mod: 			12 Apr 2019
"""
from __future__ import print_function

from openerp import models, fields, api

class sale_order(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'sale.order'

	_description = 'Order'




# ----------------------------------------------------- Product Selector --------------------------

	@api.multi
	def open_product_selector_product(self):
		"""
		high level support for doing this and that.
		"""
		print('o ps p')
		return self.open_product_selector('product')


	@api.multi
	def open_product_selector_service(self):
		"""
		high level support for doing this and that.
		"""
		print('o ps s')
		return self.open_product_selector('service')


	# Buttons  - Agregar Producto Servicio
	@api.multi
	def open_product_selector(self, x_type):
		"""
		high level support for doing this and that.
		"""
		print('o ps')


		# Init Vars
		order_id = self.id
		res_id = False


		return {
				'type': 'ir.actions.act_window',
				'name': ' New Orderline Selector Current',
				'view_type': 'form',
				'view_mode': 'form',
				#'target': 'current',
				'target': 'new',
				'res_id': res_id,


				#'res_model': 'openhealth.product.selector',
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
	# open_product_selector



