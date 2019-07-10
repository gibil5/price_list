# -*- coding: utf-8 -*-
"""
		Service echo
		Created: 				15 Apr 2019
		Last: 					15 Apr 2019

"""
from openerp import models, fields, api
#from . import px_vars
from openerp.addons.price_list.models.product import px_vars
from . import px_vars_echo
from . import px_vars_ext

class ServiceEchography(models.Model):

	_name = 'price_list.service_echography'
	
	_inherit = 'price_list.service'
	
# ---------------------------------------------- Pl Treatment -------------------------------------
	pl_treatment = fields.Selection(

			#selection=pl_px_vars._treatment_list,
			selection=px_vars_echo._treatment_list,
		
			string='Treatment',
			required=True,
		)


# ----------------------------------------------------------- Select ------------------------------

	sel_zone = fields.Selection(

			selection=px_vars_ext._zone_list_echo,

			string='Seleccionar Zona',
			required=True,
		)


	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):
		if self.sel_zone != False: 

			pl_family = 'echography'
			
			return {'domain': {'service': [														
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),		
												('pl_zone', '=', self.sel_zone),
			],},}


	

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






	zone = fields.Selection(

			#selection=px_vars._zone_list,
			selection=px_vars_echo._zone_list,
		
			string='Zone',
			required=False,
		)

	pathology = fields.Selection(

			#selection=px_vars._pathology_list,
			selection=px_vars_echo._pathology_list,

			string='Pathology',
			required=False,
		)



	sessions = fields.Selection(

			#selection=px_vars._sessions_list,
			selection=px_vars_echo._sessions_list,
		
			string='Sessions',
			required=True,
		)




	level = fields.Selection(

			#selection=px_vars._level_list,
			selection=px_vars_echo._level_list,

			string='Level',
			required=False,
		)

	time = fields.Selection(

			#selection=px_vars._time_list,
			selection=px_vars_echo._time_list,

			string='Time',
			required=False,
		)
