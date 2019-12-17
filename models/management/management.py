# -*- coding: utf-8 -*-
"""
	Management Report - Object Oriented

	Only functions. Not the data model. 

	Created: 			28 May 2018
	Last updated: 		11 Dec 2019
"""

from __future__ import print_function
from timeit import default_timer as timer
#import collections
import datetime
from openerp import models, fields, api

# Lib

#from lib import pl_mgt_vars
#from lib import pl_ord_vars

from lib import mgt_funcs
from lib import mgt_line_funcs
from lib import prod_funcs
from lib import exc_mgt
from lib import stats

from . import stax

class Management(models.Model):
	"""
	Contains only functions. Not the data model. 

	Management Report. 
	Analyzes Sales and calculates several indicators like: Doctor performance,  Productivity, Daily Sales, by Doctor. 
	Extends Business Rules. Should NOT contain Data Model
	"""
	_inherit = 'openhealth.management'




# ----------------------------------------------------------- Class Vars -----------------------


	_dic_weekday = {
					0: 	'monday',
					1: 	'tuesday',
					2: 	'wednesday',
					3: 	'thursday',
					4: 	'friday',
					5: 	'saturday',
					6: 	'sunday',
	}

	_h_name = {
				# Families
				'gynecology': 		'Ginecologia',
				'echography': 		'Ecografia',
				'promotion': 		'Promocion',

				# 13 Jul 2018 
				'other': 		'Otro',

				'product': 		'Producto',
				'consultation': 'Consulta', 		
				'consultation_gyn': 'Consulta Ginecológica', 		
				'consultation_100': 'Consulta 100', 		
				'consultation_0': 'Consulta Gratuita', 		

				#'procedure': 	'Procedimiento', 		
				'procedure': 	'Procedimiento Laser', 		
				'laser': 		'Laser', 		

				'medical': 		'Tratamiento Médico', 		
				'cosmetology': 	'Cosmeatria', 	

				'card': 		'Tarjeta Vip', 	
				'kit': 			'Kits', 	
				'topical': 		'Cremas', 	




				# Subfamilies
				'laser_co2' : 		'Laser Co2', 		
				'laser_excilite' : 	'Laser Exc', 		
				'laser_ipl' : 		'Laser Ipl', 		
				'laser_ndyag' : 	'Laser Ndyag', 		
				'laser_quick' : 	'Quick Laser', 		

				'criosurgery' : 			'Criocirugía', 		
				'intravenous_vitamin' : 	'Vitamina Intravenosa', 		
				'botulinum_toxin' : 		'Toxina Botulínica', 		
				'hyaluronic_acid' : 		'Acido Hialurónico', 		

				'mesotherapy_nctf': 		'Mesoterapia NCTF', 
				'infiltration_scar': 		'Infiltración Cicatriz', 
				'infiltration_keloid': 		'Infiltración Queloide', 


				#False: False, 	
	}










# ----------------------------------------------------- Django Interface --------------------------

# ---------------------------------------------------------------------------------------------------------------------
# 																Productivity                       
# ---------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Prod -------------------------

	# 	# For Update Productivity
	#day_line = fields.One2many(
	#		'openhealth.management.day.line',
	#		'management_id',
	#	)



	# For Update Productivity
	productivity_day = fields.One2many(

			'productivity.day',

			'management_id',
		)



	# Update Productivity
	@api.multi
	def update_productivity(self):
		"""
		Update productivity
		Used also by Django
		"""
		print()
		print('X - Update Productivity')
		

		# Handle Exceptions - Dep !
		#exc_mgt.handle_exceptions(self)


		# Go
		prod_funcs.create_days(self)

		
		# Update cumulative and average
		prod_funcs.pl_update_day_cumulative(self)
		prod_funcs.pl_update_day_avg(self)

		print()


		return 1	# For Django
	# update_productivity




