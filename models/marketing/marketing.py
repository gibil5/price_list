# -*- coding: utf-8 -*-
"""
 	Price List - Marketing Report - Object Oriented

	Only functions. Not the data model. 

 	Created: 				19 May 2018
 	Last up: 	 			11 Dec 2019
"""
from __future__ import print_function
import datetime
from timeit import default_timer as timer
import collections
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars

from openerp.addons.openhealth.models.marketing import lib_marketing

from openerp.addons.price_list.models.management.lib import mgt_funcs
from openerp.addons.price_list.models.lib import test_funcs

from . import mkt_funcs

from . import pat_funcs

from . import mkt_vars
from . import stax
from . import exc_mkt

class Marketing(models.Model):
	"""
	Marketing Report
	"""
	_inherit = 'openhealth.marketing'



# ----------------------------------------------------- Stats ------------------------------------------------------------------

	# Sex
	sex = fields.Many2one(
			'openhealth.marketing.sex', 
		)

	# Age
	age = fields.Many2one(
			'openhealth.marketing.age', 
		)

	# Origin
	origin = fields.Many2one(
			'openhealth.marketing.origin', 
		)

	# Education
	education = fields.Many2one(
			'openhealth.marketing.education', 
		)

	# First Contact
	first_contact = fields.Many2one(
			'openhealth.marketing.first_contact', 
		)




# ----------------------------------------------------------- Update ---------------------------------------------
	@api.multi
	def update(self):
		"""
		Update Patient + Sales
		Used by Django
		"""
		print()
		print('X - Update')

		self.update_patients()

		self.update_sales()

		print()

		# For Django
		self.date_test = datetime.datetime.now() 

		return 1 	# For Django
	# update_fast





# ----------------------------------------------------------- First Level - Buttons ---------------------------------------------


# ----------------------------------------------------------- Update Patients - Step 1 - Button ---------------------
	# Update Patients
	@api.multi
	def update_patients(self):
		"""
		Update Patients
		To see the Stats Macro 
		"""
		#print()
		print('X - Update Patients')

		# Handle Exceptions - Dep
		#exc_mkt.handle_exceptions(self)




# Macros - Counters - Init


		# Education
		self.education.unlink()
		name = 'Educación'	
		self.education = self.env['openhealth.marketing.education'].create({
																			'name': name,
																		})
		print(self.education)



		# First Contact
		self.first_contact.unlink()
		name = 'Primer Contacto'	
		self.first_contact = self.env['openhealth.marketing.first_contact'].create({
																					'name': name,
																		})
		print(self.first_contact)



		# Sex
		self.sex.unlink()
		name = 'Sexo'	
		self.sex = self.env['openhealth.marketing.sex'].create({
																			'name': name,
																		})
		print(self.sex)


		# Age
		self.age.unlink()
		name = 'Edad'
		self.age = self.env['openhealth.marketing.age'].create({
																			'name': name,
																		})
		print(self.age)





		# QC
		t0 = timer()
		now_0 = datetime.datetime.now()


		# Clear
		self.reset()


		# Get Patients - For Mkt
		mode = self.mode
		patients, count = pat_funcs.get_patients_filter_for_mkt(self, self.date_begin, self.date_end, mode)

		self.total_count = count


		# Loop
		for patient in patients:



		# Patient Getters


			# EMR
			treatment = patient.get_last_treatment()
			consultation = patient.get_last_consultation()
			chief_complaint = patient.get_chief_complaint()
			diagnosis = patient.get_diagnosis()


			# Places
			country = patient.get_country()
			city = patient.get_city()
			district = patient.get_district()

			# Age
			age_years = patient.get_age_years()


			# Sex
			mea_m, mea_f, mea_u = patient.get_sex_measure()

			# Vip
			mea_vip, mea_vip_no = patient.get_vip_measure()





			# Education
			mea_first, mea_second, mea_technical, mea_university, mea_masterphd, mea_edu_u = patient.get_education_measure()

			# First contact
			mea_recommendation, mea_tv, mea_radio, mea_internet, mea_website, mea_mail_campaign, mea_how_none, mea_how_u = patient.get_first_contact_mea()



			# Create
			pat_line = self.patient_line.create({
														'patient': patient.id,
														'emr': 		patient.x_id_code,  # Serial nr
														
														# Dates
														'date_create': patient.create_date,
														'date_record': patient.x_date_record,

														# EMR
														'treatment': treatment.id,
														'consultation': consultation.id,
														'chief_complaint': chief_complaint,
														'diagnosis': diagnosis, 

														# Sex
														'sex': patient.sex,
														'mea_m': mea_m,
														'mea_f': mea_f,
														'mea_u': mea_u,

														# Personal
														'dob': patient.dob,
														'age': patient.age,
														'age_years': age_years,
														'function': patient.function,
														'phone_1': 	patient.mobile,
														'phone_2': 	patient.phone,
														'email': 	patient.email,
														

# Stats
														# Vip
														'vip': patient.x_vip,														


														# Places
														#'country': patient.country_id.name,
														'country': country,
														'city': city,
														'district': district,



														# First contact
														'first_contact': patient.x_first_contact,														

														# Education
														'education': patient.x_education_level,


														# Handle
														'marketing_id': self.id,
													})
		# End create


		# Set Stats
		stax.update_stats(self)



		# Update Vip Sales
		stax.update_vip_sales(self)


		# Build Histo
		lib_marketing.build_histogram(self)


		# Build Media - Dep ?
		lib_marketing.build_media(self)


		# Build Places
		lib_marketing.build_districts(self)
		lib_marketing.build_cities(self)



		# QC
		t1 = timer()
		now_1 = datetime.datetime.now()
		self.delta_patients = t1 - t0




