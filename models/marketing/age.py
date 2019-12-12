# -*- coding: utf-8 -*-
"""
	Age - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Age(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.age'

	_description = 'Openhealth Marketing Age'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Update Stats ---------------------------------------------
	def update_stats(self, mkt):
		"""
		Update Age
		Extract BL from Structure
		"""
		#print()
		#print('X - Update Age')

		if mkt.total_count != 0:
			mkt.age_mean = mkt.age_sum / float(mkt.total_count)
			mkt.age_undefined_per = (mkt.age_undefined / float(mkt.total_count))





# ----------------------------------------------------------- Analyse -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		#print()
		#print('X - Age - analyse')


		# Age Max and Min 
		if line.age_years >= 0:
			self.age_sum = self.age_sum + line.age_years 

			if line.age_years > self.age_max: 
				self.age_max = line.age_years

			if self.age_min in [0]:
				self.age_min = line.age_years

			else:			
				if line.age_years < self.age_min: 
					self.age_min = line.age_years
		else: 										# Error 
			self.age_undefined = self.age_undefined + 1



# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		#print()
		#print('X - Age - Get Counters')

		return self.age_max, self.age_min, self.age_sum, self.age_undefined



# ----------------------------------------------------------- Fields ---------------------------------------------

	age_mean = fields.Float(
			default=0,
			string='Promedio',
		)


	age_sum = fields.Integer(
			default=0,
			string='Acumulada',
		)

	age_max = fields.Integer(
			default=0,
			string='Máxima',
		)

	age_min = fields.Integer(
			default=0,
			string='Mínima',
		)

	age_undefined = fields.Integer(
			default=0,
			string='Indefinida',
		)

