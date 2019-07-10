# -*- coding: utf-8 -*-
"""
 		Service Co2 
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api

#from . import px_vars
from openerp.addons.price_list.models.product import px_vars

from . import px_vars_ext

class ServiceCo2(models.Model):

	_name = 'price_list.service_co2'

	_inherit = 'price_list.service'



# ---------------------------------------------- Pl Treatment -------------------------------------
	pl_treatment = fields.Selection(

			selection=px_vars_ext._treatment_list_co2,
		
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select ------------------------------

	sel_zone = fields.Selection(

			selection=px_vars_ext._zone_list_co2,

			string='Seleccionar Zona',
			required=True,
		)


	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):
		if self.sel_zone != False: 

			pl_treatment = 'LASER CO2 FRACCIONAL'
			
			return {'domain': {'service': [														
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),		
												('pl_zone', '=', self.sel_zone),
			],},}







# ----------------------------------------------------------- Relational ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'LASER CO2 FRACCIONAL'),
					],
		)


# ----------------------------------------------------------- Categorized -------------------------

	time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			required=False,
		)
