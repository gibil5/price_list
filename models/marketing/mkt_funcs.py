# -*- coding: utf-8 -*-
"""
	Mkt Funcs - Dep ???

	get_orders_filter_no_cn

	Created: 	       2019
	Updated: 	14 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
import datetime




# ----------------------------------------------------------- Get Orders Faster -------------------
def get_orders_filter_no_cn(self, date_bx, date_ex):
	"""
	Should be Static Method in Order

	Only Used by Marketing
	Only Sales and Cancel. Not Credit Notes. 
	"""
	#print()
	#print('Pl - Get Orders - Fast Fast')


	# Init
	DATETIME_FORMAT = "%Y-%m-%d"
	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	# Get Orders
	orders = self.env['sale.order'].search([
													('state', 'in', ['sale', 'draft']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													('state', 'in', ['sale', 'draft']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_fast_fast