# ---------------------------------------------------------------------------------------------------------------------
# 																Daily                       
# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------- Update Daily -------------------------

	# Doctor
	#doctor_line = fields.One2many(
	#		'openhealth.management.doctor.line',
	#		'management_id',
	#	)

	
	# Doctor Day
	doctor_daily = fields.One2many(
	
			'doctor.daily',
	
			'management_id',
		)



	# Update Daily
	@api.multi
	def update_daily(self):
		"""
		Update daily sales for each doctor

		Used by Django. Last Test

		self.doctor_line
			'openhealth.management.doctor.line',
		"""
		print()
		print('X - Update Daily Sales')


		# Handle Exceptions - Dep !
		#exc_mgt.handle_exceptions(self)


		# For each doctor line
		for doctor in self.doctor_line:
			print(doctor.name)
			
			#doctor.update_daily() 	# Here !
			doctor.update_daily(self.id) 	# Here !


		print()


		# For Django
		self.date_test = datetime.datetime.now() 
		return 1	
	# update_daily







# ----------------------------------------------------------- First Level - Update Buttons ---------------------------------------------


# ----------------------------------------------------------- Update Fast ---------------------------------------------
	@api.multi
	def update_fast(self):
		"""
		Update Macros
		Used also by Django
		"""
		print()
		print('X - Update Fast')

		# Handle Exceptions
		exc_mgt.handle_exceptions(self)

		# Go
		t0 = timer()
		self.update_sales_fast()
		self.update_year()
		t1 = timer()
		self.delta_fast = t1 - t0
		#print self.delta_fast
		#print

		print()


		return 1 	# For Django
	# update_fast





# ---------------------------------------------------------------------------------------------------------------------
# 																Patients                       
# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------- Update Patients -------------------------
	# Update Patients
	@api.multi
	def update_patients(self):
		"""
		Update Patients. 
		"""
		print()
		print('X - Update Patients')


		# Handle Exceptions
		exc_mgt.handle_exceptions(self)


		# Go
		orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)
		#print(orders)
		#print(count)

		# Create
		for order in orders:

			patient = order.patient
			patient_id = order.patient.id


			#if patient.name not in ['REVILLA RONDON JOSE JAVIER']:
			
			if self.mode in ['test']  	or  	self.mode in ['normal'] and patient.name not in ['REVILLA RONDON JOSE JAVIER']:


				#print(patient)
				#print(patient_id)

				# Count
				pat_count = self.env['openhealth.management.patient.line'].search_count([
																						('patient', '=', patient_id),
																						('management_id', '=', self.id),
																				],
																					#order='x_serial_nr asc',
																					#limit=1,
																				)
				#print(pat_count)


				if pat_count in [0]:

					#self.report_sale_product = self.env['openhealth.report.sale.product'].create({
					patient_line = self.patient_line.create({
																'patient': patient_id,
																'management_id': self.id,
						})

		# Update
		for patient_line in self.patient_line:
			patient_line.update()


		print()


		return 1	# For Django
	# update_patients




# ---------------------------------------------------------------------------------------------------------------------
# 																Doctors                       
# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------- Update Doctors ----------------------
	@api.multi
	def update_doctors(self):
		"""
		Update Doctors
		"""
		print()
		print('X - Update Doctors')


		# Handle Exceptions
		exc_mgt.handle_exceptions(self)


		# Go
		t0 = timer()


		# Sales by Doctor
		self.pl_update_sales_by_doctor()


		# Stats
		#self.update_stats()
		stax.update_stats(self)


		t1 = timer()
		self.delta_doctor = t1 - t0


		print()


		return 1	# For Django
	# update_doctors



# ----------------------------------------------------------- Relational Extension -------------------------
	# patient
	patient_line = fields.One2many(
			'openhealth.management.patient.line',
			'management_id',
		)



# ----------------------------------------------------------- Second Level ---------------------------------------------

# ----------------------------------------------------------- Update Sales - Fast -----------------
	def update_sales_fast(self):
		"""
		Update Sales - Fast
		"""
		print()
		print('X - Update Sales Fast')


		# Init
		#self.statistics.initialize(self.name)
		#self.statistics = stats.Statistics(self.name)
		statistics = stats.Statistics(self.name)



		# Clean
		self.reset_macro()


		# Get Orders
		if self.type_arr in ['all']:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			orders, count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

		
