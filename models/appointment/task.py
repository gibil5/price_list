# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Task(models.Model):
	"""
	Task
	"""

	_name = 'price_list.task'


	project_id = fields.Many2one(
			'price_list.project',
		)

	user_id = fields.Many2one(
			#'res.user',
			'price_list.user',
		)

	planned_hours = fields.Char(
		)

