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
		print('Pl - Set Stats')


		# Init vars 

		# Sex 
		count_m = 0
		count_f = 0
		count_u = 0

		# Age 
		count_a = 0
		age_min = 100 
		age_max = 0 
		count_age_u = 0


		# First Contact 
		how_u = 0 
		how_none = 0 
		how_reco = 0 
		how_tv = 0
		how_radio = 0 
		how_inter = 0 
		how_web = 0 
		how_mail = 0 


		# Education 
		edu_u = 0
		edu_fir = 0
		edu_sec = 0
		edu_tec = 0
		edu_uni = 0
		edu_mas = 0


		# Vip 
		vip_true = 0 
		vip_false = 0 


		# Collections
		country_arr = []



		# Loop 
		for line in self.patient_line: 


			# Sex
			if line.sex == 'Male': 
				count_m = count_m + 1
			elif line.sex == 'Female': 
				count_f = count_f + 1
			else: 
				count_u = count_u + 1


			# Age Max and Min 
			if line.age_years not in[ -1, 0]: 			# Not an Error 
				count_a = count_a + line.age_years 
				if line.age_years > age_max: 
					age_max = line.age_years
				if line.age_years < age_min: 
					age_min = line.age_years
			else: 										# Error 
				count_age_u = count_age_u + 1


			# First Contact 
			if line.first_contact == 'none': 
				how_none = how_none + 1

			elif line.first_contact == 'recommendation': 
				how_reco = how_reco + 1

			elif line.first_contact == 'tv': 
				how_tv = how_tv + 1

			elif line.first_contact == 'radio': 
				how_radio = how_radio + 1

			elif line.first_contact == 'internet': 
				how_inter = how_inter + 1

			elif line.first_contact == 'website':
				how_web = how_web + 1

			elif line.first_contact == 'mail_campaign':
				how_mail = how_mail + 1

			else: 
				how_u = how_u + 1


			# Education 
			if line.education == 'first': 
				edu_fir = edu_fir + 1

			elif line.education == 'second': 
				edu_sec = edu_sec + 1

			elif line.education == 'technical': 
				edu_tec = edu_tec + 1

			elif line.education == 'university': 
				edu_uni = edu_uni + 1

			elif line.education == 'masterphd': 
				edu_mas = edu_mas + 1

			else: 
				edu_u = edu_u + 1


			# Vip 
			if line.vip: 
				vip_true = vip_true + 1

			else: 
				vip_false = vip_false + 1



			# Address - Using collections

			# Countries 
			country_arr.append(line.country)




		# Update Object 


		# Sex 
		# Absolutes 
		self.sex_male = count_m
		self.sex_female = count_f
		self.sex_undefined = count_u

		# Per
		#if self.total_count != 0: 
			#self.sex_male_per = ( float(self.sex_male) / float(self.total_count) ) * 100
			#self.sex_female_per = ( float(self.sex_female) / float(self.total_count) ) * 100
			#self.sex_undefined_per = ( float(self.sex_undefined) / float(self.total_count) ) * 100
		self.sex_male_per = mkt_funcs.get_per(self, self.sex_male, self.total_count)
		self.sex_female_per = mkt_funcs.get_per(self, self.sex_female, self.total_count)
		self.sex_undefined_per = mkt_funcs.get_per(self, self.sex_undefined, self.total_count)




		# Ages 
		self.age_min = age_min
		self.age_max = age_max
		self.age_undefined = count_age_u
		
		if self.total_count != 0: 
			self.age_mean = count_a / self.total_count
			self.age_undefined_per = ( float(self.age_undefined) / float(self.total_count) ) * 100


		# First Contact
		self.how_none = how_none
		self.how_reco = how_reco
		self.how_tv = how_tv
		self.how_radio = how_radio		
		self.how_inter = how_inter
		self.how_web = how_web
		self.how_mail = how_mail
		self.how_u = how_u

		# Per
		self.how_none_per = mkt_funcs.get_per(self, how_none, self.total_count)
		self.how_reco_per = mkt_funcs.get_per(self, how_reco, self.total_count)
		self.how_tv_per = mkt_funcs.get_per(self, how_tv, self.total_count)
		self.how_radio_per = mkt_funcs.get_per(self, how_radio, self.total_count)
		self.how_inter_per = mkt_funcs.get_per(self, how_inter, self.total_count)
		self.how_web_per = mkt_funcs.get_per(self, how_web, self.total_count)
		self.how_mail_per = mkt_funcs.get_per(self, how_mail, self.total_count)
		self.how_u_per = mkt_funcs.get_per(self, how_u, self.total_count)


		# Education 
		self.edu_fir = edu_fir
		self.edu_sec = edu_sec
		self.edu_tec = edu_tec
		self.edu_uni = edu_uni
		self.edu_mas = edu_mas
		self.edu_u = edu_u

		# Per 
		self.edu_fir_per = mkt_funcs.get_per(self, edu_fir, self.total_count)
		self.edu_sec_per = mkt_funcs.get_per(self, edu_sec, self.total_count)
		self.edu_tec_per = mkt_funcs.get_per(self, edu_tec, self.total_count)
		self.edu_uni_per = mkt_funcs.get_per(self, edu_uni, self.total_count)
		self.edu_mas_per = mkt_funcs.get_per(self, edu_mas, self.total_count)
		self.edu_u_per = mkt_funcs.get_per(self, edu_u, self.total_count)


		# Vip 
		self.vip_true = vip_true
		self.vip_false = vip_false

		 # Per 
		self.vip_true_per = mkt_funcs.get_per(self, vip_true, self.total_count)
		self.vip_false_per = mkt_funcs.get_per(self, vip_false, self.total_count)




		# Using collections		
		# Country
		counter_country = collections.Counter(country_arr)




		# Clear 
		self.country_line.unlink()
		self.city_line.unlink()
		self.district_line.unlink()



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




