# -*- coding: utf-8 -*-
"""
		Service Ipl 

 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019

"""
from openerp import models, fields, api

class ServiceIpl(models.Model):
	
	_inherit = 'openhealth.service.ipl'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),

						#('x_treatment', '=', 'laser_ipl'),
						('pl_treatment', '=', 'LASER M22 IPL'),

						('pl_price_list', '=', '2019'),
					],
	)

