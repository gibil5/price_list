# 13 Dec 2019

#from openerp.addons.openhealth.models.order import ord_vars

#from timeit import default_timer as timer
#import collections
#from openerp.addons.price_list.models.management.lib import mgt_funcs
#from openerp.addons.price_list.models.lib import test_funcs



	# Update Patients
	@api.multi
	def update_patients(self):

		# Handle Exceptions - Dep
		#exc_mkt.handle_exceptions(self)


		# QC - Start
		#t0 = timer()
		#now_0 = datetime.datetime.now()

		# QC - Stop
		#t1 = timer()
		#now_1 = datetime.datetime.now()
		#self.delta_patients = t1 - t0




	# Update Sales
	@api.multi
	def update_sales(self):

		# Print Disable
		#test_funcs.disablePrint()

		# Init 
		#self.delta_create_sale_lines = 0
		#self.delta_analyse_sale_lines = 0
		#self.delta_analyse_patient_lines = 0

		# Handle Exceptions
		#exc_mkt.handle_exceptions(self)



		# Benchmark
		#self.delta_sales_pl = self.delta_create_sale_lines + self.delta_analyse_sale_lines + self.delta_analyse_patient_lines


		# Print Enable
		#test_funcs.enablePrint()








# 11 Dec 2019

# ----------------------------------------------------- Django Interface --------------------------

	@api.multi
	def set_state(self, state):
		"""
		Django interface
		so_model.set_state(state)
		"""
		print()
		print('Set State')
		self.state = state



	@api.multi
	def get_name(self):
		"""
		Django interface
		"""
		print()
		print('Get name')
		return self.name



	@api.multi
	def get_date_begin(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_begin


	@api.multi
	def get_date_end(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_end


	@api.multi
	def get_date_test(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_test




	#@api.multi
	#def get_total(self):
	#	"""
	#	Django interface
	#	"""
	#	print()
	#	print('Get total')
	#	if self.total not in [False]:
	#		return self.total
	#	else:
	#		return 0



	@api.multi
	def get_count(self):
		"""
		Django interface
		"""
		print()
		print('Get count')
		if self.total_count not in [False]:
			return self.total_count
		else:
			return 0



	@api.multi
	def get_state(self):
		"""
		Django interface
		"""
		print()
		print('Get state')
		return self.state










		_dic  = {
					'consultation': 	self.sale_line_consultation_count,
					'procedure': 		self.sale_line_procedure_count,
					'product': 			self.sale_line_product_count,

		}
			#_dic[family] = count








		# Count
		count = self.env[model].search_count([
												('marketing_id', 'in', [self.id]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(count)
		self.sale_line_sale_count = count


		# Count
		family = 'consultation'
		count = self.env[model].search_count([
												('marketing_id', 'in', [self.id]),
												('family', 'in', [family]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(count)
		self.sale_line_consultation_count = count


		# Count
		family = 'procedure'
		count = self.env[model].search_count([
												('marketing_id', 'in', [self.id]),
												('family', 'in', [family]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(count)
		self.sale_line_procedure_count = count


		# Count
		family = 'product'
		count = self.env[model].search_count([
												('marketing_id', 'in', [self.id]),
												('family', 'in', [family]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(count)
		self.sale_line_product_count = count













					# Family
					if line.product_id.type in ['product']:
						family = 'product'
						subfamily = line.product_id.pl_family
						subsubfamily = line.product_id.pl_subfamily

					elif line.product_id.type in ['service']:

						if line.product_id.pl_subfamily in ['consultation']:
							#family = line.product_id.pl_subfamily
							family = 'consultation'
							subfamily = 'consultation'
							subsubfamily = 'consultation'

						else:
							family = 'procedure'
							subfamily = line.product_id.pl_family
							subsubfamily = line.product_id.pl_subfamily













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



			# Sex
			#if line.sex == 'Male': 
			#	count_m = count_m + 1
			#elif line.sex == 'Female': 
			#	count_f = count_f + 1
			#else: 
			#	count_u = count_u + 1

			# Age Max and Min 
			#if line.age_years not in[ -1, 0]: 			# Not an Error 
			#	count_a = count_a + line.age_years 
			#	if line.age_years > age_max: 
			#		age_max = line.age_years
			#	if line.age_years < age_min: 
			#		age_min = line.age_years
			#else: 										# Error 
			#	count_age_u = count_age_u + 1



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

		# Sex 
		# Absolutes 
		#self.sex_male = count_m
		#self.sex_female = count_f
		#self.sex_undefined = count_u


		#self.age_min = age_min
		#self.age_max = age_max
		#self.age_undefined = count_age_u


		# First Contact
		self.how_none = how_none
		self.how_reco = how_reco
		self.how_tv = how_tv
		self.how_radio = how_radio		
		self.how_inter = how_inter
		self.how_web = how_web
		self.how_mail = how_mail
		self.how_u = how_u



		# Education 
		self.edu_fir = edu_fir
		self.edu_sec = edu_sec
		self.edu_tec = edu_tec
		self.edu_uni = edu_uni
		self.edu_mas = edu_mas
		self.edu_u = edu_u




		# Vip 
		self.vip_true = vip_true
		self.vip_false = vip_false


		# Clear 
		#self.country_line.unlink()
		#self.city_line.unlink()
		#self.district_line.unlink()