# Update Macros - Counters

		# Education
		self.edu_fir, self.edu_sec, self.edu_tec, self.edu_uni, self.edu_mas, self.edu_u = self.education.get_counters()
		self.education.update_per(self)


		# First Contact
		self.how_none, self.how_reco, self.how_tv, self.how_radio, self.how_inter, self.how_web, self.how_mail, self.how_facebook,\
		self.how_instagram, self.how_callcenter, self.how_old_patient, self.how_u = self.first_contact.get_counters()
		self.first_contact.update_per(self)


		# Sex
		self.sex_male, self.sex_female, self.sex_undefined = self.sex.get_counters()
		self.sex.update_per(self)


		# Age
		self.age_max, self.age_min, self.age_sum, self.age_undefined = self.age.get_counters()
		self.age.update_stats(self)


	# update_patients





# ----------------------------------------------------------- Update Sales - Step 2 - Button ------------------------
	# Update Sales
	@api.multi
	def update_sales(self):
		"""
		Update Sales
		To see the detail 
		"""
		print()
		print('X - Update Sales')


		# Handle Exceptions
		#exc_mkt.handle_exceptions(self)


		# Go

		# Print Disable
		test_funcs.disablePrint()

		# Init 
		self.delta_create_sale_lines = 0
		self.delta_analyse_sale_lines = 0
		self.delta_analyse_patient_lines = 0



		# Analyse and Create
		stax.create_sale_lines(self)
		stax.analyse_sale_lines(self)
		stax.analyse_patient_lines(self)



		# Benchmark
		self.delta_sales_pl = self.delta_create_sale_lines + self.delta_analyse_sale_lines + self.delta_analyse_patient_lines


		# Print Enable
		test_funcs.enablePrint()

	# pl_update_sales






# ----------------------------------------------------------- Natives -----------------------------
	
	mode = fields.Selection(

			selection=mkt_vars._mode_list,

			default='normal',
			required=True,
		)

	delta_create_sale_lines = fields.Float()

	delta_analyse_sale_lines = fields.Float()
	
	delta_analyse_patient_lines = fields.Float()

	delta_sales_pl = fields.Float(
			'Delta Ventas',
		)

	patient_product_count = fields.Integer(
			'Nr Productos',
		)

	# Alt
	sale_line_sale_count = fields.Integer(
			#'Nr Ventas Alt',
			'Nr Ventas',
		)
	sale_line_consultation_count = fields.Integer(
			#'Nr Consultas Alt',
			'Nr Consultas',
		)

	sale_line_procedure_count = fields.Integer(
			#'Nr Procedimientos Alt',
			'Nr Procedimientos',
		)

	sale_line_product_count = fields.Integer(
			#'Nr Productos Alt',
			'Nr Productos',
		)

	sale_line_budget_count = fields.Integer(
			#'Nr Presupuestos Alt',
			'Nr Presupuestos',
		)




