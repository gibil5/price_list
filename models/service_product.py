# -*- coding: utf-8 -*-
"""
 		Service Product - 2019
 
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

class ServiceProduct(models.Model):

	_inherit = 'openhealth.service.product'

	


# ----------------------------------------------------------- Natives ------------------------------
	# Service - Pricelist 2019
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'product'),

						('pl_price_list', '=', '2019'),
					],
			string="Servicio",
			required=True, 
		)


