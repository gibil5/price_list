# -*- coding: utf-8 -*-
"""
		Service Medical treatment 

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
"""
from openerp import models, fields, api

from . import px_vars

class ServiceMedical(models.Model):

	_name = 'price_list.service_medical'

	_inherit = 'price_list.service'
	
	
# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_family', '=', 'medical'),
					],
	
	)

	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			required=True,
		)


# ---------------------------------------------- Fields - Categorized ---------
	
	family = fields.Selection(
			selection=px_vars._family_list,
			string='Family',
			required=True,
		)

	subfamily = fields.Selection(
			selection=px_vars._subfamily_list,
			string='Subfamily',
			required=True,
		)




	zone = fields.Selection(
			selection=px_vars._zone_list,
			string='Zone',
			required=True,
		)

	pathology = fields.Selection(
			selection=px_vars._pathology_list,
			string='Pathology',
			required=True,
		)



	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)

	sessions = fields.Selection(
			selection=px_vars._sessions_list,
			string='Sessions',
			required=True,
		)

	time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			required=False,
		)



# ---------------------------------------------- Fields - Floats -----------------------

	price = fields.Float(
			'Price',
		)

	price_vip = fields.Float(
			'Price vip',
		)

	price_company = fields.Float(
			'Price company',
		)



	price_session = fields.Float(
			'Price session',
		)

	price_session_next = fields.Float(
			'Price session next',
		)

	price_max = fields.Float(
			'Price max',
		)


