# 12 Dec 2019


# ----------------------------------------------------------- Line Analysis - PL- Dep -----------------------
def pl_patient_line_analysis(self, line):
	"""
	New - 2019
	Used by: Marketing
	Patient Line Analysis to update counters
	"""
	print()
	print('X - Patient Line Analysis')



	if False:

		# Education 
		if line.education == 'first': 
			self.edu_fir = self.edu_fir + 1

		elif line.education == 'second': 
			self.edu_sec = self.edu_sec + 1

		elif line.education == 'technical': 
			self.edu_tec = self.edu_tec + 1

		elif line.education == 'university': 
			self.edu_uni = self.edu_uni + 1

		elif line.education == 'masterphd': 
			self.edu_mas = self.edu_mas + 1

		else: 
			self.edu_u = self.edu_u + 1


#none
#recommendation
#tv

#radio
#internet
#website

#mail_campaign
#facebook
#instagram

#callcenter
#old_patient
#undefined


# First Contact 
	if False:
		if line.first_contact == 'none': 
			self.how_none = self.how_none + 1

		elif line.first_contact == 'recommendation': 
			self.how_reco = self.how_reco + 1

		elif line.first_contact == 'tv': 
			self.how_tv = self.how_tv + 1



		elif line.first_contact == 'radio': 
			self.how_radio = self.how_radio + 1

		elif line.first_contact == 'internet': 
			self.how_inter = self.how_inter + 1

		elif line.first_contact == 'website':
			self.how_web = self.how_web + 1



		elif line.first_contact == 'mail_campaign':
			self.how_mail = self.how_mail + 1

		elif line.first_contact == 'facebook':
			self.how_facebook = self.how_facebook + 1

		elif line.first_contact == 'instagram':
			self.how_instagram = self.how_instagram + 1



		elif line.first_contact == 'callcenter':
			self.how_callcenter = self.how_callcenter + 1

		elif line.first_contact == 'old_patient':
			self.how_old_patient = self.how_old_patient + 1

		elif line.first_contact in [False, '']:
			self.how_u = self.how_u + 1

		else:
			print('Eror: This should not happen !')







# Sex
	if line.sex == 'Male': 
		self.sex_male = self.sex_male + 1
	elif line.sex == 'Female': 
		self.sex_female = self.sex_female + 1
	else: 
		self.sex_undefined = self.sex_undefined + 1



# Age Max and Min 
	#if line.age_years not in[ -1, 0]: 			# Not an Error 
	if line.age_years >= 0:
		#count_a = count_a + line.age_years 
		self.age_sum = self.age_sum + line.age_years 

		if line.age_years > self.age_max: 
			self.age_max = line.age_years

		if self.age_min in [0]:
			self.age_min = line.age_years

		else:			
			if line.age_years < self.age_min: 
				self.age_min = line.age_years
	else: 										# Error 
		self.age_undefined = self.age_undefined + 1











# 11 Dec 2019

# ----------------------------------------------------------- Calculate Percentages ------------------------------------------------------

# Provides Percentage
@api.multi
def get_per_dep(self, value, total):
	#print()
	#print('Pl - Get Per')
	#per = 0 
	per = 0.
	if total != 0: 
		#per = ( float(value) / float(total) ) * 100
		per = float(value) / float(total)
	return per
# get_per





# Highly Deprecated !


# ----------------------------------------------------------- Line Analysis - PL -----------------------
def line_analysis(self, line):
	"""
	New - 2019
	Marketing
	Analyses Line to update counters
	"""
	print()
	print('X - Line Analysis')
	#print(line)

	prod = line.product_id

	if prod.pl_price_list in ['2019']:
		self.price_list_2019_count = self.price_list_2019_count + line.product_uom_qty
	elif prod.pl_price_list in ['2018']:
		self.price_list_2018_count = self.price_list_2018_count + line.product_uom_qty
	else:
		print('Error: This should not happen !')




# ----------------------------------------------------------- Line Analysis - PL -----------------------
def pl_sale_line_analysis_product(self, line, pat_line):
	"""
	New - 2019
	Marketing
	Analyses Line
	"""
	print()
	print('X - Sale Line Analysis - Product')
	#print(line.product_id.name)

	# Product
	#if line.product_id.type in ['product']:
	if line.product_id.pl_family in ['card']:
		pat_line.vip = True
		#print('PL - Sale Line Analysis - Product')
		#print(line.product_id.name)
		#print('Gotcha')
		#print()
		self.vip_true = self.vip_true + 1
		self.vip_false = self.vip_false - 1


	#self.nr_products = self.nr_products + line.product_uom_qty

	pat_line.nr_products = pat_line.nr_products + line.product_uom_qty

	self.patient_product_count = self.patient_product_count + line.product_uom_qty




# ----------------------------------------------------------- Line Analysis - PL -----------------------
#def pl_sale_line_analysis(self, line, pat_line):
def pl_sale_line_analysis_service(self, line, pat_line):
	"""
	New - 2019
	Marketing
	Analyses Line to update counters
	"""
	print()
	print('X - Sale Line Analysis')
	
	#print(line)
	#print(line.product_id)
	#print(line.product_id.name)
	#print(line.product_id.pl_treatment)
	#print(line.product_id.pl_subfamily)
	#print(line.product_id.pl_pathology)
	#print(line.product_id.pl_zone)
	#print()

	# Service
	if line.product_id.type in ['service']:

		if line.product_id.pl_price_list in ['2019']:
			pat_line.proc_treatment = line.product_id.pl_treatment
			pat_line.proc_pathology = line.product_id.pl_pathology
			pat_line.proc_zone = line.product_id.pl_zone

		elif line.product_id.pl_price_list in ['2018']:
			pat_line.proc_treatment = line.product_id.x_treatment
			pat_line.proc_pathology = line.product_id.x_pathology
			pat_line.proc_zone = line.product_id.x_zone

