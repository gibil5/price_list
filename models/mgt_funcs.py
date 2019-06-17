# -*- coding: utf-8 -*-
"""
	Mgt Funcs

	Created: 			28 May 2018
	Last mod: 			31 May 2019
"""
from __future__ import print_function
import datetime



# ----------------------------------------------------------- Line Analysis - PL -----------------------
def pl_line_analysis(self, line):
	"""
	New - 2019
	Analyses Line to update counters
	"""
	print()
	print('PL - Line Analysis')



	# Init
	prod = line.product_id

	print(prod.name)
	print(prod.pl_treatment)
	print(prod.pl_family)
	print(prod.pl_subfamily)

	#subfamily = prod.pl_subfamily


	# Services
	if prod.type in ['service']:
		self.nr_services = self.nr_services + line.product_uom_qty
		self.amo_services = self.amo_services + line.price_subtotal


		# Consultations
		#if prod.x_treatment in ['consultation']:
		if prod.pl_subfamily in ['consultation']:
			self.nr_consultations = self.nr_consultations + line.product_uom_qty
			self.amo_consultations = self.amo_consultations + line.price_subtotal

			if prod.pl_treatment in ['CONSULTA MEDICA']:
				self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
				self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal
				
			elif prod.pl_treatment in ['CONSULTA GINECOLOGICA']:
				self.nr_sub_con_gyn = self.nr_sub_con_gyn + line.product_uom_qty
				self.amo_sub_con_gyn = self.amo_sub_con_gyn + line.price_subtotal

			elif prod.pl_treatment in ['CONSULTA MEDICA DR. CHAVARRI']:
				self.nr_sub_con_cha = self.nr_sub_con_cha + line.product_uom_qty
				self.amo_sub_con_cha = self.amo_sub_con_cha + line.price_subtotal



		# Procedures
		else:
			self.nr_procedures = self.nr_procedures + line.product_uom_qty
			self.amo_procedures = self.amo_procedures + line.price_subtotal


			# By Family

			# Echo
			if prod.pl_family in ['echography']:
				self.nr_echo = self.nr_echo + line.product_uom_qty
				self.amo_echo = self.amo_echo + line.price_subtotal

			# Gyn
			elif prod.pl_family in ['gynecology']:
				self.nr_gyn = self.nr_gyn + line.product_uom_qty
				self.amo_gyn = self.amo_gyn + line.price_subtotal

			# Prom
			elif prod.pl_family in ['promotion']:
				self.nr_prom = self.nr_prom + line.product_uom_qty
				self.amo_prom = self.amo_prom + line.price_subtotal



			# By Sub Family

			# Co2
			#elif prod.pl_treatment in ['LASER CO2 FRACCIONAL']:
			elif prod.pl_subfamily in ['co2']:
				self.nr_co2 = self.nr_co2 + line.product_uom_qty
				self.amo_co2 = self.amo_co2 + line.price_subtotal

			# Exc
			#elif prod.pl_treatment in ['LASER EXCILITE']:
			elif prod.pl_subfamily in ['excilite']:
				self.nr_exc = self.nr_exc + line.product_uom_qty
				self.amo_exc = self.amo_exc + line.price_subtotal

			# Quick
			#elif prod.pl_treatment in ['QUICKLASER']:
			elif prod.pl_subfamily in ['quick']:
				self.nr_quick = self.nr_quick + line.product_uom_qty
				self.amo_quick = self.amo_quick + line.price_subtotal



			# By Treatment

			# Ipl
			elif prod.pl_treatment in ['LASER M22 IPL']:
				self.nr_ipl = self.nr_ipl + line.product_uom_qty
				self.amo_ipl = self.amo_ipl + line.price_subtotal

			# Ndyag
			elif prod.pl_treatment in ['LASER M22 ND YAG']:
				self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
				self.amo_ndyag = self.amo_ndyag + line.price_subtotal




			else:
				# Medical
				if prod.pl_family in ['medical']:
					self.nr_medical = self.nr_medical + line.product_uom_qty
					self.amo_medical = self.amo_medical + line.price_subtotal

				# Cosmeto
				elif prod.pl_family in ['cosmetology']:
					self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
					self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal


	# Products
	#else:
	elif prod.type in ['product']:
		self.nr_products = self.nr_products + line.product_uom_qty
		self.amo_products = self.amo_products + line.price_subtotal


		# Topical
		if prod.pl_family in ['topical']:
			self.nr_topical = self.nr_topical + line.product_uom_qty
			self.amo_topical = self.amo_topical + line.price_subtotal

		# Card
		elif prod.pl_family in ['card']:
			self.nr_card = self.nr_card + line.product_uom_qty
			self.amo_card = self.amo_card + line.price_subtotal

		# kit
		elif prod.pl_family in ['kit']:
			self.nr_kit = self.nr_kit + line.product_uom_qty
			self.amo_kit = self.amo_kit + line.price_subtotal



	# Consu
	elif prod.type in ['consu']:

		#print('Consu')

		self.nr_other = self.nr_other + line.product_uom_qty
		self.amo_other = self.amo_other + line.price_subtotal


		#if prod.x_family in ['credit_note']:
		#	self.nr_credit_notes = self.nr_credit_notes + line.product_uom_qty
		#	self.amo_credit_notes = self.amo_credit_notes + line.price_subtotal

	return False

