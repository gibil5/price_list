# -*- coding: utf-8 -*-
"""
	Mkt Funcs - Dep ? 

	pl_patient_line_analysis
	pl_family_analysis
	pl_family_analysis_2018


	Updated: 	11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Calculate Percentages ------------------------------------------------------

# Provides Percentage
@api.multi
def get_per(self, value, total):
	#print()
	#print('Pl - Get Per')
	#per = 0 
	per = 0.
	if total != 0: 
		#per = ( float(value) / float(total) ) * 100
		per = float(value) / float(total)
	return per
# get_per



# ----------------------------------------------------------- Family Analysis - PL -----------------------
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



# ----------------------------------------------------------- Line Analysis - PL -----------------------
#def pl_line_analysis(self, line):
def pl_patient_line_analysis(self, line):
	"""
	New - 2019
	Used by: Marketing
	Patient Line Analysis to update counters
	"""
	print()
	print('X - Patient Line Analysis')


# Sex
	if line.sex == 'Male': 
		self.sex_male = self.sex_male + 1
	elif line.sex == 'Female': 
		self.sex_female = self.sex_female + 1
	else: 
		self.sex_undefined = self.sex_undefined + 1


# Age Max and Min 
	#if line.age_years not in[ -1, 0]: 			# Not an Error 
	if line.age_years >= 0:
		#count_a = count_a + line.age_years 
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


# First Contact 
	if line.first_contact == 'none': 
		self.how_none = self.how_none + 1

	elif line.first_contact == 'recommendation': 
		self.how_reco = self.how_reco + 1

	elif line.first_contact == 'tv': 
		self.how_tv = self.how_tv + 1

	elif line.first_contact == 'radio': 
		self.how_radio = self.how_radio + 1

	elif line.first_contact == 'internet': 
		self.how_inter = self.how_inter + 1

	elif line.first_contact == 'website':
		self.how_web = self.how_web + 1

	elif line.first_contact == 'mail_campaign':
		self.how_mail = self.how_mail + 1



	# New
	elif line.first_contact == 'facebook':
		self.how_facebook = self.how_facebook + 1

	elif line.first_contact == 'instagram':
		self.how_instagram = self.how_instagram + 1

	elif line.first_contact == 'callcenter':
		self.how_callcenter = self.how_callcenter + 1

	elif line.first_contact == 'old_patient':
		self.how_old_patient = self.how_old_patient + 1


	# Undefined
	#else: 
	elif line.first_contact in [False, '']:
		self.how_u = self.how_u + 1


	else:
		print('Eror: This should not happen !')





	# Education 
	if line.education == 'first': 
		self.edu_fir = self.edu_fir + 1

	elif line.education == 'second': 
		self.edu_sec = self.edu_sec + 1

	elif line.education == 'technical': 
		self.edu_tec = self.edu_tec + 1

	elif line.education == 'university': 
		self.edu_uni = self.edu_uni + 1

	elif line.education == 'masterphd': 
		self.edu_mas = self.edu_mas + 1

	else: 
		self.edu_u = self.edu_u + 1


	# Vip 
	if line.vip: 
		#self.vip_true = self.vip_true + 1
		self.vip_already_true = self.vip_already_true + 1

	else: 
		#self.vip_false = self.vip_false + 1
		self.vip_already_false = self.vip_already_false + 1




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
