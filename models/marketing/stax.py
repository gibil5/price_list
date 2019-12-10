# -*- coding: utf-8 -*-
"""
	Stax Library

 	Created: 				10 Dec 2019
 	Last up: 	 			10 Dec 2019
"""

from timeit import default_timer as timer
import collections

from openerp import models, fields, api
from openerp.addons.price_list.models.management.lib import mgt_funcs

from . import exc_mkt
from . import mkt_funcs



# ----------------------------------------------------------- Second Level ---------------------------------------------

# ----------------------------------------------------------- Update Stats ------------------------
# Set Stats
@api.multi
def update_stats(self):
	"""
	Update Stats
	"""
	print()
	print('X - Update Stats')


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



# ----------------------------------------------------------- Update Vip Sales --------------------
@api.multi
def update_vip_sales(self):  
	print()
	print('X - Vip Sales')

	# Patient Lines 
	for pl in self.patient_line: 

		if pl.vip: 
			
			# Clean 
			pl.order_line.unlink()
			pl.order_line_vip.unlink()

			# Orders 
			orders = self.env['sale.order'].search([
														('state', '=', 'sale'),
														('patient', '=', pl.patient.name),
												],
													order='date_order asc',
													#limit=1,
											)

			# Find Vip Date - First Method 
			for order in orders: 
				for ol in order.order_line: 
					if ol.product_id.default_code == '495': 		# Vip Card 
						pl.vip_date = order.date_order


			# Find Vip Date - Second Method - Legacy 
			if pl.vip_date == False:
				card = self.env['openhealth.card'].search([
																('patient_name', '=', pl.patient.name),
													],
														#order='x_serial_nr asc',
														limit=1,
												)
				pl.vip_date = card.create_date


			# Order Lines - Create Order Line 
			for order in orders: 

				# Create Vip 
				for ol in order.order_line:
					pl_ol = pl.order_line.create({
													'name': ol.name, 
													'product_id': ol.product_id.id, 
													'x_date_created': order.date_order, 
													'product_uom_qty': ol.product_uom_qty, 
													'price_unit': ol.price_unit, 
													'patient_line_id': pl.id, 
						})
					#print pl_ol



					# Create - Vip sale 
					if pl.vip_date != False: 
						if order.date_order >= pl.vip_date and ol.product_id.type in ['service']: 

							pl_ol_vip = pl.order_line_vip.create({
																	'name': ol.name, 
																	'product_id': ol.product_id.id, 
																	'x_date_created': order.date_order, 
																	'product_uom_qty': ol.product_uom_qty, 
																	'price_unit': ol.price_unit, 
																	'patient_line_id_vip': pl.id, 
								})
							#print pl_ol

			pl.update_fields_vip()

# update_vip_sales







# ----------------------------------------------------------- Create Sale Lines - Button Hidden ------------------------
# Create Sales
@api.multi
def create_sale_lines(self):
	"""
	Create Sale Lines
	"""
	print()
	print('X - Create Sale Lines')

	# Handle Exceptions
	exc_mkt.handle_exceptions(self)


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




# ----------------------------------------------------------- Analyse Patient Lines ------------------------
# Analyse patients
@api.multi
def analyse_patient_lines(self):
	"""
	Analyse patient Lines
	"""
	print()
	print('X - Analysis patient Lines')

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
	print('X - Analysis Sale Lines')

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


