# -*- coding: utf-8 -*-
"""
 	Price List - Marketing Report

 	Created: 				19 May 2018
 	Last up: 	 			 3 Jul 2019

	- A Class exposes abstract interfaces that allow its users to manipulate the Essence of the data, 
	  without having to know its Implementation. 

	- Respect the Law of Demeter. Avoid Train Wrecks.

	- Treat the Active Record as a data structure and create separate objects that contain the business rules 
	  and that hide their internal data. These Objects are just instances of the Active Record.	

	- Handle Exceptions.

"""
from __future__ import print_function
import datetime
from timeit import default_timer as timer
import collections
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars
from openerp.addons.openhealth.models.marketing import lib_marketing
from . import mkt_funcs
from . import mkt_vars
from openerp.addons.price_list.models.management import mgt_funcs

from . import mkt_exc

from openerp.addons.price_list.models.lib import test_funcs

class Marketing(models.Model):
	"""
	Marketing Report
	"""
	_inherit = 'openhealth.marketing'



# ----------------------------------------------------------- First Level - Buttons ---------------------------------------------


# ----------------------------------------------------------- Update Patients - Button ---------------------
	# Update Patients
	@api.multi
	def update_patients(self):
		"""
		Update Patients
		"""
		#print()
		print('Pl - Update Patients')


		# Handle Exceptions
		mkt_exc.handle_exceptions(self)


		# Go
		# QC
		t0 = timer()
		now_0 = datetime.datetime.now()

		# Clear
		self.reset()

		# Get Patients
		mode = self.mode
		patients, count = mkt_funcs.get_patients_filter(self, self.date_begin, self.date_end, mode)
		self.total_count = count


		# Loop
		for patient in patients:

			# Create
			pat_line = self.patient_line.create({
														'patient': patient.id,
														'date_create': patient.create_date,
														'date_record': patient.x_date_record,
														'sex': patient.sex,
														'dob': patient.dob,
														'age': patient.age,
														'first_contact': patient.x_first_contact,
														'education': patient.x_education_level,
														'vip': patient.x_vip,
														'country': patient.country_id.name,
														'city': patient.city,
														'district': patient.street2,
														'function': patient.function,
														'emr': 		patient.x_id_code,
														'phone_1': 	patient.mobile,
														'phone_2': 	patient.phone,
														'email': 	patient.email,

														'marketing_id': self.id,
													})
			# Old
			ret = pat_line.update_fields()

			# New
			pat_line.update_emr()


		# Set Stats
		self.update_stats()

		# Update Vip Sales
		self.update_vip_sales()

		# Build Histo
		lib_marketing.build_histogram(self)

		# Build Media - Dep ?
		lib_marketing.build_media(self)

		# Build Places
		lib_marketing.build_districts(self)
		lib_marketing.build_cities(self)

		t1 = timer()
		now_1 = datetime.datetime.now()
		self.delta_patients = t1 - t0

	# update_patients




# ----------------------------------------------------------- Update Sales - Button ------------------------
	# Update Sales
	@api.multi
	def pl_update_sales(self):
		"""
		Pl - Update Sales
		"""
		print()
		print('Pl - Update Sales')


		# Handle Exceptions
		mkt_exc.handle_exceptions(self)


		# Go

		# Print Disable
		test_funcs.disablePrint()

		# Init 
		self.delta_create_sale_lines = 0
		self.delta_analyse_sale_lines = 0
		self.delta_analyse_patient_lines = 0

		# Analyze
		self.create_sale_lines()
		self.analyse_sale_lines()
		self.analyse_patient_lines()
		
		# Benchmark
		self.delta_sales_pl = self.delta_create_sale_lines + self.delta_analyse_sale_lines + self.delta_analyse_patient_lines


		# Print Enable
		test_funcs.enablePrint()

	# pl_update_sales




