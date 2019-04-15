# -*- coding: utf-8 -*-
"""
		Service promo 

		Created: 				15 Apr 2019
		Last: 					15 Apr 2019

"""
from openerp import models, fields, api

class ServicePromotion(models.Model):

	_name = 'price_list.service_promotion'
	
	_inherit = 'openhealth.service'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(

			'product.template',

			domain = [
						('type', '=', 'service'),

						('pl_family', '=', 'promotion'),

						('pl_price_list', '=', '2019'),
					],
	
	)
