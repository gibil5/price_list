# 11 Dec 2019

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

