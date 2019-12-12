# -*- coding: utf-8 -*-
"""
	Origin - Object Oriented
	
	For Marketing

	Created: 				12 Dec 2019
	Last up: 				12 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Origin(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.origin'

	_description = 'Openhealth Marketing Origin'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Line Analysis -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		print()
		print('X - Origin - analyse')


		# Origin






# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		print()
		print('X - Origin - Get Counters')






# ----------------------------------------------------------- Fields ---------------------------------------------