# ----------------------------------------------------------- Create Sale Lines - Button Hidden ------------------------
	# Create Sales
	@api.multi
	def create_sale_lines(self):
		"""
		Create Sale Lines
		"""
		print()
		print('Create Sale Lines')

		# Handle Exceptions
		mkt_exc.handle_exceptions(self)


		# Go
		# Print Disable
		#test_funcs.disablePrint()

		# Benchmark
		t0 = timer()

		# Clean
		self.sale_line.unlink()


		# Get - Only Sales - Not CN
		orders, count = mgt_funcs.get_orders_filter_fast_fast(self, self.date_begin, self.date_end)
		#print(orders)
		#print(count)

		for order in orders:
			#if order.state in ['credit_note']:
			#	print('Gotcha !')
			#	print(order.state)
			#	print()

			is_new = mkt_funcs.is_new_patient(self, order.patient, self.date_begin, self.date_end)

			#print(is_new)

			#if is_new:
			if is_new or order.patient.x_test:
				#print('Gotcha')
				#print(order.patient.name)

				# Loop
				for line in order.order_line:
					price_net = line.price_unit * line.product_uom_qty

					# Family Analysis
					if line.pl_price_list in ['2019']:
						family, subfamily, subsubfamily = mkt_funcs.pl_family_analysis(self, line)

					elif line.pl_price_list in ['2018']:
						family, subfamily, subsubfamily = mkt_funcs.pl_family_analysis_2018(self, line)


					# Using Getters - OO
					subsubfamily = line.product_id.get_subsubfamily()


					sale_line = self.sale_line.create({
															'date': order.date_order,
															'order': order.id,
															'patient': order.patient.id,
															'doctor': order.x_doctor.id,
															'product_id': line.product_id.id,
															'product_uom_qty': line.product_uom_qty,
															'price_unit': line.price_unit,
															'price_net': price_net,
															'family': family,
															'subfamily': subfamily,
															'subsubfamily': subsubfamily,
															'price_list': line.product_id.pl_price_list,
															'state': order.state,

															'marketing_id': self.id,
						})
					#print(sale_line)

		t1 = timer()
		self.delta_create_sale_lines = t1 - t0

		# Print Enable
		#test_funcs.enablePrint()

	# create_sale_lines





