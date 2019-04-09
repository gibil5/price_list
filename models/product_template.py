# -*- coding: utf-8 -*-
"""
		*** Product Template

		Created: 			  8 Apr 2019
		Last up: 	 		  8 Apr 2019
"""
from __future__ import print_function

from openerp import models, fields, api

from . import pl_vars

class ProductTemplate(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'product.template'

	_order = 'name'

	_description = 'Product Template'




# ---------------------------------------------- Fields - Chars -----------------------

	pl_name_short = fields.Char(
			'Name short',
			required=True,
		)

	pl_prefix = fields.Char(
			'Prefix',
			required=True,
		)

	pl_idx = fields.Char(
			'Idx',
			required=True,
		)

	pl_code = fields.Char(
			'Code',
			#required=True,
		)




# ---------------------------------------------- Fields - Categorized ---------
	
	pl_price_list = fields.Selection(

			selection=pl_vars._price_list_list,
		
			string='Price list',
			#required=True,
		)


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