# Loop
		tickets = 0

		for order in orders:
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:

				# Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					# Lines
					for line in order.order_line:

						# Line Analysis - Here !
						
						#if line.product_id.pl_price_list in ['2019']:			# Train Wreck of size 3 - Violates the LOD !
						if line.is_current_price_list():						# Respects the LOD !

							mgt_line_funcs.line_analysis_2019(self, line)

						else:
							mgt_line_funcs.line_analysis_2018(self, line)


					# Object Oriented - Stats
					#self.statistics.update(line)
					statistics.update(line)


				# Credit Note
				elif order.state in ['credit_note']:  									# CN - Do Amount Flow
					self.nr_credit_notes = self.nr_credit_notes + 1
					self.amo_credit_notes = self.amo_credit_notes + order.x_amount_flow



# Analysis - Setters
# Must be Abstract - To Hide Implementation

		# Set Averages
		mgt_funcs.set_averages(self)

		# Set Ratios
		mgt_funcs.set_ratios(self)

		# Set Totals
		mgt_funcs.set_totals(self, tickets)

		# Set Percentages
		mgt_funcs.set_percentages(self)



		# Object Oriented - Stats
		#statistics.set_stats()
		

		# Print
		#print(statistics)
		#print(statistics.name)
		#print(statistics.nr_products)
		#print(statistics.nr_consultations)
		#print(statistics.nr_procedures)
		
	# update_sales_fast