# ----------------------------------------------------------- Reset - Button ------------------------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset
		"""
		print()
		print('Reset')


		# Handle Exceptions
		mkt_exc.handle_exceptions(self)


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



# ----------------------------------------------------------- Second Level ---------------------------------------------

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




# ----------------------------------------------------------- Analyse Patient Lines ------------------------
	# Analyse patients
	@api.multi
	def analyse_patient_lines(self):
		"""
		Analyse patient Lines
		"""
		print()
		print('Pl - Analysis patient Lines')

		# Benchmark
		t0 = timer()


		# Clean
		self.vip_true = 0
		self.vip_false = 0


		# Loop
		for patient_line in self.patient_line:

			# Clean
			patient_line.clean() 		# OO


			# Lines
			patient = patient_line.patient
			#print(patient.name)
			model = 'price_list.marketing.order_line'
			lines = self.env[model].search([
													('state', 'in', ['sale', 'draft']),
													('patient', 'in', [patient.name]),
													('marketing_id', '=', self.id),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

			# Loop
			for line in lines:
				#print(line)
				#mkt_funcs.macro_line_analysis(self, line, patient_line)

				patient_line.analysis(line)  	# OO



		# Update Macros
		self.vip_false = self.total_count - (self.vip_true + self.vip_already_true)

		if self.total_count not in [0]:
			#self.vip_already_true_per = float(self.vip_already_true) / float(self.total_count)
			self.vip_true_per = float(self.vip_true) / float(self.total_count)
			self.vip_false_per = float(self.vip_false) / float(self.total_count)



		t1 = timer()
		self.delta_analyse_patient_lines = t1 - t0

	# analyse_patient_lines



# ----------------------------------------------------------- Analyse Sale Lines ------------------------
	# Update Sales
	@api.multi
	def analyse_sale_lines(self):
		"""
		Update Sale Lines
		"""
		print()
		print('Analysis Sale Lines')

		# Benchmark
		t0 = timer()


		model = 'price_list.marketing.order_line'


		# Count
		state = 'draft'
		count = self.env[model].search_count([
												('marketing_id', 'in', [self.id]),
												('state', 'in', [state]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		#print(count)
		self.sale_line_budget_count = count




		# Count
		state = 'sale'
		count = self.env[model].search_count([
												('marketing_id', 'in', [self.id]),
												('state', 'in', [state]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		#print(count)
		self.sale_line_sale_count = count



		# By Family
		family_list = ['consultation', 'procedure', 'product']
		state = 'sale'

		for family in family_list:

			count = self.env[model].search_count([
													('marketing_id', 'in', [self.id]),
													('family', 'in', [family]),
													('state', 'in', [state]),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
			#print(count)

			if family in ['consultation']:
				self.sale_line_consultation_count = count
			elif family in ['procedure']:
				self.sale_line_procedure_count = count
			elif family in ['product']:
				self.sale_line_product_count = count


		t1 = timer()
		self.delta_analyse_sale_lines = t1 - t0

	# analyse_sale_lines




# ----------------------------------------------------------- Update Stats ------------------------
	# Set Stats
	@api.multi
	def update_stats(self):
		"""
		Update Stats
		"""
		print()
		print('Pl - Update Stats')


		# Init

		# Collections
		country_arr = []


		# Loop
		for line in self.patient_line:

			# Line Analysis
			#mkt_funcs.pl_line_analysis(self, line)
			mkt_funcs.pl_patient_line_analysis(self, line)


			# Address - Using collections

			# Countries
			country_arr.append(line.country)




# Percentages

		# Sex
		if self.total_count != 0:
			#self.sex_male_per = (float(self.sex_male) / float(self.total_count))
			self.sex_male_per = (self.sex_male / float(self.total_count))
			self.sex_female_per = (self.sex_female / float(self.total_count))
			self.sex_undefined_per = (self.sex_undefined / float(self.total_count))

		#self.sex_male_per = mkt_funcs.get_per(self, self.sex_male, self.total_count)
		#self.sex_female_per = mkt_funcs.get_per(self, self.sex_female, self.total_count)
		#self.sex_undefined_per = mkt_funcs.get_per(self, self.sex_undefined, self.total_count)


		# Age
		if self.total_count != 0:
			self.age_mean = self.age_sum / float(self.total_count)
			self.age_undefined_per = (self.age_undefined / float(self.total_count))



		# First Contact
		self.how_none_per = mkt_funcs.get_per(self, self.how_none, self.total_count)
		self.how_reco_per = mkt_funcs.get_per(self, self.how_reco, self.total_count)
		self.how_tv_per = mkt_funcs.get_per(self, self.how_tv, self.total_count)
		self.how_radio_per = mkt_funcs.get_per(self, self.how_radio, self.total_count)
		self.how_inter_per = mkt_funcs.get_per(self, self.how_inter, self.total_count)
		self.how_web_per = mkt_funcs.get_per(self, self.how_web, self.total_count)
		self.how_mail_per = mkt_funcs.get_per(self, self.how_mail, self.total_count)
		self.how_u_per = mkt_funcs.get_per(self, self.how_u, self.total_count)

		# New
		self.how_facebook_per = mkt_funcs.get_per(self, self.how_facebook, self.total_count)
		self.how_instagram_per = mkt_funcs.get_per(self, self.how_instagram, self.total_count)
		self.how_callcenter_per = mkt_funcs.get_per(self, self.how_callcenter, self.total_count)
		self.how_old_patient_per = mkt_funcs.get_per(self, self.how_old_patient, self.total_count)


		# Education
		self.edu_fir_per = mkt_funcs.get_per(self, self.edu_fir, self.total_count)
		self.edu_sec_per = mkt_funcs.get_per(self, self.edu_sec, self.total_count)
		self.edu_tec_per = mkt_funcs.get_per(self, self.edu_tec, self.total_count)
		self.edu_uni_per = mkt_funcs.get_per(self, self.edu_uni, self.total_count)
		self.edu_mas_per = mkt_funcs.get_per(self, self.edu_mas, self.total_count)
		self.edu_u_per = mkt_funcs.get_per(self, self.edu_u, self.total_count)


		# Vip
		#self.vip_true_per = mkt_funcs.get_per(self, self.vip_true, self.total_count)
		#self.vip_false_per = mkt_funcs.get_per(self, self.vip_false, self.total_count)



		# Using collections
		# Country
		counter_country = collections.Counter(country_arr)

		# Country
		#print 'Create Country Line '
		for key in counter_country:
			count = counter_country[key]
			country = self.country_line.create({
													'name': key,
													'count': count,
													'marketing_id': self.id,
												})
			#print country
		#print self.country_line
		#print

	# update_stats




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
		print('Pl - Clean')
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
