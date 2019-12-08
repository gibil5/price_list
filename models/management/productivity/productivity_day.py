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
from openerp.addons.price_list.models.management import mgt_funcs


class ProductivityDay(models.Model):
	"""
	Productivity Day
	All names must be extremely descriptive
	"""


	#_name = 'productivity.day'
	_inherit = 'productivity.day'


	_order = 'date asc'


# ----------------------------------------------------------- Dep ? --------------------------
	#state = fields.Selection(
	#		selection=[
	#						('today', 'Hoy'),
							#('holiday', 'Feriado'),
	#		],
	#		string='Estado',
	#	)


	#holiday = fields.Boolean(
	#		'Feriado',
	#		default=False,
			#readonly=True,
	#	)



# ----------------------------------------------------------- Relational --------------------------

	management_id = fields.Many2one(
			'openhealth.management',

			ondelete='cascade',  	# When the management is deleted, the productivity_day is also deleted

			required=True,
		)

	configurator_emr_id = fields.Many2one(

			'openhealth.configurator.emr',

			#required=True,
		)



# ----------------------------------------------------------- Required - At creation --------------------------
	name = fields.Char(
			'Name',
			required=True,
		)

	date = fields.Date(
			'Fecha',
			required=True,
		)

	weekday = fields.Selection(
			selection=ord_vars._weekday_list,
			string='Dia de semana',
			required=True,
		)

	duration = fields.Float(
			'Duracion',
			required=True,
		)




# ----------------------------------------------------------- Computes --------------------------
	today = fields.Boolean(
			'Hoy',
			default=False,
			compute='_compute_today',
		)

	@api.multi
	def _compute_today(self):
		for record in self:
			if lib.is_today_date(record.date):
				record.today = True




# ----------------------------------------------------------- Primitives - After creation --------------------------

	amount = fields.Float(
			'Venta por dia',
			digits=(16, 1),
		)



	# Cumulative
	cumulative = fields.Float(
			'Acumulado',
			#digits=(16, 1),
		)

	nr_days = fields.Float(
			'Nr dias',
		)

	nr_days_total = fields.Float(
			'Total dias',
		)




	# Average
	avg_amount = fields.Float(
			'Promedio diario',
			#digits=(16, 1),
		)

	projection = fields.Float(
			'Proyección a final del mes',
		)




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
		high level support for doing this and that.
		"""
		#print()
		#print('Update - Average')
		self.avg_amount = self.cumulative / self.nr_days



# ----------------------------------------------------------- Update Projection ------------------------------
	# Update
	@api.multi
	def update_projection(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update - Projection')
		self.projection = self.avg_amount * self.nr_days_total