# ----------------------------------------------------------- Update Year -----------------------
	@api.multi
	def update_year(self):
		"""
		Update Year
		"""
		print()
		print('X - Update Year')

		# Mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		# Count
		count = self.env['openhealth.management'].search_count([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		#print(mgts)
		#print(count)

		total = 0		
		for mgt in mgts:
			total = total + mgt.total_amount

		self.total_amount_year = total

		if self.total_amount_year != 0:
			self.per_amo_total = self.total_amount / self.total_amount_year

	# update_year







# ----------------------------------------------------------- Validate Internal -------------------------
	# Validate
	@api.multi
	def validate(self):
		"""
		Validates the content. 
		For internal Data Coherency - internal and external. 
		"""
		print()
		print('X - Validate the content !')


		# Handle Exceptions
		exc_mgt.handle_exceptions(self)


		# Internal
		out = self.pl_validate_internal()


		# External
		#self.pl_validate_external()  	# Dep !


		# Django
		return out
	# validate




# ----------------------------------------------------------- Validate Internal -------------------------
	# Validate
	@api.multi
	def pl_validate_internal(self):
		"""
		Validates Data Coherency - internal. 
		"""
		print()
		print('X - Validate Internal')



		# Families
		self.per_amo_families = self.per_amo_products + self.per_amo_consultations + self.per_amo_procedures + self.per_amo_other + self.per_amo_credit_notes
		print(self.per_amo_families)

		# Sub Families
		self.per_amo_subfamilies = self.per_amo_sub_con_med + self.per_amo_sub_con_gyn + self.per_amo_sub_con_cha + \
									self.per_amo_co2 + self.per_amo_exc + self.per_amo_quick + self.per_amo_ipl + self.per_amo_ndyag + \
									self.per_amo_medical + self.per_amo_cosmetology + \
									self.per_amo_echo + self.per_amo_gyn + self.per_amo_prom + \
									self.per_amo_topical + self.per_amo_card + self.per_amo_kit + \
									self.per_amo_credit_notes
		print(self.per_amo_subfamilies)



		return self.per_amo_families, self.per_amo_subfamilies






# ----------------------------------------------------------- Validate external -------------------------
	# Validate
	@api.multi
	def pl_validate_external(self):
		"""
		Validates Data Coherency - External. 
		Builds a Report Sale Product for the month. 
		Compares it to Products stats.
		"""
		print()
		print('X - Validate External')

		if self.report_sale_product.name in [False]:

			date_begin = self.date_begin


			self.report_sale_product = self.env['openhealth.report.sale.product'].create({
																							'name': date_begin,
																							'management_id': self.id,
																						})

		rsp = self.report_sale_product
		print(rsp)
		print(rsp.name)


		rsp.update()

		self.rsp_count = rsp.total_qty
		self.rsp_total = rsp.total
		self.rsp_count_delta = self.nr_products - self.rsp_count
		self.rsp_total_delta = self.amo_products - self.rsp_total








# ----------------------------------------------------------- Update Sales - Fast -----------------
	# Create Timeline
	@api.multi
	def create_timeline(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Create Timeline')

		_dic_mo = {
					'01': 'ENE',
					'02': 'FEB',
					'03': 'MAR',
					'04': 'ABR',
					'05': 'MAY',
					'06': 'JUN',

					'07': 'JUL',
					'08': 'AGO',
					'09': 'SET',
					'10': 'OCT',
					'11': 'NOV',
					'12': 'DIC',
		}


		family_data = []
		subfamily_data = []

		months = []
		idxs = []

		amounts = []

		amounts_con = []
		amounts_prod = []
		amounts_proc = []

		amounts_co2 = []
		amounts_ipl = []
		amounts_exc = []
		amounts_ipl = []
		amounts_ndy = []
		amounts_qui = []
		amounts_med = []
		amounts_cos = []




		# mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
														],
														order='date_begin,name asc',
														#limit=1,
													)
		print(mgts)

		idx = 0
		for mgt in mgts:
			print(mgt.name)
			print(mgt.year)
			print(mgt.month)
			print()

			#months.append(mgt.month)
			months.append(_dic_mo[mgt.month])

			idxs.append(idx)
			idx = idx + 1

			amounts.append(mgt.total_amount)

			amounts_con.append(mgt.amo_consultations)
			amounts_proc.append(mgt.amo_procedures)
			amounts_prod.append(mgt.amo_products)

			amounts_co2.append(mgt.amo_co2)
			amounts_exc.append(mgt.amo_exc)
			amounts_ipl.append(mgt.amo_ipl)
			amounts_ndy.append(mgt.amo_ndyag)
			amounts_qui.append(mgt.amo_quick)
			amounts_med.append(mgt.amo_medical)
			amounts_cos.append(mgt.amo_cosmetology)





		print(amounts)
		print(len(amounts))
		print(months)
		print(len(months))
		print(idxs)
		print(len(idxs))



		# Common
		path = self.base_dir + 'img/chavarri/'


		# Totals
		name = 'All'
		fig_pie = 'mgt_amo_pie.png'
		fig_line = 'mgt_amo_line.png'
		mgt_amo_data = data_stats.Data(amounts, idxs, name, path, fig_pie, fig_line)
		#mgt_amo_data.get_graph()

		family_data.append(mgt_amo_data)
		subfamily_data.append(mgt_amo_data)


# Fams
		# Consultations
		name = 'Consultations'
		fig_pie = 'amo_con_pie.png'
		fig_line = 'amo_con_line.png'
		amo_con_data = data_stats.Data(amounts_con, idxs, name, path, fig_pie, fig_line)
		#amo_con_data.get_graph()

		family_data.append(amo_con_data)


		# Procedures
		name = 'Procedures'
		fig_pie = 'amo_proc_pie.png'
		fig_line = 'amo_proc_line.png'
		amo_proc_data = data_stats.Data(amounts_proc, idxs, name, path, fig_pie, fig_line)
		#amo_proc_data.get_graph()

		family_data.append(amo_proc_data)


		# Products
		name = 'Products'
		fig_pie = 'amo_prod_pie.png'
		fig_line = 'amo_prod_line.png'
		amo_prod_data = data_stats.Data(amounts_prod, idxs, name, path, fig_pie, fig_line)
		#amo_prod_data.get_graph()

		family_data.append(amo_prod_data)

		


# Subs
		# Co2
		name = 'Co2'
		fig_pie = 'amo_co2_pie.png'
		fig_line = 'amo_co2_line.png'
		amo_co2_data = data_stats.Data(amounts_co2, idxs, name, path, fig_pie, fig_line)
		#amo_co2_data.get_graph()

		subfamily_data.append(amo_co2_data)


		# qui
		name = 'Qui'
		fig_pie = 'amo_qui_pie.png'
		fig_line = 'amo_qui_line.png'
		amo_qui_data = data_stats.Data(amounts_qui, idxs, name, path, fig_pie, fig_line)
		#amo_qui_data.get_graph()

		subfamily_data.append(amo_qui_data)



		# exc
		name = 'Exc'
		fig_pie = 'amo_exc_pie.png'
		fig_line = 'amo_exc_line.png'
		amo_exc_data = data_stats.Data(amounts_exc, idxs, name, path, fig_pie, fig_line)
		#amo_exc_data.get_graph()

		subfamily_data.append(amo_exc_data)



		# ipl
		name = 'Ipl'
		fig_pie = 'amo_ipl_pie.png'
		fig_line = 'amo_ipl_line.png'
		amo_ipl_data = data_stats.Data(amounts_ipl, idxs, name, path, fig_pie, fig_line)
		#amo_ipl_data.get_graph()

		subfamily_data.append(amo_ipl_data)



		# ndy
		name = 'Ndy'
		fig_pie = 'amo_ndy_pie.png'
		fig_line = 'amo_ndy_line.png'
		amo_ndy_data = data_stats.Data(amounts_ndy, idxs, name, path, fig_pie, fig_line)
		#amo_ndy_data.get_graph()

		subfamily_data.append(amo_ndy_data)




		# med
		name = 'Med'
		fig_pie = 'amo_med_pie.png'
		fig_line = 'amo_med_line.png'
		amo_med_data = data_stats.Data(amounts_med, idxs, name, path, fig_pie, fig_line)
		#amo_med_data.get_graph()

		subfamily_data.append(amo_med_data)


		# cos
		name = 'Cos'
		fig_pie = 'amo_cos_pie.png'
		fig_line = 'amo_cos_line.png'
		amo_cos_data = data_stats.Data(amounts_cos, idxs, name, path, fig_pie, fig_line)
		#amo_cos_data.get_graph()

		subfamily_data.append(amo_cos_data)









		# All
		name = 'All'
		fig_pie = 'amo_fam_pie.png'
		fig_line = 'amo_fam_line.png'

		#all_amo_data = data_stats.DataSet(name, months, path, fig_pie, fig_line, family_data)
		all_fam_data = data_stats.DataSet(name, idxs, path, fig_pie, fig_line, family_data)
			
		all_fam_data.get_graph()



		# All
		name = 'Sub Families'
		fig_pie = 'amo_sub_pie.png'
		fig_line = 'amo_sub_line.png'

		#all_amo_data = data_stats.DataSet(name, months, path, fig_pie, fig_line, family_data)
		all_sub_data = data_stats.DataSet(name, idxs, path, fig_pie, fig_line, subfamily_data)
			
		all_sub_data.get_graph()








# ----------------------------------------------------------- Update Sales - By Doctor ------------

	def pl_update_sales_by_doctor(self):
		"""
		Pl - Update Sales
		"""
		print()
		print('X - Update Sales - By Doctor')


		# Clean - Important 
		self.doctor_line.unlink()


		# Init vars
		total_amount = 0
		total_count = 0
		total_tickets = 0



		# Doctors Inactive
		doctors_inactive = self.env['oeh.medical.physician'].search([
																	#('x_type', 'in', ['emr']),
																	('active', '=', False),
															],
															#order='date_begin,name asc',
															#limit=1,
													)
		#print(doctors_inactive)


		# Doctors Active
		doctors_active = self.env['oeh.medical.physician'].search([
																	#('x_type', 'in', ['emr']),
																	('active', '=', True),
															],
															#order='date_begin,name asc',
															#limit=1,
													)
		#print(doctors_active)



		doctors = doctors_inactive + doctors_active
		#print(doctors)


		# Create Sales - By Doctor - All 
		for doctor in doctors:
			#print(doctor.name)
			#print(doctor.active)

			# Clear
			#doctor.order_line.unlink()

			# Orders
			# Must include Credit Notes
			orders, count = mgt_funcs.get_orders_filter_by_doctor(self, self.date_begin, self.date_end, doctor.name)
			#print(orders)
			#print(count)


			if count in [0]:
				#print()
				jx = 5
			else:
				#print('Gotcha')
				self.create_doctor_data(doctor.name, orders)

			#print()


	# update_sales_by_doctor




# ----------------------------------------------------------- Create Doctor Data ------------
	def create_doctor_data(self, doctor_name, orders):
		print()
		print('X - Create Doctor Data')


		# Init Loop
		amount = 0
		count = 0
		tickets = 0
		doctor = self.doctor_line.create({
											'name': doctor_name,
											'management_id': self.id,
										})

		# Loop
		for order in orders:

			# Tickets
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:


				# Parse Data


				# Amount with State
				if order.state in ['credit_note']:
					amount = amount + order.x_amount_flow

				elif order.state in ['sale']:
					amount = amount + order.amount_total


				# Id Doc
				if order.x_type in ['ticket_invoice', 'invoice']:
					receptor = order.patient.x_firm.upper()
					id_doc = order.patient.x_ruc
					id_doc_type = 'ruc'
					id_doc_type_code = '6'
				else:
					receptor = order.patient.name
					id_doc = order.patient.x_id_doc
					id_doc_type = order.patient.x_id_doc_type
					id_doc_type_code = order.patient.x_id_doc_type_code

					# Pre-Electronic
					if id_doc_type is False or id_doc is False:
						id_doc = order.patient.x_dni
						id_doc_type = 'dni'
						id_doc_type_code = '1'






				# State equal to Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					#print('SALE')

					# Order Lines
					for line in order.order_line:

						count = count + 1

						# Price
						price_unit = line.price_unit						



						# Families
						family = line.product_id.get_family()
						sub_family = line.product_id.get_subsubfamily()



						# Create
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,

																# Line
																'product_id': 			line.product_id.id,
																'product_uom_qty': 		line.product_uom_qty,

																# Price
																'price_unit': 			price_unit,

																# Families
																'family': family, 
																'sub_family': sub_family, 
															})

						#print(line)
						#print(line.product_id)
						#print(line.product_id.name)


						# Deprecated !
						# Update Families
						#if line.product_id.pl_price_list in ['2019']:
						#	order_line.pl_update_fields()

						#elif line.product_id.pl_price_list in ['2018']:
						#	order_line.update_fields()



					# Line Analysis Sale - End

				# Conditional State Sale - End




				# State equal to Credit Note
				elif order.state in ['credit_note']:

					#print('CREDIT NOTE')


					# Order Lines
					for line in order.order_line:

						# Families
						family = line.product_id.get_family()
						sub_family = line.product_id.get_subsubfamily()


						# Price
						price_unit = order.x_amount_flow

						# Create
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,

																# Line
																'product_uom_qty': 		1,

																# Price
																'price_unit': 			price_unit,


																# Families
																'family': family, 
																'sub_family': sub_family, 
															})


						#print(line)
						#print(line.product_id)
						#print(line.product_id.name)



						# Deprecated !
						#if line.product_id.pl_price_list in ['2019']:
						#	order_line.pl_update_fields()

						#elif line.product_id.pl_price_list in ['2018']:
						#	order_line.update_fields()



					# Line Analysis Credit Note - End

				# Conditional State - End


			# Filter Block - End
		# Loop - End



		# Stats
		doctor.amount = amount
		doctor.x_count = count

		# Percentage
		if self.total_amount != 0: 
			doctor.per_amo = (doctor.amount / self.total_amount)

	# create_doctor_data





