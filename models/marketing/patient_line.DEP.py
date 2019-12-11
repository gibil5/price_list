# 11 Dec 2019



# ----------------------------------------------------------- Update EMR - Dep ------------------------------------------------------

	def update_emr(self):
		"""
		New features - Sabina
		Patients lines should contain EMR info
		"""
		print()
		print('X - Update EMR')

		# EMR 
		self.treatment = self.env['openhealth.treatment'].search([
																	('patient','=', self.patient.name),
														],
														order='start_date desc',
														limit=1,)


		self.consultation = self.env['openhealth.consultation'].search([
																		('treatment','=', self.treatment.id),
														],
														order='evaluation_start_date desc',
														limit=1,)


		self.chief_complaint = self.treatment.chief_complaint


		self.diagnosis = self.consultation.x_diagnosis

	# update_emr





# ----------------------------------------------------------- Update Fields - Dep ------------------------------------------------------
	# Update Fields
	@api.multi
	def update_fields(self):  
		print()
		print('X - Update Fields - Patient Line')

		# Dep
		# 	city, district, age_years
		# 	sex 
		# 	education
		# 	first contact

		#return ret 

	# update_fields








# ----------------------------------------------------------- Update Fields - Dep ------------------------------------------------------
	# Update Fields
	@api.multi
	def update_fields(self):  
		print()
		print('X - Update Fields - Patient Line')


# Measures

# Places
		if self.city != False: 
			self.city = self.city.title()

		if self.district != False: 
			self.district = self.district.title()

		# Age 
		if self.age.split()[0] != 'No': 
			self.age_years = self.age.split()[0]
			ret = 1
		else:
			ret = -1




# Sex 
		if self.sex == 'Male': 
			self.mea_m = 1
		elif self.sex == 'Female':
			self.mea_f = 1
		else:
			self.mea_u = 1



# Vip 
		if self.vip: 
			self.mea_vip = 1
		else: 
			self.mea_vip_no	= 1



# Education
		if self.education == 'first': 
			self.mea_first = 1

		elif self.education == 'second': 
			self.mea_second = 1

		elif self.education == 'technical': 
			self.mea_technical = 1

		elif self.education == 'university': 
			self.mea_university = 1

		elif self.education == 'masterphd': 
			self.mea_masterphd = 1 

		else: 
			self.mea_edu_u = 1			



# First Contact 
		if self.first_contact == 'recommendation': 
			self.mea_recommendation = 1


		elif self.first_contact == 'tv': 
			self.mea_tv = 1

		elif self.first_contact == 'radio': 
			self.mea_radio = 1

		elif self.first_contact == 'internet': 
			self.mea_internet = 1



		elif self.first_contact == 'website': 
			self.mea_website = 1

		elif self.first_contact == 'mail_campaign': 
			self.mea_mail_campaign = 1

		elif self.first_contact == 'none': 
			self.mea_how_none = 1

		else: 
			self.mea_how_u = 1




# ----------------------------------------------------------- Adds ------------------------------------------------------

	def add_procedure_treatment(self, product):
		# All Price Lists
		#if product.pl_price_list in ['2019']:
		#	treatment = product.pl_treatment
		#else:
		#	treatment = product.x_treatment

		# All PL
		treatment = product.get_treatment()

		if treatment != self.proc_treatment:	
			if self.proc_treatment in [False]:
				self.proc_treatment = treatment
			else:	
				self.proc_treatment = self.proc_treatment + ', ' + treatment




	#def add_procedure_pathology(self, pathology):
	def add_procedure_pathology(self, product):

		# All Price Lists
		#if product.pl_price_list in ['2019']:
		#	pathology = product.pl_pathology
		#else:
		#	pathology = product.x_pathology


		# All PL
		pathology = product.get_pathology()

		if pathology != self.proc_pathology:	
			if self.proc_pathology in [False]:
				self.proc_pathology = pathology
			else:
				self.proc_pathology = self.proc_pathology + ', ' + pathology


	#def add_procedure_zone(self, zone):
	def add_procedure_zone(self, product):

		# All Price Lists
		#if product.pl_price_list in ['2019']:
		#	zone = product.pl_zone
		#else:
		#	zone = product.x_zone


		# All PL
		zone = product.get_zone()

		if zone != self.proc_zone:	
			if self.proc_zone in [False]:
				self.proc_zone = zone
			else:
				self.proc_zone = self.proc_zone + ', ' + zone










# Highly dep !

	# Sales - Dep !
	sale_line = fields.One2many(
			'openhealth.marketing.order.line',
			'patient_line_sale_id',
		)

