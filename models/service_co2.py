# -*- coding: utf-8 -*-
"""
 		Service Co2 

 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

class ServiceCo2(models.Model):

	_inherit = 'openhealth.service.co2'




# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),

						#('x_treatment', '=', 'laser_co2'),
						('pl_treatment', '=', 'LASER CO2 FRACCIONAL'),

						('pl_price_list', '=', '2019'),
					],
		)