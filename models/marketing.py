# -*- coding: utf-8 -*-
"""
 	Report Marketing
 
 	Created: 				19 May 2018
 	Last up: 	 			27 Nov 2018
"""
from __future__ import print_function
import datetime
from timeit import default_timer as timer
import collections
from openerp import models, fields, api

from . import mkt_funcs
#from . import lib_marketing
#from openerp.addons.openhealth.models.marketing import mkt_funcs, lib_marketing
from openerp.addons.openhealth.models.marketing import lib_marketing


from openerp.addons.openhealth.models.order import ord_vars

class Marketing(models.Model):

	_inherit = 'openhealth.marketing'



# ----------------------------------------------------------- Natives ----------------------
	owner = fields.Selection(
			[
				('week', 'Week'),
				('month', 'Month'),
				('year', 'Year'),
			],
			required=True,
		)



# ----------------------------------------------------------- Update Patients ---------------------
	# Update Patients
	@api.multi
	def update_patients(self):  
		#print()
		print('Pl - Update Patients')


		# QC
		t0 = timer()
		now_0 = datetime.datetime.now()


		# Clear
		#self.patient_line.unlink()
		self.reset()


		# Get Patients 
		mode = 'normal'
		patients,count = mkt_funcs.get_patients_filter(self, self.date_begin, self.date_end, mode)

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

														'marketing_id': self.id, 
													})
			ret = pat_line.update_fields()



		# Set Stats 
		self.update_stats()


		# Update Vip Sales 
		self.update_vip_sales()



		# Build Histo
		lib_marketing.build_histogram(self)

		# Build Media
		lib_marketing.build_media(self)

		# Build Places
		lib_marketing.build_districts(self)
		lib_marketing.build_cities(self)



		t1 = timer()
		now_1 = datetime.datetime.now()
		self.delta_patients = t1 - t0

	# update_patients




# ----------------------------------------------------------- Update Stats ------------------------
	# Set Stats
	@api.multi
	def update_stats(self):  
		print()
		print('Pl - Update Stats')


		# Init 

		# Collections
		country_arr = []



		# Loop 
		for line in self.patient_line: 

			# Line Analysis
			mkt_funcs.pl_line_analysis(self, line)


			# Address - Using collections

			# Countries 
			country_arr.append(line.country)




# Percentages 

		# Sex
		if self.total_count != 0: 
			#self.sex_male_per = ( float(self.sex_male) / float(self.total_count) ) 
			self.sex_male_per = ( self.sex_male / float(self.total_count) ) 
			self.sex_female_per = ( self.sex_female / float(self.total_count) ) 
			self.sex_undefined_per = ( self.sex_undefined / float(self.total_count) ) 
		
		#self.sex_male_per = mkt_funcs.get_per(self, self.sex_male, self.total_count)
		#self.sex_female_per = mkt_funcs.get_per(self, self.sex_female, self.total_count)
		#self.sex_undefined_per = mkt_funcs.get_per(self, self.sex_undefined, self.total_count)


		# Age
		if self.total_count != 0: 
			self.age_mean = self.age_sum / float(self.total_count)
			self.age_undefined_per = ( self.age_undefined / float(self.total_count) ) 



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
		self.vip_true_per = mkt_funcs.get_per(self, self.vip_true, self.total_count)
		self.vip_false_per = mkt_funcs.get_per(self, self.vip_false, self.total_count)



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







