# -*- coding: utf-8 -*-
"""
 		Pricelist - Appointment

 		Created: 			 6 Aug 2019
		Last updated: 	 	 6 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Appointment(models.Model):
	"""
	Atomic Appointment
	"""

	_name = 'price_list.appointment'

	_description = 'Price List Appointment'

	#_order = 'appointment_date asc'




	x = fields.Char(
		)

	y = fields.Char(
		)

	value = fields.Char(
		)


	matrix_id = fields.Many2one(
			'price_list.matrix',
			ondelete='cascade', 
		)
