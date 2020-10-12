# -*- coding: utf-8 -*-
"""
	Productivity Day

	Simplified version of Day Line


	Created: 			 7 Dec 2019
	Last up: 			 7 Dec 2019
"""

from __future__ import print_function
import numpy as np
from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

from openerp.addons.openhealth.models.libs import lib

#from . import mgt_funcs
from openerp.addons.price_list.models.management.lib import mgt_funcs


class ProductivityDay(models.Model):
	"""
	Productivity Day
	All names must be extremely descriptive
	"""


	#_name = 'productivity.day'
	_inherit = 'productivity.day'


	_order = 'date asc'



# ----------------------------------------------------------- Update Amount ------------------------------
	# Update
	@api.multi
	def update_amount(self):
		"""
		Update Amount
		"""
		print()
		print('X - Update - amount')

		# Init
		data_amount = []


		# Search
		orders, count = mgt_funcs.get_orders_filter_fast(self, self.date, self.date)
		#print(orders)
		#print(count)


		# All
		for order in orders:
			data_amount.append(order.x_amount_flow)


		# Total
		self.x_count = len(data_amount)
		if self.x_count != 0:
			self.amount = np.sum(data_amount)

	# update_amount






# ----------------------------------------------------------- Update Average ------------------------------
	# Update
	@api.multi
	def update_avg(self):
		"""
		Update Average
		"""
		#print()
		#print('Update - Average')
		self.avg_amount = self.cumulative / self.nr_days




# ----------------------------------------------------------- Update Projection ------------------------------
	# Update
	@api.multi
	def update_projection(self):
		"""
		Update Projection
		"""
		#print()
		#print('Update - Projection')
		self.projection = self.avg_amount * self.nr_days_total




