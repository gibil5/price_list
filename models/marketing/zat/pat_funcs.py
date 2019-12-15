# -*- coding: utf-8 -*-
"""
	Pat Funcs - For Marketing - Dep

	Created: 	11 Dec 2019
	Updated: 	11 Dec 2019
"""

from __future__ import print_function
from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Get Patients ------------------------------------------------------
@api.multi
def get_patients_filter_for_mkt(self, date_bx, date_ex, mode):
	"""
	Provides Patients between begin date and end date. 
	Corrected for Legacy Patients
	"""
	print()
	print('Get Patients Filter - For Mkt')


	# Dates	
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'
	date_end_dt  = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')



	# Legacy 
	if mode == 'legacy': 

		# Patients 
		patients = self.env['oeh.medical.patient'].search([
															('create_date', '>=', date_begin),													
															('create_date', '<', date_end),
												],
													order='create_date asc',
													#limit=1,
													#limit=500,
												)
		# Count 
		count = self.env['oeh.medical.patient'].search_count([													
																('create_date', '>=', date_begin),
																('create_date', '<', date_end),															
												],
													#order='x_serial_nr asc',
													#limit=1,
												)

	# Normal 
	elif mode == 'normal': 

		# Patients 
		patients = self.env['oeh.medical.patient'].search([
															('x_date_record', '>=', date_begin),													
															('x_date_record', '<', date_end),
												],
													order='create_date asc',
													#limit=1,
													#limit=500,
												)
		# Count 
		count = self.env['oeh.medical.patient'].search_count([
																('x_date_record', '>=', date_begin),
																('x_date_record', '<', date_end),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
	# Test
	elif mode == 'test': 

		# Patients 
		patients = self.env['oeh.medical.patient'].search([
															('x_test', '=', True),

												],
													order='create_date asc',
													#limit=1,
												)
		# Count 
		count = self.env['oeh.medical.patient'].search_count([
																('x_test', '=', True),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)

	# Else
	else:
		print('Error: This should not happen !')


	return patients, count

# get_patients_filter
