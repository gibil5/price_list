# -*- coding: utf-8 -*-
"""
		Service Ndyag 

 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

class ServiceNdyag(models.Model):
	
	_inherit = 'openhealth.service.ndyag'
	
	


# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),

						#('x_treatment', '=', 'laser_ndyag'),
						('pl_treatment', '=', 'LASER M22 ND YAG'),

						('pl_price_list', '=', '2019'),
					],
	)




