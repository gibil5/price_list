# -*- coding: utf-8 -*-
"""
	Order Report Nex - Estado de Cuenta 

	Created: 				14 Nov 2017
	Last updated: 	 		30 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class order_report_nex(models.Model):
	"""
	Estado de Cuenta
	Used by Patient
	"""
	_inherit = 'openhealth.order.report.nex'

	_description = "Openhealth Order Report Nex"



# ----------------------------------------------------------- Clean ------------------------------

	@api.multi 
	def clean(self):
		"""
		Clean
		"""
		print()
		print('PL - Clean')

		# Search
		lines = self.env['openhealth.report.order_line'].search([
																	('order_report_nex_id', '=', self.id),
														],
															#order='date_begin asc',
															#limit=10,
													)
		#print(lines)
		lines.unlink()


