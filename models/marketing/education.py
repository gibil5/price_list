# -*- coding: utf-8 -*-
"""
	Education - Object Oriented
	
	Extract BL from Structure

	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

import mkt_funcs

class Education(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.education'

	_description = 'Openhealth Marketing Education'

	#_order = 'date_create asc'




# ----------------------------------------------------------- Analyse -----------------------
	def update_per(self, mkt):
		"""
		Patient Line Analysis to update counters
		"""
		#print()
		#print('X - Education - Update Per')

		mkt.edu_fir_per = mkt_funcs.get_per(mkt.edu_fir, mkt.total_count)
		mkt.edu_sec_per = mkt_funcs.get_per(mkt.edu_sec, mkt.total_count)
		mkt.edu_tec_per = mkt_funcs.get_per(mkt.edu_tec, mkt.total_count)
		mkt.edu_uni_per = mkt_funcs.get_per(mkt.edu_uni, mkt.total_count)
		mkt.edu_mas_per = mkt_funcs.get_per(mkt.edu_mas, mkt.total_count)
		mkt.edu_u_per = mkt_funcs.get_per(mkt.edu_u, mkt.total_count)



# ----------------------------------------------------------- Analyse -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		#print()
		#print('X - Education - analyse')


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
		#print()
		#print('X - Education - Get Counters')

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





