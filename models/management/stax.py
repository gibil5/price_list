# -*- coding: utf-8 -*-
"""
	For Update Stats

	Created: 			 9 Dec 2019
	Last updated: 		 9 Dec 2019
"""
import collections


# ----------------------------------------------------------- Update Stats ------------------------

def update_stats(self):
	"""
	Update Stats
		Doctors, 
		Families, 
		Sub-families

	Used by
		update_doctors
	"""
	print()
	print('X - Update Stats')


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

			if line.family in [False, '']:
				print()
				print('Error: Family')
				print(line.product_id.name)


			# Sub family
			sub_family_arr.append(line.sub_family)

			if line.sub_family in [False, '']:
				print()
				print('Error: Subfamily')
				print(line.product_id.name)



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



		# Doctor Stats - openhealth.management.doctor.line
		doctor.pl_stats()




# By Family

	# Count
	counter_family = collections.Counter(family_arr)



	# Create
	for name in counter_family:
		print(name)

		count = counter_family[name]
		amount = _h_amount[name]

		family = self.family_line.create({
												'name': name,

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
	for name in counter_sub_family:

		count = counter_sub_family[name]

		amount = _h_sub[name]

		name_sp = get_name_sp(name)

		sub_family = self.sub_family_line.create({
													'name': name,
													'name_sp': name_sp,

													'x_count': count,
													'amount': amount,
													'management_id': self.id,
											})
		#sub_family.update()



		# Percentage
		if self.total_amount != 0:
			sub_family.per_amo = sub_family.amount / self.total_amount

# update_stats



# ----------------------------------------------------------- Update ------------------------------

def get_name_sp(name):  
	"""
	Get name in spanish
	"""
	print()
	print('X - Get Name Sp')
	print(name)

	return name 





