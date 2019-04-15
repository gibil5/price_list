# -*- coding: utf-8 -*-
"""
		Service Medical treatment 

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018

"""
from openerp import models, fields, api

class ServiceMedical(models.Model):

	_inherit = 'openhealth.service.medical'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),

						#('x_family', '=', 'medical'),
						('pl_family', '=', 'medical'),

						('pl_price_list', '=', '2019'),
					],
	
	)
