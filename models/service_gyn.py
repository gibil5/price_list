# -*- coding: utf-8 -*-
"""
		Service Gyn 

		Created: 				15 Apr 2019
		Last: 					15 Apr 2019

"""
from openerp import models, fields, api

#from . import pl_px_vars

from . import px_vars_gyn

class ServiceGynecology(models.Model):

	_name = 'price_list.service_gynecology'
	
	_inherit = 'price_list.service'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_family', '=', 'gynecology'),
					],
	)





# ----------------------------------------------------------- Modified ------------------------------

	pl_treatment = fields.Selection(

			#selection=pl_px_vars._treatment_list,
			selection=px_vars_gyn._treatment_list,
		
			string='Treatment',
			required=True,
		)




	zone = fields.Selection(

			#selection=px_px_vars._zone_list,
			selection=px_vars_gyn._zone_list,
		
			string='Zone',
			required=True,
		)

	pathology = fields.Selection(

			#selection=px_px_vars._pathology_list,
			selection=px_vars_gyn._pathology_list,

			string='Pathology',
			required=True,
		)

	sessions = fields.Selection(

			#selection=px_px_vars._sessions_list,
			selection=px_vars_gyn._sessions_list,
		
			string='Sessions',
			required=False,
		)




	level = fields.Selection(

			#selection=px_px_vars._level_list,
			selection=px_vars_gyn._level_list,

			string='Level',
			required=False,
		)

	time = fields.Selection(

			#selection=px_px_vars._time_list,
			selection=px_vars_gyn._time_list,

			string='Time',
			required=False,
		)




