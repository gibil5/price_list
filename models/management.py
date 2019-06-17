# -*- coding: utf-8 -*-
"""
	Management Report
	Created: 			28 May 2018
	Last updated: 		 2 Jun 2019
"""
from __future__ import print_function
from timeit import default_timer as timer
import collections
import datetime
from openerp import models, fields, api
#from openerp.addons.openhealth.models.management import mgt_funcs
from . import mgt_funcs
from . import pl_mgt_vars
#from . import data_stats
from . import pl_ord_vars

class Management(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.management'



# ----------------------------------------------------------- Natives -------------------------
	per_amo_credit_notes = fields.Float(
		)


	# Medical
	nr_sub_con_med = fields.Integer(
			'Nr Cons Med',
		)

	amo_sub_con_med = fields.Float(
			'Monto Cons Med',
		)
	
	per_amo_sub_con_med = fields.Float(
			'% Monto Cons Med',
		)

	# Gyn
	nr_sub_con_gyn = fields.Integer(
			'Nr Cons Gin',
		)

	amo_sub_con_gyn = fields.Float(
			'Monto Cons Gin',
		)
	
	per_amo_sub_con_gyn = fields.Float(
			'% Monto Cons Gin',
		)

	# Chavarri
	nr_sub_con_cha = fields.Integer(
			'Nr Cons Dr. Chav',
		)

	amo_sub_con_cha = fields.Float(
			'Monto Cons Dr. Chav',
		)
	
	per_amo_sub_con_cha = fields.Float(
			'% Monto Sub Cons Dr. Chav',
		)






	per_amo_families = fields.Float(
			'% Monto Familias',
		)

	per_amo_subfamilies = fields.Float(
			'% Monto Sub Familias',
		)

	per_amo_subfamilies_products = fields.Float(
			'% Monto Sub Familias Productos',
		)

	per_amo_subfamilies_procedures = fields.Float(
			'% Monto Sub Familias Procedimientos',
		)



# ----------------------------------------------------------- Validate -------------------------
	# Validate
	@api.multi
	def pl_validate(self):
		"""
		Validates Data for internal coherency and external coherency. 
		"""
		print()
		print('Pl - Validate')

		# Families
		self.per_amo_families = self.per_amo_products + self.per_amo_consultations + self.per_amo_procedures + self.per_amo_other + self.per_amo_credit_notes

		# Sub Families
		self.per_amo_subfamilies = self.per_amo_sub_con_med + self.per_amo_sub_con_gyn + self.per_amo_sub_con_cha + \
									self.per_amo_co2 + self.per_amo_exc + self.per_amo_quick + self.per_amo_ipl + self.per_amo_ndyag + \
									self.per_amo_medical + self.per_amo_cosmetology + \
									self.per_amo_echo + self.per_amo_gyn + self.per_amo_prom + \
									self.per_amo_topical + self.per_amo_card + self.per_amo_kit + \
									self.per_amo_credit_notes


		#self.per_amo_subfamilies_products = self.per_amo_topical + self.per_amo_card + self.per_amo_kit

		#self.per_amo_subfamilies_procedures = self.per_amo_co2 + self.per_amo_exc + self.per_amo_quick + self.per_amo_ipl + self.per_amo_ndyag + \
		#							self.per_amo_medical + self.per_amo_cosmetology + \
		#							self.per_amo_echo + self.per_amo_gyn + self.per_amo_prom 



# ----------------------------------------------------------- Update Prod -------------------------
	# Update Days
	@api.multi
	#def update_productivity(self):
	def pl_update_productivity(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Update Productivity')
		
		self.pl_create_days()
		print(self.day_line)

		self.update_day_cumulative()
		
		self.update_day_avg()




# ----------------------------------------------------------- Create Days -------------------------
	# Create Days
	@api.multi
	def pl_create_days(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Create Days')


		# Clean
		self.day_line.unlink()


		# Holidays
		days_inactive = []
		if self.configurator.name not in [False]:
			for day in self.configurator.day_line:
				if day.holiday:
					days_inactive.append(day.date)
		#print(days_inactive)


		# Create
		#date_format = "%Y-%m-%d %H:%M:%S"
		date_format = "%Y-%m-%d"
		date_end_dt = datetime.datetime.strptime(self.date_end, date_format)
		date_begin_dt = datetime.datetime.strptime(self.date_begin, date_format)
		delta = date_end_dt - date_begin_dt
		print(delta)


		# Create
		for i in range(delta.days + 1):
			
			print(i)

			date_dt = date_begin_dt + datetime.timedelta(i)
			weekday = date_dt.weekday()

			#weekday_str = ord_vars._dic_weekday[weekday]
			weekday_str = pl_ord_vars._dic_weekday[weekday]
			
			#print(date_dt, weekday)


			# Duration
			if weekday in [5]:
				duration = 0.5
			else:
				duration = 1


			# Not Sunday
			if weekday in [0, 1, 2, 3, 4, 5]:


				#date_date = date_dt.split()[0]
				#date_date = date_dt.day
				#date_date = date_dt.date
				date_s = date_dt.strftime(date_format)
				
				#print(date_s)


				if date_s not in days_inactive:

					# Create
					day = self.day_line.create({
												'date': date_dt,
												'name': weekday_str,
												'weekday': weekday_str,
												'duration': duration,
												'management_id': self.id,
									})


					day.update_amount()		# Important !

					print(day)

					#print(date_dt, weekday, weekday_str)
					#print(date_dt)
					#print(date_s)
			else:
				print('Sunday, not counted')

	# create_days



# ----------------------------------------------------------- Natives ----------------------

	# New Procedures

	# Echography
	nr_echo = fields.Integer(
			'Nr Ecografia',
		)
	amo_echo = fields.Float(
			'Monto Ecografia',
		)
	per_amo_echo = fields.Float(
			'% Monto Ecografia',
		)
	avg_echo = fields.Float(
			'Precio Prom. Ecografia',
		)


	# Gynecology
	nr_gyn = fields.Integer(
			'Nr Ginecologia',
		)
	amo_gyn = fields.Float(
			'Monto Ginecologia',
		)
	per_amo_gyn = fields.Float(
			'% Monto Ginecologia',
		)
	avg_gyn = fields.Float(
			'Precio Prom. Ginecologia',
		)


	# Promotions
	nr_prom = fields.Integer(
			'Nr Promocion',
		)
	amo_prom = fields.Float(
			'Monto Promocion',
		)
	per_amo_prom = fields.Float(
			'% Monto Promocion',
		)
	avg_prom = fields.Float(
			'Precio Prom. Promocion',
		)



	# Time Line
	base_dir = fields.Char()



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





# ----------------------------------------------------------- Update Sales - Fast -----------------
	# Update Sales - Fast
	def update_sales_fast(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('PL - Update Sales Fast')


		# Clean
		self.reset_macro()


		# Get Orders
		if self.type_arr in ['all']:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			orders, count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)
		#print orders
		#print count



# Loop
		# Init
		tickets = 0
		for order in orders:
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:


				# Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					# Lines
					for line in order.order_line:

						# Line Analysis
						if line.product_id.pl_price_list in ['2019']:
							mgt_funcs.pl_line_analysis(self, line)

						else:
							mgt_funcs.line_analysis(self, line)


				# Credit Note
				elif order.state in ['credit_note']:  									# CN - Do Amount Flow
					self.nr_credit_notes = self.nr_credit_notes + 1
					self.amo_credit_notes = self.amo_credit_notes + order.x_amount_flow


# Analysis

		# Averages

		# Families
		if self.nr_other != 0:
			self.avg_other = self.amo_other / self.nr_other

		if self.nr_products != 0:
			self.avg_products = self.amo_products / self.nr_products

		if self.nr_services != 0:
			self.avg_services = self.amo_services / self.nr_services

		if self.nr_consultations != 0:
			self.avg_consultations = self.amo_consultations / self.nr_consultations

		if self.nr_procedures != 0:
			self.avg_procedures = self.amo_procedures / self.nr_procedures


		# Subfamilies
		if self.nr_topical != 0:
			self.avg_topical = self.amo_topical / self.nr_topical

		if self.nr_card != 0:
			self.avg_card = self.amo_card / self.nr_card

		if self.nr_kit != 0:
			self.avg_kit = self.amo_kit / self.nr_kit

		if self.nr_co2 != 0:
			self.avg_co2 = self.amo_co2 / self.nr_co2

		if self.nr_exc != 0:
			self.avg_exc = self.amo_exc / self.nr_exc

		if self.nr_ipl != 0:
			self.avg_ipl = self.amo_ipl / self.nr_ipl

		if self.nr_ndyag != 0:
			self.avg_ndyag = self.amo_ndyag / self.nr_ndyag

		if self.nr_quick != 0:
			self.avg_quick = self.amo_quick / self.nr_quick

		if self.nr_medical != 0:
			self.avg_medical = self.amo_medical / self.nr_medical

		if self.nr_cosmetology != 0:
			self.avg_cosmetology = self.amo_cosmetology / self.nr_cosmetology


		if self.nr_echo != 0:
			self.avg_echo = self.amo_echo / self.nr_echo

		if self.nr_gyn != 0:
			self.avg_gyn = self.amo_gyn / self.nr_gyn

		if self.nr_prom != 0:
			self.avg_prom = self.amo_prom / self.nr_prom





		# Ratios
		if self.nr_consultations != 0:
			#self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations))




		# Totals
		#self.total_amount = self.amo_products + self.amo_services + self.amo_other - self.amo_credit_notes
		self.total_amount = self.amo_products + self.amo_services + self.amo_other + self.amo_credit_notes
		
		self.total_count = self.nr_products + self.nr_services
		self.total_tickets = tickets




		# Percentages

		# Year - Dep !!!
		#if self.total_amount_year != 0:
		#		self.per_amo_total = self.total_amount / self.total_amount_year


		# Month
		if self.total_amount != 0:

			self.per_amo_other = (self.amo_other / self.total_amount)


			# Families
			self.per_amo_credit_notes = (self.amo_credit_notes / self.total_amount)

			self.per_amo_products = (self.amo_products / self.total_amount)
			self.per_amo_consultations = (self.amo_consultations / self.total_amount)
			self.per_amo_procedures = (self.amo_procedures / self.total_amount)


			# Sub Families
			self.per_amo_sub_con_med = (self.amo_sub_con_med / self.total_amount)
			self.per_amo_sub_con_gyn = (self.amo_sub_con_gyn / self.total_amount)
			self.per_amo_sub_con_cha = (self.amo_sub_con_cha / self.total_amount)


			self.per_amo_echo = (self.amo_echo / self.total_amount)
			self.per_amo_gyn = (self.amo_gyn / self.total_amount)
			self.per_amo_prom = (self.amo_prom / self.total_amount)

			self.per_amo_topical = (self.amo_topical / self.total_amount)
			self.per_amo_card = (self.amo_card / self.total_amount)
			self.per_amo_kit = (self.amo_kit / self.total_amount)

			self.per_amo_co2 = (self.amo_co2 / self.total_amount)
			self.per_amo_exc = (self.amo_exc / self.total_amount)
			self.per_amo_ipl = (self.amo_ipl / self.total_amount)
			self.per_amo_ndyag = (self.amo_ndyag / self.total_amount)
			self.per_amo_quick = (self.amo_quick / self.total_amount)

			self.per_amo_medical = (self.amo_medical / self.total_amount)
			self.per_amo_cosmetology = (self.amo_cosmetology / self.total_amount)

	# update_sales_fast




# ----------------------------------------------------------- Update Fast -----------------------
	@api.multi
	def update_fast(self):
		"""
		Update Button
		"""
		print()
		print('Pl - Update Fast')
		t0 = timer()

		self.update_sales_fast()
		
		self.update_year()

		t1 = timer()
		self.delta_fast = t1 - t0
		#print self.delta_fast
		#print
	# update


# ----------------------------------------------------------- Update Doctors ----------------------
	@api.multi
	def pl_update_doctors(self):
		"""
		Pl - Update Doctors
		"""
		print()
		print('Pl - Update Doctors')
		t0 = timer()


		self.pl_update_sales_by_doctor()


		#self.update_stats()
		self.pl_update_stats()


		t1 = timer()

		self.delta_doctor = t1 - t0
	# update_doctors



# ----------------------------------------------------------- Update Stats ------------------------

	#def update_stats(self):
	def pl_update_stats(self):
		"""
		Update Stats - Doctors, Families, Sub-families
		"""
		print()
		print('Pl - Update Stats')


		# Using collections - More Abstract !


		# Clean
		self.family_line.unlink()
		self.sub_family_line.unlink()


		# Init
		family_arr = []
		sub_family_arr = []
		_h_amount = {}
		_h_sub = {}


	# All
		# Loop - Doctors
		for doctor in self.doctor_line:

			# Loop - Order Lines
			for line in doctor.order_line:

				# Family
				family_arr.append(line.family)

				# Sub family
				sub_family_arr.append(line.sub_family)

				# Amount - Family
				if line.family in _h_amount:
					_h_amount[line.family] = _h_amount[line.family] + line.price_total

				else:
					_h_amount[line.family] = line.price_total

				# Amount - Sub Family
				if line.sub_family in _h_sub:
					_h_sub[line.sub_family] = _h_sub[line.sub_family] + line.price_total

				else:
					_h_sub[line.sub_family] = line.price_total



			# Doctor Stats
			print('mark 0')
			#doctor.stats()
			doctor.pl_stats()
			print('mark 1')



	# By Family

		# Count
		counter_family = collections.Counter(family_arr)

		# Create
		for key in counter_family:
			count = counter_family[key]
			amount = _h_amount[key]
			family = self.family_line.create({
													'name': key,
													'x_count': count,
													'amount': amount,
													'management_id': self.id,
												})
			family.update()

			# Percentage
			if self.total_amount != 0:
				family.per_amo = family.amount / self.total_amount



	# Subfamily

		# Count
		counter_sub_family = collections.Counter(sub_family_arr)

		# Create
		for key in counter_sub_family:
			count = counter_sub_family[key]
			amount = _h_sub[key]
			sub_family = self.sub_family_line.create({
														'name': key,
														'x_count': count,
														'amount': amount,
														'management_id': self.id,
												})
			sub_family.update()

			# Percentage
			if self.total_amount != 0:
				sub_family.per_amo = sub_family.amount / self.total_amount

	# update_stats




# ----------------------------------------------------------- Update Sales - By Doctor ------------

	def pl_update_sales_by_doctor(self):
		"""
		Pl - Update Sales
		"""
		print()
		print('Pl - Update Sales - By Doctor')


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


		# Create Sales - By Doctor
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
		#print()
		print('Create Doctor Data')


		# Loop
		doctor = self.doctor_line.create({
											'name': doctor_name,
											'management_id': self.id,
										})

		# Init Loop
		amount = 0
		count = 0
		tickets = 0


		# Loop
		for order in orders:

			# Tickets
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:


				# Parse Data

				# Amount
				#amount = amount + order.amount_total

				# Amount with State
				if order.state in ['credit_note']:
					#amount = amount - order.amount_total
					#amount = amount - order.amount_total
					#amount = amount - order.x_credit_note_amount
					amount = amount + order.x_amount_flow
					#print('Gotcha !')
					#print(amount)

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




				# Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					# Order Lines
					for line in order.order_line:

						count = count + 1

						# State
						#if order.state in ['credit_note']:
						#	price_unit = -line.price_unit
						#elif order.state in ['sale']:
						#	price_unit = line.price_unit
						
						# Price
						price_unit = line.price_unit						


						# Here !!!
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
															})
						#print('mark 0')

						if line.product_id.pl_price_list in ['2019']:
							order_line.pl_update_fields()

						elif line.product_id.pl_price_list in ['2018']:
							order_line.update_fields()

						#print('mark 1')

					# Line Analysis - End
				# Conditional State Sale - End



				# Credit Note
				elif order.state in ['credit_note']:

					# Price
					price_unit = order.x_amount_flow

					# Here !!!
					#jx
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
															#'product_id': 			product_id.id,
															'product_uom_qty': 		1,

															# Price
															'price_unit': 			price_unit,
														})

					#order_line.update_fields()
					#order_line.pl_update_fields()
					if line.product_id.pl_price_list in ['2019']:
						order_line.pl_update_fields()

					elif line.product_id.pl_price_list in ['2018']:
						order_line.update_fields()

				# Conditional State CN - End
			# Filter Block - End
		# Loop - End



		# Stats
		#print('mark 10')
		doctor.amount = amount
		doctor.x_count = count
		# Percentage
		if self.total_amount != 0: 
			doctor.per_amo = (doctor.amount / self.total_amount)

	# create_doctor_data