# ----------------------------------------------------------- Natives ------------------------------------------------------

	price_list_2019_count = fields.Integer(
			'pl 2019',
		)

	price_list_2018_count = fields.Integer(
			'pl 2018',
		)


	test_obj = fields.Boolean()


	# Vip
	vip_true_per = fields.Float(
			'Vip Si %',
			readonly=True,
			digits=(12, 3),
		)

	vip_false_per = fields.Float(
			'Vip No %',
			readonly=True,
			digits=(12, 3),
		)

	vip_already_true = fields.Integer()

	vip_already_false = fields.Integer()

	vip_already_true_per = fields.Float(
			digits=(12, 3),
		)



# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Patient Lines
	patient_line = fields.One2many(
			'openhealth.patient.line',
			'marketing_id',
		)


	# Sales
	#sale_line_tkr = fields.One2many(
	sale_line = fields.One2many(
			#'openhealth.marketing.order.line',
			'price_list.marketing.order_line',
			'marketing_id',
		)



# ----------------------------------------------------------- Natives ----------------------

	year = fields.Selection(
			selection=ord_vars._year_order_list,
			string='Año',
			required=True,

			default='2019',
		)

	month = fields.Selection(
			selection=ord_vars._month_order_list,
			string='Mes',
			#required=True,
		)

	owner = fields.Selection(
			[
				('week', 'Week'),
				('month', 'Month'),
				('year', 'Year'),
			],
			required=True,

			default='month',
		)


# ----------------------------------------------------------- Age  ----------------------------------
	# Age
	age_mean = fields.Float(
			'Edad Promedio',
			readonly=True,
			digits=(12, 3),
		)

	age_sum = fields.Float(
			#'Edad Promedio',
			#readonly=True,
			digits=(12, 3),
		)



# ----------------------------------------------------------- Sex  ----------------------------------

	# Sex
	#sex_male = fields.Float(
	sex_male = fields.Integer(
			#'Sexo M',
			'Masculino',
			readonly=True,
		)

	#sex_female = fields.Float(
	sex_female = fields.Integer(
			#'Sexo F',
			'Femenino',
			readonly=True,
		)

	#sex_undefined = fields.Float(
	sex_undefined = fields.Integer(
			#'Sexo Error',
			'Error',
			readonly=True,
		)



	# Sex
	sex_male_per = fields.Float(
			#'M %',
			'Masculino %',
			readonly=True,
			digits=(12, 3),
		)

	sex_female_per = fields.Float(
			#'F %',
			'Femenino %',
			readonly=True,
			digits=(12, 3),
		)

	sex_undefined_per = fields.Float(
			'Error %',
			readonly=True,
			digits=(12, 3),
		)


# ----------------------------------------------------------- Education Level  ----------------------------------

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True,
			digits=(12, 3),
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True,
			digits=(12, 3),
		)

	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True,
			digits=(12, 3),
		)

	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True,
			digits=(12, 3),
		)

	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True,
			digits=(12, 3),
		)

	edu_u_per = fields.Float(
			'No Definido %',
			readonly=True,
			digits=(12, 3),
		)

# ----------------------------------------------------------- First Contact ----------------------------------

	# First Contact - Nr
	how_u = fields.Integer(
			'No Definido',
			readonly=True,
		)

	how_none = fields.Integer(
			'Ninguno',
			readonly=True,
		)

	how_reco = fields.Integer(
			'Recomendación',
			readonly=True,
		)

	how_tv = fields.Integer(
			'Tv',
			readonly=True,
		)

	how_radio = fields.Integer(
			'Radio',
			readonly=True,
		)

	how_inter = fields.Integer(
			'Internet',
			readonly=True,
		)

	how_web = fields.Integer(
			'Web',
			readonly=True,
		)

	how_mail = fields.Integer(
			'Mail',
			readonly=True,
		)

	# New
	how_facebook = fields.Integer(
			'Facebook',
			readonly=True,
			#digits=(12, 3),
		)

	how_instagram = fields.Integer(
			'Instagram',
			readonly=True,
			#digits=(12, 3),
		)

	how_callcenter = fields.Integer(
			'Call center',
			readonly=True,
			#digits=(12, 3),
		)

	how_old_patient = fields.Integer(
			'Paciente Antiguo',
			readonly=True,
			#digits=(12, 3),
		)



	# First Contact - %

	# New Per
	how_facebook_per = fields.Float(
			'Facebook %',
			readonly=True,
			digits=(12, 3),
		)

	how_instagram_per = fields.Float(
			'Instagram %',
			readonly=True,
			digits=(12, 3),
		)

	how_callcenter_per = fields.Float(
			'Callcenter %',
			readonly=True,
			digits=(12, 3),
		)

	how_old_patient_per = fields.Float(
			#'Old_patient %',
			'Paciente Antiguo %',
			readonly=True,
			digits=(12, 3),
		)


	# Standard
	how_u_per = fields.Float(
			'No Definido %',
			readonly=True,
			digits=(12, 3),
		)

	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True,
			digits=(12, 3),
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True,
			digits=(12, 3),
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True,
			digits=(12, 3),
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True,
			digits=(12, 3),
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True,
			digits=(12, 3),
		)


	# Dep
	how_inter_per = fields.Float(
			'Internet %',
			readonly=True,
			digits=(12, 3),
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True,
			digits=(12, 3),
		)


