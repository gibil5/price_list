# -*- coding: utf-8 -*-
"""
 		Service Product - 2019
 
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

#from . import pl_vars
#from . import pl_vars_prod

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
					],
			string="Servicio",
			required=True, 
		)