# ----------------------------------------------------------- Update Sales ------------------------
	# Update Sales
	@api.multi
	def update_sales(self):  
		print()
		print('Pl - Update Sales')

		# QC
		t0 = timer()

		# Clean Macros 
		self.patient_budget_count = 0 
		self.patient_sale_count = 0 
		self.patient_consu_count = 0 
		self.patient_proc_count = 0 


		# Loop - Patient Lines 
		for pat_line in self.patient_line: 

			# Update Line
			pat_line.update_fields_mkt()




			# Budgets
			budgets = self.env['sale.order'].search([
															('state', '=', 'draft'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)

			# Clean 
			pat_line.budget_line.unlink()


			# Create
			for budget in budgets:

				doctor = budget.x_doctor

				for line in budget.order_line: 
					
					if True: 

						# Budgets 
						budget_line = pat_line.budget_line.create({
																	'name': line.name,
																	'doctor': doctor.id,
																	'product_id': line.product_id.id, 
																	'x_date_created': budget.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit,
																	'patient_line_budget_id': pat_line.id, 
																	'marketing_id': self.id,
							})

			# Count
			self.patient_budget_count = self.patient_budget_count + len(pat_line.budget_line)


			# Update Nrs
			pat_line.update_nrs()





			# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)

			# Clean 
			pat_line.sale_line.unlink()
			pat_line.consu_line.unlink()
			pat_line.procedure_line.unlink()


			# Create
			for order in orders: 

				doctor = order.x_doctor

				for line in order.order_line: 
					
					prod = line.product_id

					# Sale
					sale_line = pat_line.sale_line.create({
															'name': line.name,
															'doctor': doctor.id,
															'product_id': line.product_id.id,
															'x_date_created': order.date_order,
															'product_uom_qty': line.product_uom_qty,
															'price_unit': line.price_unit,
															'patient_line_sale_id': pat_line.id, 
															'marketing_id': self.id, 
						})



					# Consultation
					#if prod.x_family in ['consultation']:
					#if prod.pl_subfamily in ['consultation']:
					if prod.pl_subfamily in ['consultation'] or prod.x_family in ['consultation']:
						consu_line = pat_line.consu_line.create({
																	'name': line.name, 
																	'product_id': line.product_id.id, 
																	'x_date_created': order.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit, 
																	'patient_line_consu_id': pat_line.id, 
																	'marketing_id': self.id, 
																})


					# Procedure
					#if 	(prod.type not in ['product'])   and   (prod.x_family not in ['consultation']):
					#if 	(prod.type not in ['product']) and (prod.pl_subfamily not in ['consultation']):
					#if 	(prod.type not in ['product']) and (prod.pl_subfamily not in ['consultation']) or (prod.type not in ['product']) and (prod.x_family not in ['consultation']):
					if 	(prod.pl_family in ['laser', 'cosmetology', 'medical', 'echography', 'gynecology']) 		or 		(prod.type not in ['product']) and (prod.x_family not in ['consultation', False]):
						procedure_line = pat_line.procedure_line.create({
																			'name': line.name, 
																			'product_id': line.product_id.id, 
																			'x_date_created': order.date_order, 
																			'product_uom_qty': line.product_uom_qty, 
																			'price_unit': line.price_unit, 
																			'patient_line_proc_id': pat_line.id, 
																			'marketing_id': self.id, 
																		})


			# Update Counts
			self.patient_sale_count = self.patient_sale_count + len(pat_line.sale_line)
			self.patient_consu_count = self.patient_consu_count + len(pat_line.consu_line)
			self.patient_proc_count = self.patient_proc_count + len(pat_line.procedure_line)

			# Update Nrs
			pat_line.update_nrs()


		# QC
		t1 = timer()
		self.delta_sales = t1 - t0

	# update_sales



# ----------------------------------------------------------- QC ----------------------------------

	year = fields.Selection(

			selection=ord_vars._year_order_list,
		
			string='Año',
			#default='2019',
			required=True,
		)

	month = fields.Selection(

			selection=ord_vars._month_order_list,
		
			string='Mes',
			#required=True,
		)


# ----------------------------------------------------------- Age  ----------------------------------
	# Age
	age_mean = fields.Float(
			'Edad Promedio',
			readonly=True,
			#digits=(16,1),
			digits = (12,3),
		)

	age_sum = fields.Float(
			#'Edad Promedio',
			#readonly=True,
			digits = (12,3),
		)



# ----------------------------------------------------------- Sex  ----------------------------------

	# Sex
	#sex_male = fields.Float(
	sex_male = fields.Integer(
			'Sexo M',
			readonly=True, 
		)

	#sex_female = fields.Float(
	sex_female = fields.Integer(
			'Sexo F',
			readonly=True, 
		)

	#sex_undefined = fields.Float(
	sex_undefined = fields.Integer(
			'Sexo Error',
			readonly=True, 	
		)



	# Sex 
	sex_male_per = fields.Float(
			'M %',
			readonly=True, 
			#digits=(16,1), 
			digits = (12,3),
			#digits=(12,1),
			#digits=(12,2),
		)

	sex_female_per = fields.Float(
			'F %',
			readonly=True, 
			#digits=(16,1), 
			digits = (12,3),
		)

	sex_undefined_per = fields.Float(
			'Error %',
			readonly=True, 
			#digits=(16,1), 
			digits = (12,3),
		)


# ----------------------------------------------------------- Education Level  ----------------------------------

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True, 
			digits=(12,3), 
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True, 
			digits=(12,3), 
		)

	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True, 
			digits=(12,3), 
		)

	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True, 
			digits=(12,3), 
		)
	
	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True, 
			digits=(12,3), 
		)

	edu_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(12,3), 
		)

