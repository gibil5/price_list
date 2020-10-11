# -*- coding: utf-8 -*-
"""
		Service Excilite
 		Created: 				15 Apr 2019
	    Last mod: 			28 Jul 2020
"""
from openerp import models, fields, api
from openerp.addons.price_list.models.product import px_vars
from . import px_vars_ext

class ServiceExcilite(models.Model):
	_name = 'price_list.service_excilite'
	_inherit = 'price_list.service'

# ---------------------------------------------- Pl Treatment -------------------------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_exc,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select ------------------------------

	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_exc_ipl,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone 
	@api.onchange('sel_zone')	
	def _onchange_sel_zone(self):
		if self.sel_zone != False: 
			pl_treatment = 'LASER EXCILITE'
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
						('pl_treatment', '=', 'LASER EXCILITE'),
					],
	)
	
# ----------------------------------------------------------- Categorized -------------------------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)