# ----------------------------------------------------------- Natives ----------------------
	pl_max = fields.Boolean(
			'Max',
		)

	pl_min = fields.Boolean(
			'Min',
		)

# ----------------------------------------------------------- Relational ----------------------
	# Doctor
	doctor_line = fields.One2many(
			'openhealth.management.doctor.line',
			'management_id',
		)

# ----------------------------------------------------------- Update Max -----------------------
	@api.multi
	def update_max(self):
		"""
		Update Year All
		"""
		print()
		print('Pl - Update Max')

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
		#print()
		#print('Pl - Update Year All')

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



# ----------------------------------------------------------- Update Year -----------------------
	@api.multi
	def update_year(self):
		"""
		Update Year
		"""
		#print()
		#print('Pl - Update Year')


		# Mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															#('year', 'in', ['2019']),
															('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		# Count
		count = self.env['openhealth.management'].search_count([
															('owner', 'in', ['month']),
															#('year', 'in', ['2019']),
															('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

		#print(mgts)
		#print(count)

		total = 0
		
		for mgt in mgts:
			#print(mgt.name)
			#print(mgt.total_amount)
			total = total + mgt.total_amount

		self.total_amount_year = total

		if self.total_amount_year != 0:
			self.per_amo_total = self.total_amount / self.total_amount_year

	# update_year




# ----------------------------------------------------------- Natives ----------------------
	# Owner
	owner = fields.Selection(
			[
				('aggregate', 'Aggregate'),

				('month', 'Month'),
				('year', 'Year'),
				('account', 'Account'),
			],
			default='month',
			required=True,
		)

	month = fields.Selection(

			#selection=ord_vars._month_order_list,
			selection=pl_mgt_vars._month_order_list,
		
			string='Mes',
			required=True,
		)


# ----------------------------------------------------------- Update Daily -------------------------
	# Update Daily
	@api.multi
	def update_daily(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update daily')
		for doctor in self.doctor_line:
			doctor.update_daily()




	# Reset Macros
	def reset_macro(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Reset Macros'

		# Clear
		self.total_amount_year = 0

		self.total_amount = 0
		self.total_count = 0
		self.total_tickets = 0

		# Nr
		self.nr_sub_con_med = 0
		self.nr_sub_con_gyn = 0
		self.nr_sub_con_cha = 0

		self.nr_echo = 0
		self.nr_gyn = 0
		self.nr_prom = 0

		self.nr_credit_notes = 0
		self.nr_other = 0
		self.nr_products = 0
		self.nr_services = 0
		self.nr_consultations = 0
		self.nr_procedures = 0
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

		# Amo
		self.amo_sub_con_med = 0
		self.amo_sub_con_gyn = 0
		self.amo_sub_con_cha = 0

		self.amo_echo = 0
		self.amo_gyn = 0
		self.amo_prom = 0

		self.per_amo_total = 0
		self.amo_credit_notes = 0
		self.amo_other = 0
		self.amo_products = 0
		self.amo_services = 0
		self.amo_consultations = 0
		self.amo_procedures = 0
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

		# Per Amo
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

