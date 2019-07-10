# -*- coding: utf-8 -*-
"""
		Service Medical treatment
		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
"""
from openerp import models, fields, api

#from . import px_vars
from openerp.addons.price_list.models.product import px_vars

from . import px_vars_ext

class ServiceMedical(models.Model):
	_name = 'price_list.service_medical'

	_inherit = 'price_list.service'
	


# ---------------------------------------------- Pl Treatment -------------------------------------
	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			required=True,
		)



# ----------------------------------------------------------- Select ------------------------------

	sel_zone = fields.Selection(

			selection=px_vars_ext._zone_list_med,

			string='Seleccionar Zona',
			required=True,
		)


	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):
		if self.sel_zone != False: 

			pl_family = 'medical'
			
			return {'domain': {'service': [														
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),		
												('pl_zone', '=', self.sel_zone),
			],},}





# ----------------------------------------------------------- Relational --------------------------
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_family', '=', 'medical'),
					],
	)

# ----------------------------------------------------------- Categorized -------------------------
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
