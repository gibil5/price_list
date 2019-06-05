# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api
import datetime


# ----------------------------------------------------------- Line Analysis - PL -----------------------
def pl_line_analysis(self, line):
	"""
	New - 2019
	Marketing
	Analyses Line to update counters
	"""
	#print()
	#print('PL - Line Analysis')



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
		self.vip_true = self.vip_true + 1

	else: 
		self.vip_false = self.vip_false + 1






# ----------------------------------------------------------- Calculate Percentages ------------------------------------------------------

# Provides Percentage
@api.multi
#def get_per(self, value, total): 
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



# ----------------------------------------------------------- Get Patients ------------------------------------------------------

# Provides Patients between begin date and end date. 
@api.multi
def get_patients_filter(self, date_bx, date_ex, mode):

	#print
	#print 'Get Patients'


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
	else:
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

	return patients, count

# get_patients_filter

