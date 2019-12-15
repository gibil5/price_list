# -*- coding: utf-8 -*-
"""
	Vip - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from openerp.addons.price_list.models.marketing.marketing import Marketing  	# Use static method

class Vip(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.vip'

	_description = 'Openhealth Marketing Vip'

	#_order = 'date_create asc'


# ----------------------------------------------------------- Class Vars -----------------------

	# Vip Arrays
	#vip_arr = []
	#not_vip_arr = []



# ----------------------------------------------------------- Update Stats ---------------------------------------------
	def update_stats(self, mkt):
		"""
		Update Vip
		"""

		mkt.vip_true_per = 	Marketing.get_per(mkt.vip_true, mkt.total_count)
		mkt.vip_false_per = Marketing.get_per(mkt.vip_false, mkt.total_count)



# ----------------------------------------------------------- Analyse -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		#print()
		#print('X - Vip - analyse')

		# Vip 
		if line.vip: 
			self.vip += 1

		else: 
			self.not_vip += 1



# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		#print()
		#print('X - Vip - Get Counters')

		return self.vip, self.not_vip, self.vip_already, self.not_vip_already


# ----------------------------------------------------------- Fields ---------------------------------------------

	vip = fields.Integer(
			default=0,
			#string='Vip por venta mes',
			string='Vip',
		)

	not_vip = fields.Integer(
			default=0,
			string='No Vip',
		)


	vip_already = fields.Integer(
			default=0,
			string='Vip por venta anterior',
		)

	not_vip_already = fields.Integer(
			default=0,
			#string='',
		)



