# -*- coding: utf-8 -*-
"""
	Patient - Object Oriented

	Only functions. Not the data model. 

	Used by Marketing - Patient Lines

 	Created: 		26 Aug 2016
	Last up: 		11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import count_funcs
from . import exc_pat

class Patient(models.Model):
	"""
	Patient
	Encapsulates Business Rules. Should not extend the Data Model.
	"""
	_inherit = 'oeh.medical.patient'



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


	def get_district(self):
		"""
		Used by Marketing - Patient Line
		"""
		if self.street2 != False: 
			return self.street2.title()





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