# ----------------------------------------------------------- Sex  ----------------------------------
	# Sex 
	sex_male_per = fields.Float(
			'M %',
			readonly=True, 
			digits=(16,1), 
		)

	sex_female_per = fields.Float(
			'F %',
			readonly=True, 
			digits=(16,1), 
		)

	sex_undefined_per = fields.Float(
			'Error %',
			readonly=True, 
			digits=(16,1), 
		)


# ----------------------------------------------------------- Education Level  ----------------------------------

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(16,1), 
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
			digits=(16,1), 
		)



	# New
	how_facebook = fields.Float(
			'Facebook',
			readonly=True, 
			digits=(16,1), 
		)

	how_instagram = fields.Float(
			'Instagram',
			readonly=True, 
			digits=(16,1), 
		)

	how_callcenter = fields.Float(
			'Callcenter',
			readonly=True, 
			digits=(16,1), 
		)

	how_old_patient = fields.Float(
			'Old_patient',
			readonly=True, 
			digits=(16,1), 
		)



	# New Per
	how_facebook_per = fields.Float(
			'Facebook %',
			readonly=True, 
			digits=(16,1), 
		)

	how_instagram_per = fields.Float(
			'Instagram %',
			readonly=True, 
			digits=(16,1), 
		)

	how_callcenter_per = fields.Float(
			'Callcenter %',
			readonly=True, 
			digits=(16,1), 
		)

	how_old_patient_per = fields.Float(
			'Old_patient %',
			readonly=True, 
			digits=(16,1), 
		)




	# Standard
	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True, 
			digits=(16,1), 
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True, 
			digits=(16,1), 
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True, 
			digits=(16,1), 
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True, 
			digits=(16,1), 
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True, 
			digits=(16,1), 
		)



	# Dep
	how_inter_per = fields.Float(
			'Internet %',
			readonly=True, 
			digits=(16,1), 
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True, 
			digits=(16,1), 
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




