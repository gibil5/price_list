# -*- coding: utf-8 -*-
"""
		Service Cosmetology

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
"""
from openerp import models, fields, api

class ServiceCosmetology(models.Model):

	_inherit = 'openhealth.service.cosmetology'


# ----------------------------------------------------------- Natives ------------------------------

	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						#('x_family', '=', 'cosmetology'),
						('pl_family', '=', 'cosmetology'),
						('pl_price_list', '=', '2019'),
					],
		)

