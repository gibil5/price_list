# -*- coding: utf-8 -*-
"""
		Service Quick 
 	
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

from . import px_vars
from . import px_vars_ext

class ServiceQuick(models.Model):

	_name = 'price_list.service_quick'

	_inherit = 'price_list.service'





# ----------------------------------------------------------- Select ------------------------------

	sel_zone = fields.Selection(

			selection=px_vars_ext._zone_list_qui,

			string='Seleccionar Zona',
			required=True,
		)


	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):

		if self.sel_zone != False: 

			pl_treatment = 'QUICKLASER'
			
			return {	'domain': {	'service': [														
														('pl_treatment', '=', pl_treatment),		
														('pl_zone', '=', self.sel_zone),
														('pl_price_list', '=', '2019'),
													], 
									},
					}






	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_qui,
			string='Treatment',
			required=True,
		)




# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_treatment', '=', 'QUICKLASER'),
					],
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

	sessions = fields.Selection(
			selection=px_vars._sessions_list,
			string='Sessions',
			required=True,
		)



	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
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
