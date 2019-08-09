# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Project(models.Model):
	"""
	Project
	"""
	_name = 'price_list.project'

	name = fields.Char(
		)

	task_ids = fields.One2many(
			'price_list.task',
			'project_id',
		)


