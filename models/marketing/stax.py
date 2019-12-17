# -*- coding: utf-8 -*-
"""
	Stax Library

	Separate BL from Structure

	Used by
		Marketing

	Uses
		mkt_funcs

	- Update Stats
	- Update Vip Sales
	- Create Sale Lines
	- Analyse patient Lines
	- Analyse Sale Lines

 	Created: 				10 Dec 2019
 	Last up: 	 			12 Dec 2019
"""

from timeit import default_timer as timer
import collections
from openerp import models, fields, api

#from openerp.addons.price_list.models.management.lib import mgt_funcs  # Dep


from openerp.addons.price_list.models.patient.patient import Patient

from . import exc_mkt

from . import mkt_funcs


# ----------------------------------------------------------- Update Counters ------------------------
# Set Stats
@api.multi
def update_counters(self):
	"""
	Create Macro Stats
		Education
		First Contact

	"""
	print()
	print('X - Update Counters')


	# Loop - For all Patients
	for line in self.patient_line:

		# First Contact
		#self.first_contact.analyse(line)


		# Origin
		self.origin.analyse(line)


		# Education
		self.education.analyse(line)


		# Sex
		self.sex.analyse(line)


		# Age
		self.age.analyse(line)


		# Vip
		self.vip.analyse(line)


		# Line Analysis - Dep !
		#mkt_funcs.pl_patient_line_analysis(self, line)

# update_counters





# ----------------------------------------------------------- Update Vip Sales --------------------
@api.multi
def update_vip_sales(self):  
	"""
	Update Vip Sales
	"""
	#print()
	#print('X - Vip Sales')

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
	#print()
	#print('X - Create Sale Lines')


	# Clean
	self.sale_line.unlink()


	# Get - Only Sales - Not CN
	orders, count = mkt_funcs.get_orders_filter_no_cn(self, self.date_begin, self.date_end)
	#print(orders, count)


	for order in orders:

		# The patient has been created this month
		
		#is_new = mkt_funcs.is_new_patient(self, order.patient, self.date_begin, self.date_end)
		is_new = Patient.is_new_patient(self, order.patient, self.date_begin, self.date_end)
		
		#print(is_new)


		if is_new or order.patient.x_test:

			# Loop
			for line in order.order_line:
				price_net = line.price_unit * line.product_uom_qty



				# Family Analysis - Dep
				#if line.pl_price_list in ['2019']:
				#	family, subfamily, subsubfamily = mkt_funcs.pl_family_analysis(self, line)
				#elif line.pl_price_list in ['2018']:
				#	family, subfamily, subsubfamily = mkt_funcs.pl_family_analysis_2018(self, line)



				# Uses Product method
				family, subfamily, subsubfamily = line.product_id.get_families_for_mkt()


				# Using Getters - OO - Redundance ?
				subsubfamily = line.product_id.get_subsubfamily()



				# Create Sale Line
				sale_line = self.sale_line.create({
														'product_id': line.product_id.id,

														'date': order.date_order,
														'order': order.id,
														'patient': order.patient.id,
														'doctor': order.x_doctor.id,


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
# create_sale_lines




# ----------------------------------------------------------- Analyse Patient Lines ------------------------
# Analyse patients
@api.multi
def analyse_patient_lines(self):
	"""
	Analyse patient Lines
	"""
	#print()
	#print('X - Analysis patient Lines')

	# Benchmark
	t0 = timer()



	# Clean
	#self.vip_true = 0
	#self.vip_false = 0



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
			#patient_line.analysis(line)  	# OO
			patient_line.counters_update(line)  	# OO







	# Update Macros - Dep
	#self.vip_false = self.total_count - (self.vip_true + self.vip_already_true)
	#if self.total_count not in [0]:
	#	self.vip_true_per = float(self.vip_true) / float(self.total_count)
	#	self.vip_false_per = float(self.vip_false) / float(self.total_count)




	t1 = timer()
	self.delta_analyse_patient_lines = t1 - t0

# analyse_patient_lines





# ----------------------------------------------------------- Analyse Sale Lines ------------------------
# Update Sales
@api.multi
def analyse_sale_lines(self):
	"""
	Analyse Sale Lines
	"""
	#print()
	#print('X - Analysis Sale Lines')

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


