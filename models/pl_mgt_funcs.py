# -*- coding: utf-8 -*-


# ----------------------------------------------------------- Get orders - By patient --------------
# Provides sales between begin date and end date. Filters: by patient.
def get_orders_filter_by_patient_fast(self, patient):
	"""
	Sales.
	Must include Credit Notes.
	"""
	#print()
	#print('Get Orders Filter - By patient')


	# Search

	# Orders
	orders = self.env['sale.order'].search([
													#('state', '=', 'sale'),
													('state', 'in', ['sale', 'credit_note']),

													('patient', '=', patient),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													#('state', '=', 'sale'),
													('state', 'in', ['sale', 'credit_note']),

													('patient', '=', patient),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_by_patient_fast




# ----------------------------------------------------------- Get orders - By patient --------------
# Provides sales between begin date and end date. Filters: by patient.
def get_orders_filter_by_patient(self, date_bx, date_ex, patient):
	"""
	Sales.
	Must include Credit Notes.
	"""
	#print()
	#print('Get Orders Filter - By patient')


	# Init
	# Dates
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_begin = date_bx + ' 05:00:00'
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Prints
	#print date_end_dt


	# Search

	# Orders
	orders = self.env['sale.order'].search([
													#('state', '=', 'sale'),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													
													('patient', '=', patient),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													#('state', '=', 'sale'),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													
													('patient', '=', patient),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_by_patient
