# -*- coding: utf-8 -*-
"""
	Sale Order Line
	
	Created:            26 Aug 2016
	Last mod:            9 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from . import px_vars

from . import chk_order_line
				
class SaleOrderLine(models.Model):
	""" 
	Sale Order Line
	""" 
	_inherit = 'sale.order.line'




# ---------------------------------------- Constraints Python - Important -------------------------

	# Check Price List
	@api.constrains('pl_price_list')
	def check_pl_price_list(self):
		"""
		Check Pl Price List
		"""
		chk_order_line.check_pl_price_list(self)





# ---------------------------------------------- Fields - Categorized -----------------------------
	
	pl_price_list = fields.Selection(
			selection=px_vars._price_list_list,
			string='Lista de Precios',

			compute='_compute_pl_price_list',
		)

	@api.multi
	#@api.depends('state')
	def _compute_pl_price_list(self):
		"""
		high level support for doing this and that.
		"""
		for record in self:

			record.pl_price_list = record.product_id.pl_price_list






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

