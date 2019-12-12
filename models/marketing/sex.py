# -*- coding: utf-8 -*-
"""
	Sex - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Sex(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.sex'

	_description = 'Openhealth Marketing Sex'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Analyse -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		print()
		print('X - Sex - analyse')

		# Sex
		if line.sex == 'Male': 
			self.male = self.male + 1

		elif line.sex == 'Female': 
			self.female = self.female + 1

		else: 
			self.undefined = self.undefined + 1



# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		print()
		print('X - Sex - Get Counters')

		return self.male, self.female, self.undefined




# ----------------------------------------------------------- Fields ---------------------------------------------

	male = fields.Integer(
			default=0,
		)

	female = fields.Integer(
			default=0,
		)

	undefined = fields.Integer(
			default=0,
		)


