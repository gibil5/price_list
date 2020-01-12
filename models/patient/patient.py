# -*- coding: utf-8 -*-
"""
	Patient - Object Oriented

	Only functions. Not the data model. 

	Used by Marketing - Patient Lines

 	Created: 		26 Aug 2016
	Last up: 		11 Dec 2019
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import count_funcs
from . import exc_pat

class Patient(models.Model):
	"""
	Patient
	Encapsulates Business Rules. Should not extend the Data Model.
	"""
	_inherit = 'oeh.medical.patient'




# ----------------------------------------------------------- Alta -----------------------
	@api.multi
	def discharge_myself(self):
		"""
		Discharge Patient
		"""
		self.discharged = True


	@api.multi
	def recall_myself(self):
		"""
		Recall Patient
		"""
		self.discharged = False




# ----------------------------------------------------------- Class Vars -----------------------

	_sex_type_list = [
						('Male', 'Masculino'),
						('Female', 'Femenino'),
	]


	_education_level_type = [
				('first', 'Primaria'),
				('second', 'Secundaria'),
				('technical', 'Instituto'),
				('university', 'Universidad'),
				('masterphd', 'Posgrado'),
	]



# ----------------------------------------------------------- Static Methods -----------------------

	@staticmethod
	def is_new_patient(self, patient, date_bx, date_ex):
		"""
		Is New Patient ?
		The patient has been created inside this date delta 
		Used by Marketing
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








	@staticmethod
	def get_patients_mkt(self, date_bx, date_ex, mode):
		"""
		Provides Patients between begin date and end date. 
		Corrected for Legacy Patients
		"""		
		print()
		print('Patient - Get Patients Mkt')

		print(self)
		print(date_bx)
		print(date_ex)
		print(mode)

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






# ----------------------------------------------------------- Getters - Mkt - EMR -----------
	
# Origin

	# Origin
	def get_origin(self):
		"""
		Used by Marketing - Patient Line
		"""
		#print()
		#print('Get Origin')

		return self.origin.short_name






# EMR

	# Chief complaint
	def get_chief_complaint(self):
		"""
		Used by Marketing - Patient Line
		"""
		chief_complaint = self.get_last_treatment().chief_complaint
		return chief_complaint


	# Diagnosis
	def get_diagnosis(self):
		"""
		Used by Marketing - Patient Line
		"""
		diagnosis = self.get_last_consultation().x_diagnosis
		return diagnosis


	# Treatment
	def get_last_treatment(self):
		"""
		EMR - Treatment
		Used by Marketing - Patient Line
		"""
		treatment = self.env['openhealth.treatment'].search([
																('patient','=', self.name),
														],
														order='start_date desc',
														limit=1,)
		return treatment


	# Consultation
	def get_last_consultation(self):
		"""
		EMR - Consultation
		Used by Marketing - Patient Line
		"""
		consultation = self.env['openhealth.consultation'].search([
																		#('treatment','=', self.treatment.id),
																		('patient','=', self.name),
														],
														order='evaluation_start_date desc',
														limit=1,)
		return consultation




# ----------------------------------------------------------- Getters - Mkt -----------

# Places

	def get_country(self):
		"""
		Used by Marketing - Patient Line
		"""
		if self.country_id.name != False: 
			return self.country_id.name



	def get_city(self):
		"""
		Used by Marketing - Patient Line
		"""
		if self.city != False: 
			return self.city.title()
			#return self.city



	def get_district(self):
		"""
		Used by Marketing - Patient Line
		"""
		if self.street2 != False: 
			name = self.street2
			return name





# Age
	def get_age_years(self):
		"""
		Used by Marketing - Patient Line
		"""
		# Age 
		if self.age.split()[0] != 'No': 
			return self.age.split()[0]


# Measures

	def get_sex_measure(self):
		"""
		Used by Marketing - Patient Line
		"""

		# Init
		#mea_m = 0 
		#mea_f = 0
		#mea_u = 0

		mea_m, mea_f, mea_u = 0, 0, 0

		if self.sex == 'Male': 
			mea_m = 1

		elif self.sex == 'Female':
			mea_f = 1

		else:
			mea_u = 1

		return mea_m, mea_f, mea_u



	def get_vip_measure(self):
		"""
		Used by Marketing - Patient Line
		"""

		# Init
		#mea_vip = 0
		#mea_vip_no = 0

		mea_vip, mea_vip_no = 0, 0


		# Vip 
		if self.x_vip: 
			mea_vip = 1
		else: 
			mea_vip_no	= 1

		return mea_vip, mea_vip_no



	def get_education_measure(self):
		"""
		Used by Marketing - Patient Line
		"""

		# Init
		#mea_first = 0
		#mea_second = 0
		#mea_technical = 0

		#mea_university = 0
		#mea_masterphd = 0
		#mea_edu_u =0

		mea_first, mea_second, mea_technical, mea_university, mea_masterphd, mea_edu_u = 0, 0, 0, 	0, 0, 0


		# Education
		education = self.x_education_level

		if education == 'first': 
			mea_first = 1

		elif education == 'second': 
			mea_second = 1

		elif education == 'technical': 
			mea_technical = 1

		elif education == 'university': 
			mea_university = 1

		elif education == 'masterphd': 
			mea_masterphd = 1 

		else: 
			mea_edu_u = 1			

		return mea_first, mea_second, mea_technical, mea_university, mea_masterphd, mea_edu_u 




	def get_first_contact_mea(self):
		"""
		Used by Marketing - Patient Line
		"""

		mea_recommendation, mea_tv, mea_radio, mea_internet, mea_website, mea_mail_campaign, mea_how_none, mea_how_u = 0, 0, 0, 0, 	0, 0, 0, 0


		# First Contact 
		first_contact = self.x_first_contact


		if first_contact == 'recommendation': 
			mea_recommendation = 1

		elif first_contact == 'tv': 
			mea_tv = 1

		elif first_contact == 'radio': 
			mea_radio = 1

		elif first_contact == 'internet': 
			mea_internet = 1

		elif first_contact == 'website': 
			mea_website = 1

		elif first_contact == 'mail_campaign': 
			mea_mail_campaign = 1

		elif first_contact == 'none': 
			mea_how_none = 1

		else: 
			mea_how_u = 1

		return mea_recommendation, mea_tv, mea_radio, mea_internet, mea_website, mea_mail_campaign, mea_how_none, mea_how_u 




# ----------------------------------------------------------- Validate -----------
	@api.multi
	def validate(self):
		"""
		Validate Patient, for Id Doc.
		Triggered by all Buttons
		"""
		print()
		print('X - Patient Validate')

		# Handle Exceptions
		exc_pat.handle_exceptions(self)


# ----------------------------------------------------------- Validate For Invoice -----------
	@api.multi
	def validate_for_invoice(self):
		"""
		Validate Patient, for Invoice
		Used by Electronic Container (Txt Generation). 
		"""
		print()
		print('X - Patient Validate for Invoice')

		# Handle Exceptions
		exc_pat.handle_exceptions_invoice(self)

