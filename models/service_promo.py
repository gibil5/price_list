# -*- coding: utf-8 -*-
"""
		Service promo 

		Created: 				15 Apr 2019
		Last: 					15 Apr 2019

"""
from openerp import models, fields, api

from . import px_vars

from . import px_vars_promo

class ServicePromotion(models.Model):

	_name = 'price_list.service_promotion'
	
	_inherit = 'price_list.service'
	
	

# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_family', '=', 'promotion'),
					],
	
	)


# ----------------------------------------------------------- Modified ------------------------------

	pl_treatment = fields.Selection(

			#selection=pl_px_vars._treatment_list,
			selection=px_vars_promo._treatment_list,
		
			string='Treatment',
			required=True,
		)



	#sessions = fields.Selection(

	#		selection=px_vars._sessions_list,
			#selection=px_vars_gyn._sessions_list,
		
	#		string='Sessions',
	#		required=False,
	#	)




	level = fields.Selection(

			selection=px_vars._level_list,
			#selection=px_vars_gyn._level_list,

			string='Level',
			required=False,
		)

	time = fields.Selection(

			selection=px_vars._time_list,
			#selection=px_vars_gyn._time_list,

			string='Time',
			required=False,
		)