# ----------------------------------------------------------- Update Max -----------------------
	@api.multi
	def update_max(self):
		"""
		Update Year All
		"""
		print()
		print('X - Update Max')

		# Clear
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		for mgt in mgts:
			#print(mgt.name)
			mgt.pl_max = False
			mgt.pl_min = False


		# Max
		mgt = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount asc',
														limit=1,
													)
		mgt.pl_min = True


		# Max
		mgt = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount desc',
														limit=1,
													)
		mgt.pl_max = True



# ----------------------------------------------------------- Update Year all -----------------------
	@api.multi
	def update_year_all(self):
		"""
		Update Year All
		"""
		print()
		print('X - Update Year All')


		# Mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		# Count
		count = self.env['openhealth.management'].search_count([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
															#order='x_serial_nr asc',
															#limit=1,
														)
		print(mgts)
		print(count)


		for mgt in mgts:
			print(mgt.name)
			mgt.update_year()





# ----------------------------------------------------------- Reset -------------------------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset Button.
		"""
		#print()
		print('X - Reset')

		# Handle Exceptions
		#exc_mgt.handle_exceptions(self)

		# Go
		self.reset_macro()

		#self.reset_micro()
		self.reset_relationals()
	# reset




# ----------------------------------------------------------- Reset -------------------------
	# Reset Macros
	def reset_macro(self):
		"""
		Reset Macro
		All self fields
		"""
		print()
		print('X - Reset Macros')


		# Deltas
		self.delta_fast = 0
		self.delta_doctor = 0


		# Relational
		if self.patient_line not in [False]:
			self.patient_line.unlink()


		#self.report_sale_product = False
		self.report_sale_product.unlink()
		self.rsp_count = 0
		self.rsp_count_delta = 0
		self.rsp_total = 0
		self.rsp_total_delta = 0

		# Clear
		self.total_amount_year = 0

		self.total_amount = 0
		self.total_count = 0
		self.total_tickets = 0


		# Nr - 1st level
		self.nr_products = 0
		self.nr_services = 0
		self.nr_consultations = 0
		self.nr_procedures = 0

		# Nr - 2nd level
		self.nr_topical = 0
		self.nr_card = 0
		self.nr_kit = 0
		self.nr_co2 = 0
		self.nr_exc = 0
		self.nr_ipl = 0
		self.nr_ndyag = 0
		self.nr_quick = 0
		self.nr_medical = 0
		self.nr_cosmetology = 0
		self.nr_echo = 0
		self.nr_gyn = 0
		self.nr_prom = 0
		self.nr_credit_notes = 0
		self.nr_other = 0
		self.nr_sub_con_med = 0
		self.nr_sub_con_gyn = 0
		self.nr_sub_con_cha = 0


		# Amo - 1st Level
		self.amo_products = 0
		self.amo_services = 0
		self.amo_consultations = 0
		self.amo_procedures = 0
		self.amo_credit_notes = 0
		self.amo_other = 0

		# Amo - 2nd Level
		self.amo_topical = 0
		self.amo_card = 0
		self.amo_kit = 0
		self.amo_co2 = 0
		self.amo_exc = 0
		self.amo_ipl = 0
		self.amo_ndyag = 0
		self.amo_quick = 0
		self.amo_medical = 0
		self.amo_cosmetology = 0
		self.amo_echo = 0
		self.amo_gyn = 0
		self.amo_prom = 0
		self.amo_sub_con_med = 0
		self.amo_sub_con_gyn = 0
		self.amo_sub_con_cha = 0



		# Per Amo
		self.per_amo_total = 0
		self.per_amo_families = 0
		self.per_amo_subfamilies = 0

		self.per_amo_sub_con_med = 0
		self.per_amo_sub_con_gyn = 0
		self.per_amo_sub_con_cha = 0

		self.per_amo_echo = 0
		self.per_amo_gyn = 0
		self.per_amo_prom = 0

		self.per_amo_other = 0
		self.per_amo_credit_notes = 0
		self.per_amo_topical = 0
		self.per_amo_card = 0
		self.per_amo_kit = 0
		self.per_amo_products = 0
		self.per_amo_services = 0
		self.per_amo_consultations = 0
		self.per_amo_procedures = 0
		self.per_amo_co2 = 0
		self.per_amo_exc = 0
		self.per_amo_ipl = 0
		self.per_amo_ndyag = 0
		self.per_amo_quick = 0
		self.per_amo_medical = 0
		self.per_amo_cosmetology = 0

		# Avg
		self.avg_echo = 0
		self.avg_gyn = 0
		self.avg_prom = 0

		self.avg_other = 0
		self.avg_topical = 0
		self.avg_kit = 0
		self.avg_card = 0
		self.avg_products = 0
		self.avg_services = 0
		self.avg_consultations = 0
		self.avg_procedures = 0
		self.avg_co2 = 0
		self.avg_exc = 0
		self.avg_ipl = 0
		self.avg_ndyag = 0
		self.avg_quick = 0
		self.avg_medical = 0
		self.avg_cosmetology = 0

		# Ratios
		self.ratio_pro_con = 0
	# reset_macro





	# Reset Relationals
	def reset_relationals(self):
		"""
		Reset Micro

		All Relational
			Doctors, Families, Sub-families
		"""
		print()
		print('X - Reset Micros')
		


		# Productivity Days
		self.productivity_day.unlink()



		# Productivity days 
		#productivity_days = self.env['productivity.day'].search([
		#															('management_id', '=', self.id),
		#													],
															#order='date_begin,name asc',
															#limit=1,
		#											)
		#print(productivity_days)
		#print(doctors_inactive)






		# Order Lines
		self.order_line.unlink()


		# Doctor lines
		self.doctor_line.unlink()


		# Family lines
		self.family_line.unlink()
		self.sub_family_line.unlink()

	# reset_micro



