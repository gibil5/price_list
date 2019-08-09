# -*- coding: utf-8 -*-
"""
 		Pricelist - Matrix

 		Created: 			 6 Aug 2019
		Last updated: 	 	 6 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Matrix(models.Model):
	"""
	Day Schedule for the Clini
	"""
	_name = 'price_list.matrix'

	_description = 'Price List Matrix'

	#_order = 'day_date asc'



	# ----------------------------------------------------------- Fields ---------------------
	appointment = fields.One2many(
			'price_list.appointment',
			'matrix_id',
		)

	#date = fields.Datetime(
	name = fields.Datetime(
			'Fecha',
		)







	# ----------------------------------------------------------- Update - Button ---------------------

	@api.multi
	def update(self):
		"""
		Update
		"""
		print()
		print('Update')


	# ----------------------------------------------------------- validate - Button ---------------------

	@api.multi
	def validate(self):
		"""
		validate
		"""
		print()
		print('validate')







