# -*- coding: utf-8 -*-
"""
		Service Cosmetology
		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
"""
from openerp import models, fields, api
from . import px_vars
from . import px_vars_ext

class ServiceCosmetology(models.Model):

	_name = 'price_list.service_cosmetology'

	_inherit = 'price_list.service'



# ---------------------------------------------- Pl Treatment -------------------------------------
	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			required=True,
		)



# ----------------------------------------------------------- Select ------------------------------

	sel_zone = fields.Selection(

			selection=px_vars_ext._zone_list_cos,

			string='Seleccionar Zona',
			#required=True,
		)


	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):
		if self.sel_zone != False: 

			pl_family = 'cosmetology'
			
			return {'domain': {'service': [														
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),		
												('pl_zone', '=', self.sel_zone),
			],},}







# ----------------------------------------------------------- Natives ------------------------------

	# Service
	service = fields.Many2one(
			'product.template',

			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_family', '=', 'cosmetology'),
					],
		)



# ----------------------------------------------------------- Categorized -------------------------

	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',

			required=False,
		)
