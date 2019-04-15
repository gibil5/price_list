# -*- coding: utf-8 -*-
"""
		Service - 2019

		Created: 				20 Sep 2016
		Last updated: 	 		15 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api
#from . import prodvars
#from . import ipl

from . import pl_vars

class Service(models.Model):
	"""
	Price list aware
	"""
	_inherit = 'openhealth.service'




# ----------------------------------------------------------- Natives ------------------------------
	# Service - Pricelist 2019
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
					],
			string="Producto",
			required=True,
		)






# ---------------------------------------------- Fields - Categorized ---------
	
	pl_price_list = fields.Selection(
			selection=pl_vars._price_list_list,
			string='Price list',
			default='2019',
			#required=True,
		)




	#pl_manufacturer = fields.Selection(
	#		selection=pl_vars._manufacturer_list,
	#		string='Manufacturer',
	#	)

	#pl_brand = fields.Selection(
	#		selection=pl_vars._brand_list,
	#		string='brand',
	#	)




	pl_family = fields.Selection(
			selection=pl_vars._family_list,
			string='Family',
			required=True,
		)

	pl_subfamily = fields.Selection(
			selection=pl_vars._subfamily_list,
			string='Subfamily',
			required=True,
		)

	pl_treatment = fields.Selection(
			selection=pl_vars._treatment_list,
			string='Treatment',
			required=True,
		)

	pl_zone = fields.Selection(
			selection=pl_vars._zone_list,
			string='Zone',
			required=True,
		)

	pl_pathology = fields.Selection(
			selection=pl_vars._pathology_list,
			string='Pathology',
			required=True,
		)

	pl_level = fields.Selection(
			selection=pl_vars._level_list,
			string='Level',
			required=True,
		)

	pl_sessions = fields.Selection(
			selection=pl_vars._sessions_list,
			string='Sessions',
			required=True,
		)

	pl_time = fields.Selection(
			selection=pl_vars._time_list,
			string='Time',
			required=True,
		)



# ---------------------------------------------- Fields - Floats -----------------------

	pl_price = fields.Float(
			'Price',
		)

	pl_price_vip = fields.Float(
			'Price vip',
		)

	pl_price_company = fields.Float(
			'Price company',
		)

	pl_price_session = fields.Float(
			'Price session',
		)

	pl_price_session_next = fields.Float(
			'Price session next',
		)

	pl_price_max = fields.Float(
			'Price max',
		)

