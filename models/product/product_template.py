# -*- coding: utf-8 -*-
"""
	*** Product Template - 2019

	Only functions. Not the data model. 

	Created: 			  8 Apr 2019
	Last up: 	 		 10 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import px_vars
from . import chk_product
from . import pl_prod_vars
from . import exc_prod

class ProductTemplate(models.Model):
	"""
	Product Template - 2019
	"""
	_inherit = 'product.template'

	_order = 'pl_idx_int'

	_description = 'Product Template'



# ----------------------------------------------------------- Configurator ------------------------
	def init_configurator(self):
		"""
		Initializes the Configurator
		Is compatible with Tacna. Does the search by type, not by name
		"""
		# Search
		if self.configurator.name in [False]:
			self.configurator = self.env['openhealth.configurator.emr'].search([
																					('x_type', 'in', ['emr']),
															],
															#order='date_begin,name asc',
															limit=1,
														)
	# Configurator - Used by Product Template Tree
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
		)





# ---------------------------------------- Constraints Python - Name -------------------------

	# Check Name
	@api.constrains('name')
	def check_name(self):
		"""
		Check Name
		"""
		chk_product.check_name(self)


# ----------------------------------------------------------- Fields ------------------------

	pl_price_list = fields.Selection(
			[
				('2019', '2019'),
				('2018', '2018'),
			],
			string='Lista de Precios',
			required=True,
		)




# ----------------------------------------------------------- Natives ----------------------------------------------------
	# Treatment
	x_treatment = fields.Selection(

			#selection=prodvars._treatment_list,
			selection=pl_prod_vars._treatment_list,
		
			required=False,
		)




# ---------------------------------------------- Fields - Categorized -----------------------------
	# Required
	pl_family = fields.Selection(

			selection=px_vars._family_list,
		
			string='Family',
			required=True,
		)

	pl_subfamily = fields.Selection(

			selection=px_vars._subfamily_list,
		
			string='Subfamily',
			required=True,
		)


	# Not Required
	pl_manufacturer = fields.Selection(
			selection=px_vars._manufacturer_list,
			string='Fabricante',
		)

	pl_brand = fields.Selection(
			selection=px_vars._brand_list,
			string='Marca',
		)


	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			#required=True,
		)

	pl_zone = fields.Selection(
			selection=px_vars._zone_list,
			string='Zone',
			#required=True,
		)

	pl_pathology = fields.Selection(
			selection=px_vars._pathology_list,
			string='Pathology',
			#required=True,
		)

	pl_level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			#required=True,
		)

	pl_sessions = fields.Selection(
			selection=px_vars._sessions_list,
			string='Sessions',
			#required=True,
		)

	pl_time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			#required=True,
		)

# ---------------------------------------------- Fields - Floats ----------------------------------

	pl_price = fields.Float(
			'Price',
		)

	pl_price_vip = fields.Float(
			'Precio Vip',
		)

	pl_price_company = fields.Float(
			'Precio Empresa',
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

# ---------------------------------------------- Fields - Chars -----------------------------------

	pl_name_short = fields.Char(
			'Name short',
			required=True,
		)

	pl_prefix = fields.Char(
			'Prefix',
			#required=True,
		)

	pl_idx = fields.Char(
			'Idx',
			#required=True,
		)

	pl_code = fields.Char(
			'Code',
			#required=True,
		)

	pl_idx_int = fields.Integer(
			#'Idx I',
			'Indice',
			#required=True,
		)

	pl_account = fields.Char(
			'Cuenta contable',
			required=False,
		)

	pl_time_stamp = fields.Char(
			required=False,
		)


