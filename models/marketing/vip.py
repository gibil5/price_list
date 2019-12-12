# -*- coding: utf-8 -*-
"""
	Vip - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Vip(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.vip'

	_description = 'Openhealth Marketing Vip'

	#_order = 'date_create asc'


# ----------------------------------------------------------- Analyse -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		print()
		print('X - Vip - analyse')

		# Vip 
		if line.vip: 
			#self.vip_true = self.vip_true + 1
			#self.vip_already_true = self.vip_already_true + 1
			self.vip_already = self.vip_already + 1

		else: 
			#self.vip_false = self.vip_false + 1
			#self.vip_already_false = self.vip_already_false + 1
			self.not_vip_already = self.not_vip_already + 1



# ----------------------------------------------------------- Fields ---------------------------------------------

	vip = fields.Integer(
			default=0,
		)

	not_vip = fields.Integer(
			default=0,
		)


	vip_already = fields.Integer(
			default=0,
		)

	not_vip_already = fields.Integer(
			default=0,
		)



