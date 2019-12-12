# -*- coding: utf-8 -*-
"""
	Mkt Funcs - Dep ? 

	pl_family_analysis
	pl_family_analysis_2018

	Created: 	       2019
	Updated: 	11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Family Analysis - PL -----------------------
def pl_family_analysis(self, line):
	"""
	New - 2019
	Marketing
	Analyses Line to update counters
	"""
	print()
	print('X - Family Analysis')

	# Family
	if line.product_id.type in ['product']:
		family = 'product'
		subfamily = line.product_id.pl_family
		subsubfamily = line.product_id.pl_subfamily

	elif line.product_id.type in ['service']:

		if line.product_id.pl_subfamily in ['consultation']:
			#family = line.product_id.pl_subfamily
			family = 'consultation'
			subfamily = 'consultation'
			subsubfamily = 'consultation'

		else:
			family = 'procedure'
			subfamily = line.product_id.pl_family
			subsubfamily = line.product_id.pl_subfamily

	return family, subfamily, subsubfamily

	# pl_family_analysis



# ----------------------------------------------------------- Family Analysis - 2018 -----------------------
def pl_family_analysis_2018(self, line):
	"""
	New - 2019
	Marketing
	Analyses Line to update counters
	"""
	print()
	print('X - Family Analysis - 2018')

	family = 'x'
	subfamily = 'x'
	subsubfamily = 'x'


	# Family
	if line.product_id.type in ['product']:
		family = 'product'
		subfamily = line.product_id.x_family
		#subsubfamily = line.product_id.pl_subfamily

	elif line.product_id.type in ['service']:

		#if line.product_id.pl_subfamily in ['consultation']:
		if line.product_id.x_family in ['consultation']:
			#family = line.product_id.pl_subfamily
			family = 'consultation'
			subfamily = 'consultation'
			subsubfamily = 'consultation'

		else:
			family = 'procedure'
			subfamily = line.product_id.x_family
			subsubfamily = line.product_id.x_treatment

	return family, subfamily, subsubfamily







# ----------------------------------------------------------- Is New Patient ? ------------------------------------------------------
@api.multi
def is_new_patient(self, patient, date_bx, date_ex):
	"""
	Is New Patient ?
	The patient has been created this month
	"""
	#print()
	#print('Is New Patient')
	#print(patient)

	# Dates	
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'
	date_end_dt  = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Must Correct !
	if (patient.x_date_record >= date_begin) and (patient.x_date_record < date_end):
		is_new = True
	else:
		is_new = False

	return is_new

# is_new_patient


# ----------------------------------------------------------- Calculate Percentages ------------------------------------------------------
def get_per(value, total):
	"""
	Provides Percentage - New
	Does not use Self
	"""
	#print()
	#print('Pl - Get Per')
	#print(value)
	#print(total)

	per = 0.
	if total != 0: 
		per = float(value) / float(total)
	return per
# get_per_nex
