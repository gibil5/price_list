# -*- coding: utf-8 -*-
"""

 	Electronic Order - Sunat compatible

 	Created: 			15 Apr 2019
 	Last updated: 		30 Apr 2019

"""
from openerp import models, fields, api
from . import lib_coeffs

class electronic_order(models.Model):
	"""
	high level support for doing this and that.
	"""

	_inherit = 'openhealth.electronic.order'




# ----------------------------------------------------------- Required ----------------------------

	# Patient
	id_doc_type = fields.Char(
			string='Doc Id Tipo',
			default=".",
			required=True,
		)

	id_doc_type_code = fields.Char(
			string='Codigo',
			default=".",
			required=True,
		)



	# Order
	x_type = fields.Char(
			'Tipo',
			required=True,
		)

	type_code = fields.Char(
			'Codigo',
			required=True,
		)

	serial_nr = fields.Char(
			'Serial Nr',
			required=True,
		)

	receptor = fields.Char(
			string='Receptor',
			required=True,
		)

# ----------------------------------------------------------- Electronic -------------------------------

	def get_coeff(self):
		"""
		Used by Txt Generation
		From containers.lib_exp
		"""
		print()
		print('Pl - Get Coeff')

		coeff = lib_coeffs.get_coeff(self.state)

		return coeff

