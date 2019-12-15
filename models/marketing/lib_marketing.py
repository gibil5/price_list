# -*- coding: utf-8 -*-
"""
 	Price List 2019 - lib_marketing.py

 	Created: 			12 Dec 2019
 	Last up: 	 		14 Dec 2019
"""
import collections
try:
	import numpy as np
except (ImportError, IOError) as err:
	_logger.debug(err)

from origin import Origin
from city_line import CityLine
from district_line import DistrictLine


# ----------------------------------------------------------- Origin -------------------------------
def build_origin(self):  
	"""
	Build Origin - For Marketing
	"""
	print()
	print('X - Build Origin')

	# Clean
	self.origin_line.unlink()


	# Create Collection from Patient Lines
	origin_arr = []
	for line in self.patient_line: 
		origin_arr.append(line.origin)
	#print(origin_arr)


	# Using collections
	counter_origin = collections.Counter(origin_arr)


	# origin
	#print('Create origin Line ')
	for key in counter_origin:
		count = counter_origin[key]

		# Using Static method
		name_sp = Origin.get_sp_name(key)
		#print(key, name_sp)

		origin = self.origin_line.create({
												'name': key,
												'name_sp': name_sp,
												'count': count,
												'marketing_id': self.id,
											})
		#print origin





# ----------------------------------------------------------- Countries ------------------------------
def build_countries(self):
	"""
	Build Countries - For Marketing
	"""
	#print() 
	#print('X - Build Countries')


	# Clean
	self.country_line.unlink()


	# Create Collection from Patient Lines
	country_arr = []
	for line in self.patient_line: 
		country_arr.append(line.country)
	#print(country_arr)


	# Using collections
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



# ----------------------------------------------------------- Districts ---------------------------
def build_districts(self):  
	"""
	Build Districts - For Marketing
	Using Collections to count faster
	"""
	#print()
	#print('X - Build Districts')

	# Clean
	self.district_line.unlink()


	# Create Collection from Patient Lines
	district_arr = []
	for line in self.patient_line: 
		if line.city in ['Lima']: 
			district_arr.append(line.district)
	#print(district_arr)


	# Count Collection
	counter_district = collections.Counter(district_arr)
	#print(counter_district)


	# Create
	for key in counter_district:

		# Init
		count = counter_district[key]

		#sector = DistrictLine.district_sector[key]
		sector = DistrictLine.get_district_sector(key)

		#code = DistrictLine.zip_dic[key]
		code = DistrictLine.get_zip_code(key)

		# Create
		district = self.district_line.create({
												'name' : 		key, 
												'count' :		count,
												'code' :		code, 
												'sector' : 		sector, 
												'marketing_id' :	self.id, 
									})
		#print(district)

		# Update 
		district.update_fields()

# build_districts




# ----------------------------------------------------------- Cities ------------------------------
def build_cities(self):
	"""
	Build Cities - For Marketing
	"""
	#print() 
	#print('X - Build Cities')


	# Clean
	self.city_line.unlink()


	# Create Collection from Patient Lines
	city_arr = []
	for line in self.patient_line: 
		city_arr.append(line.city)


	# Count Collection
	counter_cities = collections.Counter(city_arr)


	# Create
	for key in counter_cities:

		# Init
		count = counter_cities[key]
		sector = CityLine.city_sector[key]

		# Create 
		city = self.city_line.create({
											'name' : 		key, 
											'sector' : 		sector, 
											'count' :		count,
											'marketing_id' :	self.id, 
									})
		
		# Update 
		city.update_fields()

# build_cities









# ----------------------------------------------------------- Histogram ---------------------------
def build_histogram(self):  
	"""
	Build Histogram - For Marketing
	"""
	#print()
	#print('X - Build Histogram')


	#input_arr = [15, 25, 26, 30, 44, 70]

	# Build Input Array
	input_arr = []
	input_arr_m = []
	input_arr_f = []

	for line in self.patient_line: 
		if line.age_years not in [0, -1]: 		# Not an Error 

			input_arr.append(line.age_years)

			if line.sex == 'Male': 
				input_arr_m.append(line.age_years)
			elif line.sex == 'Female': 
				input_arr_f.append(line.age_years)

	
	#print inp_arr


	# Bins
	inp_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 100]


	# Histogram 
	#histo = np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
	histo = np.histogram(input_arr, bins=inp_bins)
	histo_m = np.histogram(input_arr_m, bins=inp_bins)
	histo_f = np.histogram(input_arr_f, bins=inp_bins)


	# Update
	bins = histo[1]
	counts = histo[0]
	counts_m = histo_m[0]
	counts_f = histo_f[0]

	#print bins
	#print counts


	# Total 
	total = len(input_arr)


	# Init
	idx = 0 
	idx_max = 14

	# Clear 
	self.histo_line.unlink()

	for count in counts: 

		if idx < idx_max: 

			x_bin = bins[idx]

			#print idx 
			#print x_bin
			#print count 

			line = self.histo_line.create({
											'x_bin': x_bin, 
											'idx': idx, 
											'total': total, 
											'total_m': self.sex_male, 
											'total_f': self.sex_female, 
											'count': count, 
											'count_m': counts_m[idx], 
											'count_f': counts_f[idx], 
											'marketing_id': self.id, 
					})

			line.update_fields()
			idx = idx + 1

# build_histogram
