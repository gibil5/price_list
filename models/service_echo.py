# -*- coding: utf-8 -*-
"""
		Service echo 

		Created: 				15 Apr 2019
		Last: 					15 Apr 2019

"""
from openerp import models, fields, api

class ServiceEchography(models.Model):

	_name = 'price_list.service_echography'
	
	_inherit = 'openhealth.service'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(

			'product.template',

			domain = [
						('type', '=', 'service'),

						('pl_family', '=', 'echography'),

						('pl_price_list', '=', '2019'),
					],
	
	)