# ----------------------------------------------------------- First Contact ----------------------------------


# From Patient
#_first_contact_list = [
#						('facebook','Facebook'), 					# New
#						('instagram','Instagram'), 					# New
#						('callcenter','Call Center'), 				# New 
#						('old_patient','Paciente Antiguo'), 		# New 		

#						('recommendation','Recomendación'), 
#						('tv','Tv'), 
#						('radio','Radio'), 		
#						('website','Web'), 
#						('mail_campaign','Mailing'), 


#						('internet','Internet'), 	# Dep
#						('none','Ninguno'), 		# Dep
#]



	# First Contact 
	how_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(12,3), 
		)



	# New
	#how_facebook = fields.Float(
	how_facebook = fields.Integer(
			'Facebook',
			readonly=True, 
			#digits=(12,3), 
		)

	#how_instagram = fields.Float(
	how_instagram = fields.Integer(
			'Instagram',
			readonly=True, 
			#digits=(12,3), 
		)

	#how_callcenter = fields.Float(
	how_callcenter = fields.Integer(
			'Call center',
			readonly=True, 
			#digits=(12,3), 
		)

	#how_old_patient = fields.Float(
	how_old_patient = fields.Integer(
			'Paciente Antiguo',
			readonly=True, 
			#digits=(12,3), 
		)



	# New Per
	how_facebook_per = fields.Float(
			'Facebook %',
			readonly=True, 
			digits=(12,3), 
		)

	how_instagram_per = fields.Float(
			'Instagram %',
			readonly=True, 
			digits=(12,3), 
		)

	how_callcenter_per = fields.Float(
			'Callcenter %',
			readonly=True, 
			digits=(12,3), 
		)

	how_old_patient_per = fields.Float(
			#'Old_patient %',
			'Paciente Antiguo %',
			readonly=True, 
			digits=(12,3), 
		)




	# Standard
	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True, 
			digits=(12,3), 
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True, 
			digits=(12,3), 
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True, 
			digits=(12,3), 
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True, 
			digits=(12,3), 
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True, 
			digits=(12,3), 
		)



	# Dep
	how_inter_per = fields.Float(
			'Internet %',
			readonly=True, 
			digits=(12,3), 
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True, 
			digits=(12,3), 
		)



# ----------------------------------------------------------- Reset ------------------------------
	# Reset
	@api.multi
	def reset(self):  
		print('Pl - Reset')

		self.patient_sale_count = 0
		self.patient_consu_count = 0
		self.patient_proc_count = 0
		self.patient_budget_count = 0

		self.total_count = 0
		self.patient_reco_count = 0

		self.patient_line.unlink()
		self.histo_line.unlink()
		self.media_line.unlink()
		self.district_line.unlink()
		self.country_line.unlink()
		self.city_line.unlink()


		# First Contact 

		# New
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
		self.vip_true = 0
		self.vip_false = 0

		self.vip_true_per = 0
		self.vip_false_per = 0