# pl_line_analysis




# ----------------------------------------------------------- Line Analysis -----------------------
def line_analysis(self, line):
	"""
	Old - 2018
	Analyses Line to update counters
	"""
	#print()
	#print('Line Analysis')


	# Init
	prod = line.product_id


	# Services
	if prod.type in ['service']:
		self.nr_services = self.nr_services + line.product_uom_qty
		self.amo_services = self.amo_services + line.price_subtotal


		# Consultations
		if prod.x_treatment in ['consultation']:
			self.nr_consultations = self.nr_consultations + line.product_uom_qty
			self.amo_consultations = self.amo_consultations + line.price_subtotal

			self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
			self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal


		# Procedures
		else:
			self.nr_procedures = self.nr_procedures + line.product_uom_qty
			self.amo_procedures = self.amo_procedures + line.price_subtotal

			# Co2
			if prod.x_treatment in ['laser_co2']:
				self.nr_co2 = self.nr_co2 + line.product_uom_qty
				self.amo_co2 = self.amo_co2 + line.price_subtotal

			# Exc
			elif prod.x_treatment in ['laser_excilite']:
				self.nr_exc = self.nr_exc + line.product_uom_qty
				self.amo_exc = self.amo_exc + line.price_subtotal

			# Ipl
			elif prod.x_treatment in ['laser_ipl']:
				self.nr_ipl = self.nr_ipl + line.product_uom_qty
				self.amo_ipl = self.amo_ipl + line.price_subtotal

			# Ndyag
			elif prod.x_treatment in ['laser_ndyag']:
				self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
				self.amo_ndyag = self.amo_ndyag + line.price_subtotal

			# Quick
			elif prod.x_treatment in ['laser_quick']:
				self.nr_quick = self.nr_quick + line.product_uom_qty
				self.amo_quick = self.amo_quick + line.price_subtotal

			else:
				# Medical
				if prod.x_family in ['medical']:
					self.nr_medical = self.nr_medical + line.product_uom_qty
					self.amo_medical = self.amo_medical + line.price_subtotal

				# Cosmeto
				elif prod.x_family in ['cosmetology']:
					self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
					self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal


	# Products
	#else:
	elif prod.type in ['product']:
		self.nr_products = self.nr_products + line.product_uom_qty
		self.amo_products = self.amo_products + line.price_subtotal


		# Topical
		if prod.x_family in ['topical']:
			self.nr_topical = self.nr_topical + line.product_uom_qty
			self.amo_topical = self.amo_topical + line.price_subtotal

		# card
		elif prod.x_family in ['card']:
			self.nr_card = self.nr_card + line.product_uom_qty
			self.amo_card = self.amo_card + line.price_subtotal

		# kit
		elif prod.x_family in ['kit']:
			self.nr_kit = self.nr_kit + line.product_uom_qty
			self.amo_kit = self.amo_kit + line.price_subtotal



	# Consu
	elif prod.type in ['consu']:

		#print('Consu')

		self.nr_other = self.nr_other + line.product_uom_qty
		self.amo_other = self.amo_other + line.price_subtotal


		#if prod.x_family in ['credit_note']:
		#	self.nr_credit_notes = self.nr_credit_notes + line.product_uom_qty
		#	self.amo_credit_notes = self.amo_credit_notes + line.price_subtotal

	return False

