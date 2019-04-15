# -*- coding: utf-8 -*-
"""

 	Electronic Order - Sunat compatible

 	Created: 			15 Apr 2019
 	Last updated: 		15 Apr 2019

"""
from openerp import models, fields, api

from . import lib_coeffs

class electronic_order(models.Model):
	"""
	high level support for doing this and that.
	"""
	#_inherit = 'openhealth.line'
	#_name = 'openhealth.electronic.order'
	#_description = "Sunat Electronic Order"
	#_order = 'serial_nr asc'


	_inherit = 'openhealth.electronic.order'




# ----------------------------------------------------------- Electronic -------------------------------

	def get_coeff(self):
		"""
		Used by Txt Generation
		From containers.lib_exp
		"""
		coeff = lib_coeffs.get_coeff(self.state)
		return coeff

