# -*- coding: utf-8 -*-
"""
	Pricelist Marketing Order Line 

	Created: 			26 Jun 2019
	Last updated: 		26 Jun 2019
"""
from openerp import models, fields, api

class MarketingOrderLine(models.Model):

	_name = 'price_list.marketing.order_line'

	_description = "PriceList Marketing Order Line"

	_order = 'date desc'



# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Marketing Id
	marketing_id = fields.Many2one(			
			'openhealth.marketing',
			ondelete='cascade', 			
		)



# ----------------------------------------------------------- Natives ------------------------------------------------------
	order = fields.Many2one(
			'sale.order',
			ondelete='cascade',
		)


	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente',
			ondelete='cascade',
		)


	product_id = fields.Many2one(
			'product.product',
			ondelete='cascade',			
		)


	date = fields.Datetime(
		)


	product_uom_qty = fields.Float(
		)

	price_unit = fields.Float(
		)

	price_net = fields.Float(
		)



	family = fields.Char(
		)

	subfamily = fields.Char(
		)

	subsubfamily = fields.Char(
		)



	price_list = fields.Char(
		)

	state = fields.Char(
		)

