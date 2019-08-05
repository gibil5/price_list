

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



		#pl_lib_marketing.pl_build_media(self)



# ----------------------------------------------------------- Update Sales - Dep ------------------------
	# Update Sales
	@api.multi
	def update_sales(self):
		"""
		Update Sales
		"""
		print()
		print('Update Sales')

		# QC
		t0 = timer()

		# Clean Macros
		self.patient_budget_count = 0
		self.patient_sale_count = 0
		self.patient_consu_count = 0
		self.patient_proc_count = 0
		self.patient_product_count = 0


		self.price_list_2019_count = 0
		self.price_list_2018_count = 0

		# Init
		#self.vip_true = self.vip_already_true
		self.vip_false = self.vip_already_false
		self.vip_true = 0
		#self.vip_false = 0



		# Loop - Patient Lines
		for pat_line in self.patient_line:

			# Update Line
			pat_line.update_fields_mkt()


# Budgets
			# Search
			#budgets = self.env['sale.order'].search([
			#												('state', '=', 'draft'),
			#												('patient', '=', pat_line.patient.name),
			#										],
			#											order='date_order asc',
			#											#limit=1,
			#									)

			# By Library
			budgets, count = mgt_funcs.get_orders_filter_fast_patient_draft(self, self.date_begin, self.date_end, pat_line.patient.name)


			# Clean
			pat_line.budget_line.unlink()

			# Create Budgets
			for budget in budgets:
				doctor = budget.x_doctor
				for line in budget.order_line:
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





# Sales
			# Search - DEP - Not Date Restrictions. Over calculates
			#orders = self.env['sale.order'].search([
			#												('state', '=', 'sale'),
			#												('patient', '=', pat_line.patient.name),
			#										],
			#											order='date_order asc',
			#											#limit=1,
			#									)


			# Get - Only Sales - Not CN
			orders, count = mgt_funcs.get_orders_filter_fast_patient(self, self.date_begin, self.date_end, pat_line.patient.name)
			#print(orders)
			#print(count)




			# Clean
			pat_line.sale_line.unlink()
			pat_line.consu_line.unlink()
			pat_line.procedure_line.unlink()


			# Create
			for order in orders:

				doctor = order.x_doctor

				for line in order.order_line:


					# Line Analysis
					mkt_funcs.line_analysis(self, line)



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



					# Consultation Lines
					# 2018
					#if prod.x_family in ['consultation']:

					# 2019
					#if prod.pl_subfamily in ['consultation']:

					# 2019 and 2018
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


					# Procedure Lines

					# 2018
					#if 	(prod.type not in ['product'])   and   (prod.x_family not in ['consultation']):

					# 2019
					#if 	(prod.pl_subfamily in ['co2', 'excilite', 'm22', 'quick', 'echography', 'gynecology', 'medical', 'cosmetology',  ]):
					#if 	(prod.pl_subfamily in ['co2', 'excilite', 'm22', 'quick', 'echography', 'gynecology', 'medical', 'cosmetology', 'promotion', ]):

					# 2019 and 2018
					if 	(prod.pl_subfamily in ['co2', 'excilite', 'm22', 'quick', 'echography', 'gynecology', 'medical', 'cosmetology', 'promotion', ])		or prod.x_family in ['laser', 'medical', 'cosmetology']:

						procedure_line = pat_line.procedure_line.create({
																			'name': line.name,
																			'product_id': line.product_id.id,
																			'x_date_created': order.date_order,
																			'product_uom_qty': line.product_uom_qty,
																			'price_unit': line.price_unit,

																			'patient_line_proc_id': pat_line.id,
																			'marketing_id': self.id,
																		})
						# Sale Line Analysis - Procedure
						#mkt_funcs.pl_sale_line_analysis(self, line, pat_line)
						mkt_funcs.pl_sale_line_analysis_service(self, line, pat_line)



					if line.product_id.type in ['product']:
						# Sale Line Analysis - Product
						mkt_funcs.pl_sale_line_analysis_product(self, line, pat_line)




			# Update Counts
			self.patient_sale_count = self.patient_sale_count + len(pat_line.sale_line)
			self.patient_consu_count = self.patient_consu_count + len(pat_line.consu_line)
			self.patient_proc_count = self.patient_proc_count + len(pat_line.procedure_line)

			# Update Nrs
			pat_line.update_nrs()




		# Per - Vip
		#jx
		#if self.total_count != 0:
		#self.vip_true_per = mkt_funcs.get_per(self, self.vip_true, self.total_count)
		#self.vip_false_per = mkt_funcs.get_per(self, self.vip_false, self.total_count)

		#print('Per - Vip')
		#print(self.vip_true)
		#print(self.vip_false)
		if self.total_count not in [0]:
			self.vip_already_true_per = float(self.vip_already_true) / float(self.total_count)
			self.vip_true_per = float(self.vip_true) / float(self.total_count)
			self.vip_false_per = float(self.vip_false) / float(self.total_count)
		#print(self.vip_true_per)
		#print(self.vip_false_per)


		# QC
		t1 = timer()
		self.delta_sales = t1 - t0

	# update_sales



		#t1 = timer()
		#self.delta_sales_pl = t1 - t0




		#mode = 'normal'


		#self.patient_line.unlink()


			#emr = self.patient.x_id_code
			#phone_1 = self.patient.mobile
			#phone_2 = self.patient.phone
			#email = self.patient.email