# ----------------------------------------------------------- Clean ------------------------------

	# Clean
	@api.multi
	def clean(self):
		"""
		Clean
		"""
		print('X - Clean')
		print('Begin')

		# If Test Obj
		if self.test_obj:

			# Clear
			self.patient_line.unlink()

			# Clear
			model = 'openhealth.marketing.order.line'

			objs = self.env[model].search([
												('marketing_id', 'in', [False]),
											],
											#order='date_begin asc',
											#limit=1,
				)

			# Unlink
			limit = 1000
			count = 0
			for obj in objs:
				if count < limit:
					obj.unlink()
					count = count + 1

			# Count
			count = self.env[model].search_count([
													('marketing_id', 'in', [False]),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
			print(count)
			print('End')
	# clean



# ----------------------------------------------------------- Reset - Button ------------------------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset
		"""
		print()
		print('X - Reset')


		# Handle Exceptions
		#exc_mkt.handle_exceptions(self)


		# Go
		self.delta_patients = 0
		self.delta_sales_pl = 0
		self.delta_create_sale_lines = 0
		self.delta_analyse_sale_lines = 0
		self.delta_analyse_patient_lines = 0

		# Counts
		self.sale_line_consultation_count = 0
		self.sale_line_procedure_count = 0
		self.sale_line_product_count = 0
		self.sale_line_budget_count = 0
		self.sale_line_sale_count = 0
		self.price_list_2019_count = 0
		self.price_list_2018_count = 0
		self.patient_product_count = 0
		self.patient_sale_count = 0
		self.patient_consu_count = 0
		self.patient_proc_count = 0
		self.patient_budget_count = 0
		self.total_count = 0
		self.patient_reco_count = 0

		# Unlinks
		self.sale_line.unlink()
		self.patient_line.unlink()
		self.histo_line.unlink()
		self.media_line.unlink()
		self.district_line.unlink()
		self.country_line.unlink()
		self.city_line.unlink()

		# First Contact
		self.how_facebook = 0
		self.how_instagram = 0
		self.how_callcenter = 0
		self.how_old_patient = 0
		self.how_facebook_per = 0
		self.how_instagram_per = 0
		self.how_callcenter_per = 0
		self.how_old_patient_per = 0

		# Standard
		self.how_u = 0
		self.how_reco = 0
		self.how_tv = 0
		self.how_radio = 0
		self.how_web = 0
		self.how_mail = 0

		# Dep
		self.how_inter = 0
		self.how_none = 0

		# Standard
		self.how_u_per = 0
		self.how_reco_per = 0
		self.how_tv_per = 0
		self.how_radio_per = 0
		self.how_web_per = 0
		self.how_mail_per = 0

		# Dep
		self.how_inter_per = 0
		self.how_none_per = 0

		# Sex
		self.sex_male = 0
		self.sex_female = 0
		self.sex_undefined = 0
		self.sex_male_per = 0
		self.sex_female_per = 0
		self.sex_undefined_per = 0

		# Age
		self.age_sum = 0
		self.age_mean = 0
		self.age_max = 0
		self.age_min = 0
		self.age_undefined = 0

		# Education
		self.edu_fir = 0
		self.edu_sec = 0
		self.edu_tec = 0
		self.edu_uni = 0
		self.edu_mas = 0
		self.edu_u = 0
		self.edu_fir_per = 0
		self.edu_sec_per = 0
		self.edu_tec_per = 0
		self.edu_uni_per = 0
		self.edu_mas_per = 0
		self.edu_u_per = 0

		# Vip
		self.vip_already_true = 0
		self.vip_already_false = 0
		self.vip_true = 0
		self.vip_false = 0
		self.vip_true_per = 0
		self.vip_false_per = 0
	# reset
