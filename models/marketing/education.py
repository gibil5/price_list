# -*- coding: utf-8 -*-
"""
	Education - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Education(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.education'

	_description = 'Openhealth Marketing Education'

	#_order = 'date_create asc'




# ----------------------------------------------------------- Analyse -----------------------
	def update_per(self, repo):
		"""
		Patient Line Analysis to update counters
		"""
		print()
		print('X - Education - Update Per')




# ----------------------------------------------------------- Analyse -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		print()
		print('X - Education - analyse')


		# Education 
		if line.education == 'first': 
			self.first = self.first + 1

		elif line.education == 'second': 
			self.second = self.second + 1

		elif line.education == 'technical': 
			self.technical = self.technical + 1

		elif line.education == 'university': 
			self.university = self.university + 1

		elif line.education == 'masterphd': 
			self.master_phd = self.master_phd + 1

		else: 
			self.undefined = self.undefined + 1



# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		print()
		print('X - Education - Get Counters')

		return self.first, self.second, self.technical, self.university, self.master_phd, self.undefined






# ----------------------------------------------------------- Fields ---------------------------------------------
	first = fields.Integer(
			default=0,
		)

	second = fields.Integer(
			default=0,
		)

	technical = fields.Integer(
			default=0,
		)

	university = fields.Integer(
			default=0,
		)

	master_phd = fields.Integer(
			default=0,
		)

	undefined = fields.Integer(
			default=0,
		)





