# -*- coding: utf-8 -*-
"""
	Day Doctor Line

	Created: 			25 Jan 2019
	Last up: 			25 Jan 2019
"""
from __future__ import print_function

#import datetime
from openerp import models, fields, api
#from openerp.addons.openhealth.models.order import ord_vars

class DayDoctorLine(models.Model):
	"""
	high level support for doing this and that.
	"""

	_inherit = 'openhealth.management.day.doctor.line'



# ----------------------------------------------------------- 2019 ------------------------------
	@api.multi
	#def update_macro(self):
	def pl_update_macro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Update - Macro')

		# Clean		
		self.reset_macro()

		for line in self.order_line:
			self.amount = self.amount + line.price_total

			#if line.product_id.x_family in ['consultation']:
			if line.product_id.pl_subfamily in ['consultation']:
				self.nr_consultations = self.nr_consultations + line.product_uom_qty

			#if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:
			elif line.product_id.pl_family in ['laser', 'medical', 'cosmetology', 'echography', 'gynecology', 'promotion']:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty


		if self.nr_consultations != 0:
			print('Gotcha !')
			self.ratio_pro_con = float(self.nr_procedures) / float(self.nr_consultations)

	# update_macro



# ----------------------------------------------------------- 2018 ------------------------------
	@api.multi
	def update_macro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update - Macro')

		# Clean		
		self.reset_macro()

		for line in self.order_line:
			self.amount = self.amount + line.price_total

			if line.product_id.x_family in ['consultation']:
				self.nr_consultations = self.nr_consultations + line.product_uom_qty

			if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty


		if self.nr_consultations != 0:
			print('Gotcha !')
			self.ratio_pro_con = float(self.nr_procedures) / float(self.nr_consultations)

	# update_macro
