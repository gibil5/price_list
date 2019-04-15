# -*- coding: utf-8 -*-
"""
		Service Excilite 

 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

class ServiceExcilite(models.Model):
	
	_inherit = 'openhealth.service.excilite'




# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),

						#('x_treatment', '=', 'laser_excilite'),
						('pl_treatment', '=', 'LASER EXCILITE'),

						('pl_price_list', '=', '2019'),
					],
	)
	
