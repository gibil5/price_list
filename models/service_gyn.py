# -*- coding: utf-8 -*-
"""
		Service Gyn 

		Created: 				15 Apr 2019
		Last: 					15 Apr 2019

"""
from openerp import models, fields, api

class ServiceGynecology(models.Model):

	_name = 'price_list.service_gynecology'
	
	_inherit = 'openhealth.service'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(

			'product.template',

			domain = [
						('type', '=', 'service'),

						('pl_family', '=', 'gynecology'),

						('pl_price_list', '=', '2019'),
					],
	
	)
