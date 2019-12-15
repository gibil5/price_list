# -*- coding: utf-8 -*-
"""
	Lib 

	For Marketing

	Created: 				14 Dec 2019
	Last up: 				14 Dec 2019
"""

from openerp import models, fields, api


# Create Model
def create_model(self, key):
	"""
	Abstract some Odoo Internals
	"""

	_dic_name = {
					'origin': 'Origen', 
					'education': 'Educación', 
					'first_contact': 'Primer Contacto', 
					'sex': 'Sexo', 
					'vip': 'Vip', 
					'age': 'Edad', 
	}

	_dic_model = {
					'origin': 'openhealth.marketing.origin', 
					'education': 'openhealth.marketing.education', 
					'first_contact': 'openhealth.marketing.first_contact', 
					'sex': 'openhealth.marketing.sex', 
					'vip': 'openhealth.marketing.vip', 
					'age': 'openhealth.marketing.age', 
	}


	name = _dic_name[key]

	model = _dic_model[key]

	obj = self.env[model].create({
										'name': name,
									})

	return obj 



# ----------------------------------------------------------- Clean ------------------------------

# Clean
@api.multi
def clean(self):
	"""
	Clean
	"""
	print('X - Clean')
	print('Begin')

	# If Test Obj
	if self.test_obj:

		# Clear
		self.patient_line.unlink()

		# Clear
		model = 'openhealth.marketing.order.line'

		objs = self.env[model].search([
											('marketing_id', 'in', [False]),
										],
										#order='date_begin asc',
										#limit=1,
			)

		# Unlink
		limit = 1000
		count = 0
		for obj in objs:
			if count < limit:
				obj.unlink()
				count = count + 1

		# Count
		count = self.env[model].search_count([
												('marketing_id', 'in', [False]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(count)
		print('End')
# clean

