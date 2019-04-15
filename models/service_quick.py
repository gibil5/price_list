# -*- coding: utf-8 -*-
"""
		Service Quick 
 	
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

class ServiceQuick(models.Model):

	_inherit = 'openhealth.service.quick'




# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			#default = 'QUICKLASER - Cuello - Rejuvenecimiento Cuello - 1',
			domain = [
						('type', '=', 'service'),
						
						#('x_treatment', '=', 'laser_quick'),
						('pl_treatment', '=', 'QUICKLASER'),

						('pl_price_list', '=', '2019'),
					],
	)



