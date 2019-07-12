# -*- coding: utf-8 -*-
"""
 		Service Product - 2019
 
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

class ServiceProduct(models.Model):

	_name = 'price_list.service_product'

	_inherit = 'price_list.service'

	

# ----------------------------------------------------------- Natives ------------------------------

	# Service - Pricelist 2019
	service = fields.Many2one(
			
			'product.template',
			#'product.product',

			domain = [
						('type', '=', 'product'),

						('pl_price_list', '=', '2019'),
						#('pl_price_list', 'in', ['2019', '2018']),
						#('pl_price_list', '=', '2018'),
					],
			string="Servicio",
			required=True, 
		)



