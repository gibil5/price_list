# -*- coding: utf-8 -*-
"""
	Sale Order Line
	
	Created:            26 Aug 2016
	Last mod:            9 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api
				
class SaleOrderLine(models.Model):
	""" 
	Sale Order Line
	""" 
	_inherit = 'sale.order.line'



# ----------------------------------------------------------- Print Ticket -------------------------------

	def get_quantity(self):
		"""
		Used by Print Ticket.
		"""
		return int(self.product_uom_qty)



# ----------------------------------------------------------- Product ----------
	product_id = fields.Many2one(
		'product.product',
		string='Product',

		
		#domain=[('sale_ok', '=', True)],
		domain=[
					('sale_ok', '=', True),
					('pl_price_list', '=', '2019'),
				],


		change_default=True,
		ondelete='restrict',
		required=True
		)