# line_analysis







# ----------------------------------------------------------- Get Orders Fast -------------------
# States: In State Array
def get_orders_filter_fast(self, date_bx, date_ex):
	"""
	high level support for doing this and that.
	"""
	#print('')
	#print('Get Orders - Fast')


	# Init
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')



	# Orders
	orders = self.env['sale.order'].search([
													#('state', 'in', ['sale']),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													#('state', 'in', ['sale']),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_fast



# ---------------------------------------------- Get orders - Filter ------------------------------
# States: In State Array
def get_orders_filter(self, date_bx, date_ex, state_arr, type_arr):
	"""
	high level support for doing this and that.
	"""
	print('')
	print('Get Orders - Filter')
	print(date_bx)
	print(date_ex)
	print(state_arr)
	print(type_arr)


	# Init
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	_dic_states = {
					'sale,cancel,credit_note': 	['sale', 'cancel', 'credit_note'],
					'sale,cancel': 	['sale', 'cancel'],
					'sale': 		['sale'],
					'cancel': 		['cancel'],
	}


	_dic_types = {
					'ticket_receipt,ticket_invoice,receipt,invoice,sale_note,advertisement': ['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice', 'sale_note', 'advertisement'],


					'ticket_receipt,ticket_invoice': 	['ticket_receipt', 'ticket_invoice'],
					'ticket_receipt': 					['ticket_receipt'],
					'ticket_invoice': 					['ticket_invoice'],
					'ticket_receipt,ticket_invoice,receipt,invoice': \
																	['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice'],
	}



	if state_arr in _dic_states and type_arr in _dic_types:

		# Orders
		orders = self.env['sale.order'].search([
													('state', 'in', _dic_states[state_arr]),
													('x_type', 'in', _dic_types[type_arr]),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		count = self.env['sale.order'].search_count([
														('state', 'in', _dic_states[state_arr]),
														('x_type', 'in', _dic_types[type_arr]),
														('date_order', '>=', date_begin),
														('date_order', '<', date_end),
														('x_legacy', '=', False),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
	else:

		# Orders
		orders = self.env['sale.order'].search([
													('name', '=', 'This does note exist !'),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		count = 0



	return orders, count

# get_orders_filter




# ----------------------------------------------------------- Get Orders By Type ------------------

def get_orders_filter_type(self, date_bx, date_ex, x_type):
	"""
	high level support for doing this and that.
	"""

	# Dates
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	# Orders
	orders = self.env['sale.order'].search([
													('state', 'in', ['sale', 'cancel']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												order='x_counter_value asc',
												#limit=1,
											)

	# Count
	count = self.env['sale.order'].search_count([
													('state', 'in', ['sale', 'cancel']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

	return orders, count

# get_orders_filter_type






# ----------------------------------------------------------- Get orders - By Doctor --------------
# Provides sales between begin date and end date. Filters: by Doctor.
def get_orders_filter_by_doctor(self, date_bx, date_ex, doctor):
	"""
	Sales.
	Must include Credit Notes.
	"""
	#print()
	#print('PL - Get Orders Filter - By Doctor')


	# Init
	# Dates
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_begin = date_bx + ' 05:00:00'
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Prints
	#print date_end_dt


	# Search

	# Orders
	orders = self.env['sale.order'].search([
													#('state', '=', 'sale'),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_doctor', '=', doctor),
													('x_legacy', '=', False),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													#('state', '=', 'sale'),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_doctor', '=', doctor),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_by_doctor
