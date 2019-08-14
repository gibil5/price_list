# -*- coding: utf-8 -*-
"""
		Pricelist - Matrix

		Created: 			 6 Aug 2019
		Last updated: 	 	 6 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Matrix(models.Model):

	_name = 'price_list.matrix'

	_description = 'Price List Matrix'



	# ----------------------------------------------------------- Fields ---------------------
	name = fields.Char()


	task_ids = fields.Many2many(
			'price_list.task',
			relation='matrix_project_user_relation', 
			column1='project_id',
			column2='user_id', 
		)


	#attendee_ids = fields.Many2many(
	#		'management.student',
	#		relation='your_table_name', 
	#		column1='course_id',
	#		column2='student_id', 
	#		string="Attendees"
	#	)


