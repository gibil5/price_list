# -*- coding: utf-8 -*-
"""
		Service Ndyag
 		Created: 				15 Apr 2019
 		Last updated: 	 		15 Apr 2019
"""
from openerp import models, fields, api
from openerp.addons.price_list.models.product import px_vars
from . import px_vars_ext

class ServiceNdyag(models.Model):
	_name = 'price_list.service_ndyag'
	_inherit = 'price_list.service'
	
# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_ndy,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_ndy,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):
		if self.sel_zone != False: 
			pl_treatment = 'LASER M22 ND YAG'			
			return {'domain': {'service': [														
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),		
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Relational -------
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'LASER M22 ND YAG'),
					],
	)

# ----------------------------------------------------------- Categorized ------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)
